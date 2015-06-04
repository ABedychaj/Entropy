import numpy as np
import matplotlib.pyplot as plt
import math
import random
import re

pattern = re.compile('([^\s\w]|_)+')  # usuwamy wszystko poza bialymi znakami i literami/liczbami

f = open('Rota.txt', 'r')
# print(f.read())

''' usuwamy znaki interpunkcyjne '''
k = "".join(line for line in f if not line.isspace())
k = pattern.sub('', k)
dlugoscTekstu = len(k)
print(dlugoscTekstu)

Max_Block = 10
S = 701
R = [list() for _ in range(0, S)]
AveragesOfR = [0 for _ in range(0, Max_Block)]

''' Szukamy pierwszego powrotu n-bloku od s-tego miejsca '''
for i in range(0, S):
    for b in range(0, Max_Block):
        ReturnIndex = k.find(k[i:i + b + 1], i + 1)
        if ReturnIndex != -1:
            R[i].append(ReturnIndex - i)
        else:
            R[i].append(dlugoscTekstu)

A = np.array(R)
AveLog = [0 for _ in range(0, Max_Block)]
for i in range(0, Max_Block):
    tempAveLog = [t for t in A[:, i] if t > 0]
    temp = [abs(math.log(tempAveLog[t], 2.)) / (i + 1) for t in range(0, len(tempAveLog))]
    if sum(temp) == 0 or len(temp) == 0:
        continue
    else:
        AveLog[i] = sum(temp) / len(temp)

g2 = {i: AveLog[i] for i in range(1, len(AveLog))}
print(g2)
plt.plot(np.arange(1, len(AveLog), 1), list(g2.values()), color="red")
plt.ylabel('entropia')
plt.xlabel('n')
plt.savefig('RotaEntropia.png')
