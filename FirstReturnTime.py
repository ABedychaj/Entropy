import numpy as np
import matplotlib.pyplot as plt
import math
import random

k = 5  # Przesunięcie Bernulliego (1/(k+1),4/(k+1));
prob = 1. / (k + 1)  # Prawdopodobieństwo symbolu '1';
entropy = -(1. - prob) * math.log(1. - prob, 2.) - prob * math.log(prob, 2.)
print(entropy)

Max_Block = 20  # maksymalny blok
N = round(2 ** (
    entropy * Max_Block))  # całkowita długość binarnego bloku x1x2x3... Istnieje szansa, że powrót nie pojawi się dla dużego bloku (bliskiego Max_Block) w próbce o długości N
print(N)

x = list()  # generowanie ciągu Bernulliego
for i in range(1, N + 1):
    x.append(math.trunc(random.randint(1, k) / k))

t = x.count(1) / N  # prawdopodobienstwo '1'
print(t)

seq = x[0: Max_Block]
print(seq)

t = seq.count(1) / Max_Block  # prawdopodobienstwo '1' w bloku
print(t)

''' Policzmy czas pierwszego powrotu '''
R = list()
for n in range(0, Max_Block):
    k = 1
    tempSum = 0
    for j in range(0, n):
        tempSum = abs(x[j] - x[j + k])
        if tempSum > 0:
            k += 1
    R.append(k)
print(R)

g1 = {i: abs(math.log(R[i - 1] / i, 2.)) for i in range(1, Max_Block + 1)}
print(g1)

plt.plot(np.arange(1, Max_Block + 1, 1), list(g1.values()))
plt.plot([1, Max_Block], [entropy, entropy], 'k-', lw=2)
plt.savefig('foo.png')
