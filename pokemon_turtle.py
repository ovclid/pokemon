import turtle
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

t = turtle.Turtle()

x = [-100]
y = [100]


def show(num):
    if num != -1 :
        t.up()
        t.goto(x[0], y[0])
        t.down()
        t.write(str(data[num]))
        y[0] = y[0] - 30
        
def search(name):
    for i in range(len(data)):
        #print(data[i][1])
        if data[i][1] == name:
            return i
    return -1

def rand_pick(num):
    p = []
    for i in range(num):
        p.append(random.randint(1, len(data)))

    return p


"""    
for i in range(10):
    t.up()
    t.goto(-450, 300 - i*20)
    t.down()
    t.write(str(data[i]))

t.up()
t.goto(-500,0)
t.down()
t.forward(1000)

for i in range(10):
    t.up()
    t.goto(-450, -100 - i*20)
    t.down()
    t.write(str(data[i]))
"""
