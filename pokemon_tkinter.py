import tkinter as tk
import random

f = open("pokemon.csv", "r", encoding = "utf-8")
data = f.readlines()
f.close()


for i in range(len(data)):
    data[i] = data[i].split(",")

str_index = [1,2,3]
for i in range(1, len(data)):
    for j in range(len(data[0])):
        if j in str_index:
            continue
        else:
            data[i][j] = int(data[i][j])

            
def process():
    text = e1.get()
    print(text)
    for i in range(len(data)):
        if data[i][1] == text:
            print(data[i])
            return
    print("찾지못했습니다")
    
    """
    for i in range(int(text)):
        num = random.randint(1, len(data))
        print(data[num])
    """
    
w = tk.Tk()

e1 = tk.Entry(w)
e1.grid(row = 0, column = 1)
b = tk.Button(w, text = "클릭", command = process)
b.grid(row = 0, column = 2)

w.mainloop()



