import numpy as np
import matplotlib.pyplot as plt
import math
import random

k = 7  # Przesunięcie Bernulliego (1/(k+1),4/(k+1));
prob = 1. / (k + 1)  # Prawdopodobieństwo symbolu '1';
entropy = -(1. - prob) * math.log(1. - prob, 2.) - prob * math.log(prob, 2.)
print(entropy)

Max_Block = 30  # maksymalny blok
N = round(2 ** (
    entropy * Max_Block))  # całkowita długość binarnego bloku x1x2x3... Istnieje szansa, że powrót nie pojawi się dla dużego bloku (bliskiego Max_Block) w próbce o długości N
print(N)

x = list()  # generowanie ciągu Bernulliego
for i in range(1, N + 1):
    x.append(math.trunc(random.randint(0, k) / k))

t = x.count(1) / N  # prawdopodobienstwo '1'
print(t)

seq = x[0: Max_Block]
print(seq)

t = seq.count(1) / Max_Block  # prawdopodobienstwo '1' w bloku
print(t)

zxc = ''.join([str(tempX) for tempX in x])
tempR = list()
for i in range(0, Max_Block - 1):
    ReturnIndex = zxc.find(zxc[0:i + 1], i + 1)
    # print(zxc[0:i + 1])
    if ReturnIndex != -1:
        tempR.append(ReturnIndex)
    else:
        break

print(tempR)

# Algorytm z pracy Cho - nieoptymalny w Pythonie
# R = list()
# k = 1
# R.append(k)
# for n in range(0, Max_Block - 1):
#     if x[n] != x[n + 1]:
#         k += 1
#     R.append(k)
# print(R)

g1 = {i: abs(math.log(tempR[i - 1], 2.)) / i for i in range(1, len(tempR))}
print(g1)

plt.plot(np.arange(1, len(tempR), 1), list(g1.values()))
plt.axhline(entropy, lw=2, color='black', label=str(entropy))
plt.suptitle(''.join(str(b) for b in seq), fontsize=10)
plt.ylabel('entropia')
plt.xlabel('n')
plt.legend()
plt.savefig('FirstTime.png')
