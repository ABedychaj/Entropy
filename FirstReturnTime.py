import numpy as np
import matplotlib.pyplot as plt
import math
import random
import time

k = 5  # Przesunięcie Bernulliego (1/(k+1),4/(k+1));
prob = 1. / (k + 1)  # Prawdopodobieństwo symbolu '1';
entropy = -(1. - prob) * math.log(1. - prob, 2.) \
          - prob * math.log(prob, 2.)

f = open(''.join(['FirstReturnTime/FirstTime', 'Prawdopodobienstwo1_', str(prob), '_', str(int(time.time())), '.log']), 'w')
print(entropy, file=f)

Max_Block = 15 # maksymalny blok
N = round(2 ** (
    entropy * Max_Block))  # całkowita długość binarnego bloku x1x2x3...
                           # Istnieje szansa, że powrót nie pojawi się dla dużego bloku (bliskiego Max_Block) w próbce o długości N
print(N, file=f)

x = list()  # generowanie ciągu Bernulliego
for i in range(1, N + 1):
    x.append(math.trunc(random.randint(0, k) / k))

empiricalProb = x.count(1) / N  # prawdopodobienstwo '1'
print(empiricalProb, file=f)

seq = x[0: Max_Block]
print(seq, file=f)

t = seq.count(1) / Max_Block  # prawdopodobienstwo '1' w bloku
print(t, file=f)

fullBinarySeries = ''.join([str(tempX) for tempX in x])
tempR = list()
for i in range(0, Max_Block - 1):
    ReturnIndex = fullBinarySeries.find(fullBinarySeries[0:i + 1],
                                        1)
    # print(fullBinarySeries[0:i + 1])
    if ReturnIndex != -1:
        tempR.append(ReturnIndex)
    else:
        break

print(tempR, file=f)

# Algorytm z pracy Cho - nieoptymalny w Pythonie
# R = list()
# k = 1
# R.append(k)
# for n in range(0, Max_Block - 1):
#     if x[n] != x[n + 1]:
#         k += 1
#     R.append(k)
# print(R)

g1 = {i: abs(math.log(tempR[i - 1], 2.)) / i
      for i in range(1, len(tempR))}
print(g1, file=f)

plt.plot(np.arange(1, len(tempR), 1), list(g1.values()))
plt.axhline(entropy, lw=2, color='black', label=str(entropy))
# plt.suptitle(''.join(str(b) for b in seq), fontsize=6)
plt.ylabel('entropia')
plt.xlabel('n')
plt.legend(loc='best')
plt.savefig(''.join(['FirstReturnTime/FirstTime', 'Prawdopodobienstwo1_', str(prob), '_', str(int(time.time())), '.png']))
f.close()
