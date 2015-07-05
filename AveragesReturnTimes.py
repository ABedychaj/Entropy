import numpy as np
import matplotlib.pyplot as plt
import math
import random
import time

k = 9  # Przesuniecie Bernulliego (1/(k+1),4/(k+1));
prob = 1. / (k + 1)  # Prawdopodobienstwo symbolu '1';
entropy = -(1. - prob) * math.log(1. - prob, 2.) - prob * math.log(prob, 2.)

f = open(''.join(['AvReturnTime/AveTimes', 'Prawdopodobienstwo1_', str(prob), '_', str(int(time.time())), '.log']), 'w')
print(entropy, file=f)

Max_Block = 20  # maksymalny blok
N = round(2 ** (
    entropy * Max_Block)) * 200  # mnozymy * 200, gdyz dla duzych Max_Block powtorzenie moze sie nie pojawic.
print(N, file=f)
print(N)

x = list()  # generowanie ciagu Bernulliego
for i in range(1, N + 1):
    x.append(math.trunc(random.randint(0, k) / k))

t = x.count(1) / N  # prawdopodobienstwo '1'
print(t, file=f)

binarySeries = ''.join([str(tempX) for tempX in x])

S = 5000
M = N - Max_Block - S + 2
print(M, file=f)

R = [list() for _ in range(0, S)]
''' Szukamy pierwszego powrotu n-bloku od s-tego miejsca '''
for i in range(0, S):
    for b in range(0, Max_Block):
        ReturnIndex = binarySeries.find(binarySeries[i:i + b + 1], i + 1)
        if ReturnIndex != -1:
            R[i].append(ReturnIndex - i)
        else:
            break
            #R[i].append(N)

AveragesOfR = [0 for _ in range(0, Max_Block)]
for i in range(0, Max_Block):
    tempAve = list()
    for j in range(0, S):
        if len(R[j]) > i:
            tempAve.append(R[j][i])
    AveragesOfR[i] = sum(tempAve) / len(tempAve)

g1 = {i: abs(math.log(AveragesOfR[i - 1], 2.)) / i
      for i in range(1, len(AveragesOfR))}
print(g1, file=f)

plt.plot(np.arange(1, len(AveragesOfR), 1), list(g1.values()), label='logarytm srednich', lw=3)
plt.axhline(entropy, lw=2, color='black', label=str(entropy))
plt.ylabel('entropia')
plt.xlabel('n')


AveLog = [0 for _ in range(0, Max_Block)]
for i in range(0, Max_Block):
    tempAveLog = list()
    for j in range(0, S):
        if len(R[j]) > i:
            tempAveLog.append(R[j][i])
    temp = [abs(math.log(tempAveLog[t], 2.)) / (i + 1)
            for t in range(0, len(tempAveLog))]
    if sum(temp) == 0 or len(temp) == 0:
        continue
    else:
        AveLog[i] = sum(temp) / len(temp)

g2 = {i: AveLog[i] for i in range(1, len(AveLog))}
print(g2, file=f)
plt.plot(np.arange(1, len(AveLog), 1), list(g2.values()), color="red", label='srednie logarytmu', lw=3)
plt.legend(loc='best')
plt.savefig(''.join(['AvReturnTime/AveTimes', 'Prawdopodobienstwo1_', str(prob), '_', str(int(time.time())), '.png']))
