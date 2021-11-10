from random import randint
import numpy as np
import os
from tabulate import tabulate

def randomize_expert(i, j):
    x = [[randint(1,7) for i in range(i)] for j in range(j)]
    return x

criterion = []
with open('Criterion.txt', 'r', encoding="utf-8") as file:
    for line in file:
        criterion.append(line[:-1])

resorts = []
with open('Resorts.txt', 'r', encoding="utf-8") as file:
    for line in file:
        resorts.append(line[:-1])

importance = []
with open('importance.txt', 'r') as file:
    data_importance = file.read().split()
    for elem in data_importance:
        importance.append(float(elem))
importance = np.float_(importance)

ex1 = []
if os.stat("expert1.txt").st_size == 0:
    with open("expert1.txt", "w+") as expert1:
        ex1 = randomize_expert(len(criterion), len(resorts))
        r = np.array(ex1)
        np.savetxt(expert1, r, fmt="%4d", delimiter="", newline="\n")
else:
    ex1 = np.loadtxt("expert1.txt", dtype=int)
        
ex2 = []
if os.stat("expert2.txt").st_size == 0:
    with open("expert2.txt", "w+") as expert2:
        ex2 = randomize_expert(len(criterion), len(resorts))
        r = np.array(ex2)
        np.savetxt(expert2, r, fmt="%4d", delimiter="", newline="\n")
else:
    ex2 = np.loadtxt("expert2.txt", dtype=int)

ex3 = []
if os.stat("expert3.txt").st_size == 0:
    with open("expert3.txt", "w+") as expert3:
        ex3 = randomize_expert(len(criterion), len(resorts))
        r = np.array(ex3)
        np.savetxt(expert3, r, fmt="%4d", delimiter="", newline="\n")
else:
    ex3 = np.loadtxt("expert3.txt", dtype=int)

ex4 = []
if os.stat("expert4.txt").st_size == 0:
    with open("expert4.txt", "w+") as expert4:
        ex4 = randomize_expert(len(criterion), len(resorts))
        r = np.array(ex4)
        np.savetxt(expert4, r, fmt="%4d", delimiter="", newline="\n")
else:
    ex4 = np.loadtxt("expert4.txt", dtype=int)

all_add = np.add(np.add(ex1, ex2), np.add(ex3, ex4))
res = np.round(np.multiply(all_add, importance), 3)
res = res.transpose()

sum_of_res = np.sum(res, axis=0)
sum_of_res = list(sum_of_res)
sum_of_res.insert(0, sum(importance))
sum_of_res.insert(0, "Сума")

all_criterion = []
for i in range(len(res)):
    all_criterion.append(list(res[i]))

numeric_resorts = []
for i in range(0, len(resorts)):
    print(str(i+1) + ". " + resorts[i])
    numeric_resorts.append(i+1)

all_criterion.insert(0, numeric_resorts)
all_criterion[0].insert(0, 'Вага:')
all_criterion[0].insert(0, 'Параметри:')
for i in range(1, len(all_criterion)):
    all_criterion[i].insert(0, importance[i-1])
    all_criterion[i].insert(0, criterion[i-1])    

all_criterion.append(sum_of_res)

show = tabulate(all_criterion, headers='firstrow', tablefmt='fancy_grid', 
                numalign='center', showindex=range(1,len(all_criterion)))
print(show)




