import numpy as np
import matplotlib.pyplot as plt
import math
import random

k = 3  # Przesuniecie Bernulliego (1/(k+1),4/(k+1));
prob = 1. / (k + 1)  # Prawdopodobienstwo symbolu '1';
entropy = -(1. - prob) * math.log(1. - prob, 2.) - prob * math.log(prob, 2.)
print(entropy)

Max_Block = 12  # maksymalny blok
N = round(2 ** (
    entropy * Max_Block)) * 200  # mnozymy * 200, gdyz dla duzych Max_Block powtorzenie moze sie nie pojawic.
print(N)

x = list()  # generowanie ciagu Bernulliego
for i in range(1, N + 1):
    x.append(math.trunc(random.randint(0, k) / k))

t = x.count(1) / N  # prawdopodobienstwo '1'
print(t)

S = 10
M = N - Max_Block - S + 2
print(M)

# R = [[0 for x in range(0, Max_Block)] for x in range(0, S)]
#
# for s in range(0, S):
#     R[s][0] = 1
#
# for s in range(0, S):
#     for n in range(0, Max_Block):
#         k = R[s][n]
#         i = 1
#         while i <= n and k <= M:
#             if x[s + i - 1] == x[s + i - 1 + k]:
#                 i += 1
#             else:
#                 k += 1
#                 i = 1
#         print(k)
#         R[s][n] = k
#
# print(R)
