import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException,\
     UnexpectedAlertPresentException
import pandas as pd

"""
url = 'https://pokemon.fandom.com/ko/wiki/%EC%A0%84%EA%B5%AD%EB%8F%84%EA%B0%90'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup)

    f = open("test.html", "w", encoding = 'utf-8')
    f.write(html)
    f.close()

else : 
    print(response.status_code)

"""

chrome_driver = r'C:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver)
url ='https://pokemon.fandom.com/ko/wiki/%EC%A0%84%EA%B5%AD%EB%8F%84%EA%B0%90'
driver.get(url)
time.sleep(1)

num_xpath = '//*[@id="mw-content-text"]/div/table[1]/tbody/tr[2]/td[2]'
name_xpath = '//*[@id="mw-content-text"]/div/table[1]/tbody/tr[2]/td[4]/a'
type1_xpath = '//*[@id="mw-content-text"]/div/table[1]/tbody/tr[2]/td[5]/span/a[1]/span'
type2_xpath = ' //*[@id="mw-content-text"]/div/table[1]/tbody/tr[2]/td[5]/span/a[2]/span'

cols = ["순번", "이름", "속성1", "속성2"]
df = pd.DataFrame(columns = cols)

num = 0

num_list = [151, 251, 386, 493, 649, 721, 809, 898]
total_cnt = 0

f = open("포켓몬.txt", "w")

for i in range(len(num_list)):
    cnt = 0
    file_write = ''
    
    while num <= num_list[i]-1 :
        
        num_xpath = f'//*[@id="mw-content-text"]/div/table[{i+1}]/tbody/tr[{cnt+2}]/td[2]'
        name_xpath = f'//*[@id="mw-content-text"]/div/table[{i+1}]/tbody/tr[{cnt+2}]/td[4]/a'
        type1_xpath = f'//*[@id="mw-content-text"]/div/table[{i+1}]/tbody/tr[{cnt+2}]/td[5]/span/a[1]/span'
        type2_xpath = f' //*[@id="mw-content-text"]/div/table[{i+1}]/tbody/tr[{cnt+2}]/td[5]/span/a[2]/span'  
        cnt = cnt + 1
        
        temp = []
        try :
            num = driver.find_element_by_xpath(num_xpath)
            num = int(num.text.strip("#"))
            
            name = driver.find_element_by_xpath(name_xpath)
            type1 = driver.find_element_by_xpath(type1_xpath)
            type2 = driver.find_element_by_xpath(type2_xpath)

            df.loc[total_cnt, "순번"] = num
            df.loc[total_cnt, "이름"] = name.text
            df.loc[total_cnt, "속성1"] = type1.text
            df.loc[total_cnt, "속성2"] = type2.text

            total_cnt = total_cnt + 1
            file_write = str(num) + ',' + name.text + ',' + type1.text+ ','
            
        except NoSuchElementException:
                print(num, name.text, type1.text+'\n')
                f.write(file_write)
                continue

        print(num, name.text, type1.text, type2.text)
        f.write(file_write + ',' + type2.text + '\n')
        df.loc[i, "속성2"] = type2.text

f.close()
df.to_excel("포켓몬 도감.xlsx", index = False)

