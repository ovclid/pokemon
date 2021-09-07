import shutil
import pandas as pd

##################   사용자 함수 정의   #####################################
# 포켓몬 다국어 이름으로 저장된 파일을 읽어들임
# 출처 : https://pokemon.fandom.com/ko/wiki/%EA%B5%AD%EA%B0%80%EB%B3%84_%ED%8F%AC%EC%BC%93%EB%AA%AC_%EC%9D%B4%EB%A6%84_%EB%AA%A9%EB%A1%9D
def read_file(filename):
    f = open(filename, "r", encoding="utf-8")
    data = f.readlines()
    f.close()
    
    for i in range(len(data)):
        data[i] = data[i].split()
    
    return data

# 외부용 PC에서 엑셀파일은 자동 삭제되어 확장자명을 달리하여 저장해 놓고
# 필요시 엑셀파일(확장자)로 복사하여 사용
# 출처 : pokemondb.net -> pokemon with stat
def copy_to_excel(src_file):
    target_filename = src_file.split('.')[0] + '.xlsx'
    shutil.copy(src_file, target_filename)

######################   메인 프로세스 #####################################
    
data = read_file("포켓몬.t")
copy_to_excel("포켓몬.x")


cols = ["번호", "이름", "타입", "총합", "HP", "공격력", "방어력", "특별공격력", "특별방어력", "속도"]
df = pd.read_excel("포켓몬.xlsx", names = cols)
#df.columns = cols

df["별칭"] = ""
cols.insert(2, "별칭")
df = df[cols]

# 인터넷에서 포켓몬 정보를 복사해 엑셀에 저장하면 일부 캐릭터는 엑셀 2줄을 차지하므로
# 필요없는 행은 삭제, 다만 이름에 대한 추가 정보는 별도의 열에 저장함

for i in range(len(df)):
    if pd.isnull(df.loc[i, "번호"]) == True:
        if pd.isnull(df.loc[i, "이름"]) == False:
            df.loc[i-1, "별칭"] = df.loc[i, "이름"]
        df = df.drop(i, 0)

# '이름, 타입'을 제외한 '순번, 총합, 공격력 등'을 float -> int 타입으로 변경
str_columns = ["이름", "타입", "별칭"]
for i in cols:
    print(i)
    if i in str_columns:
        continue
    else:
        df[i] = df[i].astype(int)
        
df.reset_index(drop = True, inplace = True)

# 영문 이름을 국문 이름으로 변경
for i in range(len(df)):
    for j in range(len(data)):
        if df.loc[i, "이름"] == data[j][3] :
            df.loc[i, "이름"] = data[j][1]

df.to_excel("result.xlsx", index=False)
df.to_csv("result.csv", index=False)
