# -*- coding: utf-8 -*-
import math
import re
import glob

import numpy as np
import matplotlib.pyplot as plt

pattern = re.compile('([^\s\w]|_)+')  # usuwamy wszystko poza bialymi znakami i literami/liczbami
Teksty = glob.glob('Liryka/*.txt')
# Teksty = glob.glob('Epika/*.txt')
AvgEntropy = list()
LogAvgEntropy = list()

for tekst in Teksty:
    helper = re.search('\\\(.*)\.txt', tekst, flags=0)
    toAnalyze = open(''.join(['Liryka/', helper.group(1), '.txt']), 'r', encoding='utf-8')

    f = open(''.join(['TekstyLirykaAnaliza/', helper.group(1), '.log']), 'w')
    ''' usuwamy znaki interpunkcyjne '''
    k = "".join(line for line in toAnalyze if not line.isspace())
    k = pattern.sub('', k)
    # if helper.group(1) == 'confiteor':
    #     print(k)

    binary = ' '.join(format(ord(x), 'b') for x in k).replace(' ', '')  # tlumaczymy tekst na binarny
    # print(binary)
    dlugoscTekstu = len(binary)
    print(dlugoscTekstu, file=f)

    prob = binary.count('1') / dlugoscTekstu
    entropy = -(1. - prob) * math.log(1. - prob, 2.) \
              - prob * math.log(prob, 2.)
    print(prob, file=f)
    print(entropy, file=f)
    print(abs(math.log(dlugoscTekstu, 2. * entropy)), file=f)

    Max_Block = math.ceil(abs(math.log(dlugoscTekstu, 2. * entropy)))
    S = 5000
    R = [list() for _ in range(0, S)]
    AveragesOfR = [0 for _ in range(0, Max_Block)]

    ''' Szukamy pierwszego powrotu n-bloku od s-tego miejsca '''
    for i in range(0, S):
        for b in range(0, Max_Block):
            ReturnIndex = binary.find(binary[i:i + b + 1], i + 1)
            if ReturnIndex != -1:
                R[i].append(ReturnIndex - i)
            else:
                break

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

    plt.plot(np.arange(1, len(AveragesOfR), 1), list(g1.values()), label='logarytm srednich', lw=2)

    AveLog = [0 for _ in range(0, Max_Block)]
    for i in range(0, Max_Block):
        tempAveLog = list()
        for j in range(0, S):
            if len(R[j]) > i:
                tempAveLog.append(R[j][i])
        temp = [abs(math.log(tempAveLog[t], 2.)) / (i + 1) for t in range(0, len(tempAveLog))]
        if sum(temp) == 0 or len(temp) == 0:
            continue
        else:
            AveLog[i] = sum(temp) / len(temp)

    g2 = {i: AveLog[i] for i in range(1, len(AveLog))}
    print(g2, file=f)
    plt.plot(np.arange(1, len(AveLog), 1), list(g2.values()), label='srednia logarytmu', color="red", lw=2)
    plt.ylabel('entropia')
    plt.xlabel('n')
    plt.legend(loc='best')
    plt.savefig(''.join(['TekstyLirykaAnaliza/', helper.group(1), '.png']))
    plt.close('all')
    AvgEntropy.append(g2[len(g2)-1])
    LogAvgEntropy.append(g1[len(g1)-1])
    f.close()

newFile = open(''.join(['FinalResultForLiryka.log']), 'w')
print(np.arange(1, len(AvgEntropy), 1))
print(AvgEntropy, file=newFile)
print(LogAvgEntropy, file=newFile)
plt.plot(np.arange(0, len(AvgEntropy), 1), AvgEntropy, label='srednia logarytmu', color="red", lw=1)
plt.plot(np.arange(0, len(LogAvgEntropy), 1), LogAvgEntropy, label='logarytm sredniej', color="blue", lw=1)
plt.ylabel('entropia')
plt.xlabel('n')
plt.legend(loc='best')
plt.savefig(''.join(['FinalResultForLiryka.png']))
plt.close('all')
newFile.close()
