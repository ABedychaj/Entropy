import numpy as np
import matplotlib.pyplot as plt
import math
import random

k = 25  # Przesuniecie Bernulliego (1/(k+1),4/(k+1));
prob = 1. / (k + 1)  # Prawdopodobienstwo symbolu '1';
entropy = -(1. - prob) * math.log(1. - prob, 2.) - prob * math.log(prob, 2.)
print(entropy)

Max_Block = 45  # maksymalny blok
N = round(2 ** (
    entropy * Max_Block)) * 200  # mnozymy * 200, gdyz dla duzych Max_Block powtorzenie moze sie nie pojawic.
print(N)

x = list()  # generowanie ciagu Bernulliego
for i in range(1, N + 1):
    x.append(math.trunc(random.randint(0, k) / k))

t = x.count(1) / N  # prawdopodobienstwo '1'
print(t)

zxc = ''.join([str(tempX) for tempX in x])

S = 1000
M = N - Max_Block - S + 2
print(M)

R = [list() for _ in range(0, S)]
AveragesOfR = [0 for _ in range(0, Max_Block)]
''' Szukamy pierwszego powrotu n-bloku od s-tego miejsca '''
for i in range(0, S):
    for b in range(0, Max_Block):
        ReturnIndex = zxc.find(zxc[i:i + b + 1], i + 1)
        if ReturnIndex != -1:
            R[i].append(ReturnIndex-i)
        else:
            # print(b)
            R[i].append(N)

A = np.array(R)
for i in range(0, Max_Block):
    tempAve = [t for t in A[:, i] if t > 0]
    AveragesOfR[i] = sum(tempAve) / len(tempAve)

g1 = {i: abs(math.log(AveragesOfR[i - 1], 2.)) / i for i in range(1, len(AveragesOfR))}
print(g1)

plt.plot(np.arange(1, len(AveragesOfR), 1), list(g1.values()))
plt.axhline(entropy, lw=2, color='black', label=str(entropy))
plt.ylabel('entropia')
plt.xlabel('n')
plt.legend()

AveLog = [0 for _ in range(0, Max_Block)]
for i in range(0, Max_Block):
    tempAveLog = [t for t in A[:, i] if t > 0]
    temp = [abs(math.log(tempAveLog[t], 2.)) / (i + 1) for t in range(0, len(tempAveLog))]
    AveLog[i] = sum(temp) / len(temp)

g2 = {i: AveLog[i] for i in range(1, len(AveLog))}
print(g2)
plt.plot(np.arange(1, len(AveLog), 1), list(g2.values()), color="red")
plt.savefig('AveTimes.png')
