# -*- coding: utf-8 -*-
import math
import re
import glob

import numpy as np
import matplotlib.pyplot as plt

pattern = re.compile('([^\s\w]|_)+')  # usuwamy wszystko poza bialymi znakami i literami/liczbami
Teksty = glob.glob('Epika/*.txt')
AvgEntropy = list()
LogAvgEntropy = list()
polishAlphabet = [
    'a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n',
    'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż'
]

for tekst in Teksty:
    helper = re.search('\\\(.*)\.txt', tekst, flags=0)
    toAnalyze = open(''.join(['Epika/', helper.group(1), '.txt']), 'r', encoding='utf-8')

    f = open(''.join(['TestEpika32litery/', helper.group(1), '.log']), 'w')
    ''' usuwamy znaki interpunkcyjne '''
    k = "".join(line for line in toAnalyze if not line.isspace())
    k = k.lower()  # wielkość liter ma znaczenie, więc spróbujmy najpierw ujednolicenia
    k = pattern.sub('', k)
    # if helper.group(1) == 'confiteor':
    #     print(k)

    # binary = ' '.join(format(ord(x), 'b') for x in k).replace(' ', '')  # tlumaczymy tekst na binarny
    # print(binary)
    dlugoscTekstu = len(k)
    print(dlugoscTekstu, file=f)

    prob = [k.count(str(t)) / dlugoscTekstu for t in polishAlphabet]
    entropy = sum([0 if t == 0 else -t * math.log(t, len(polishAlphabet))
                   for t in prob])
    print(prob, file=f)
    print(entropy, file=f)
    print(abs(math.log(dlugoscTekstu, len(polishAlphabet) * entropy)), file=f)

    Max_Block = math.ceil(abs(math.log(dlugoscTekstu,
                                       len(polishAlphabet) * entropy)))
    Max_Block = 10
    S = 5000
    R = [list() for _ in range(0, S)]
    AveragesOfR = [0 for _ in range(0, Max_Block)]

    ''' Szukamy pierwszego powrotu n-bloku od s-tego miejsca '''
    for i in range(0, S):
        for b in range(0, Max_Block):
            ReturnIndex = k.find(k[i:i + b + 1], i + 1)
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
        if not tempAve:
            AveragesOfR = AveragesOfR[0:i - 1]
            break
        else:
            AveragesOfR[i] = sum(tempAve) / len(tempAve)

    g1 = {i: abs(math.log(AveragesOfR[i - 1], len(polishAlphabet))) / i
          for i in range(1, len(AveragesOfR))}
    print(g1, file=f)

    plt.plot(np.arange(1, len(AveragesOfR), 1), list(g1.values()), label='logarytm srednich', lw=2)

    AveLog = [0 for _ in range(0, Max_Block)]
    for i in range(0, Max_Block):
        tempAveLog = list()
        for j in range(0, S):
            if len(R[j]) > i:
                tempAveLog.append(R[j][i])
        temp = [abs(math.log(tempAveLog[t], len(polishAlphabet)))
                / (i + 1) for t in range(0, len(tempAveLog))]
        if sum(temp) == 0 or len(temp) == 0:
            AveLog = AveLog[0:i - 1]
            continue
        else:
            AveLog[i] = sum(temp) / len(temp)

    g2 = {i: AveLog[i] for i in range(1, len(AveLog))}
    print(g2, file=f)
    plt.plot(np.arange(1, len(AveLog), 1), list(g2.values()), label='srednia logarytmu', color="red", lw=2)
    plt.ylabel('entropia')
    plt.xlabel('n')
    plt.legend(loc='best')
    plt.savefig(''.join(['TestEpika32litery/', helper.group(1), '.png']))
    plt.close('all')
    AvgEntropy.append(g2[1 if len(g2) == 1 else len(g2) - 1])
    LogAvgEntropy.append(g1[1 if len(g1) == 1 else len(g1) - 1])
    f.close()

newFile = open(''.join(['TestEpika32litery', str(Max_Block), '.log']), 'w')
print(np.arange(1, len(AvgEntropy), 1))
print(AvgEntropy, file=newFile)
print(LogAvgEntropy, file=newFile)
plt.plot(np.arange(0, len(AvgEntropy), 1), AvgEntropy, label='srednia logarytmu', color="red", lw=1)
plt.plot(np.arange(0, len(LogAvgEntropy), 1), LogAvgEntropy, label='logarytm sredniej', color="blue", lw=1)
plt.ylabel('entropia')
plt.xlabel('n')
plt.legend(loc='best')
plt.savefig(''.join(['TestEpika32litery', str(Max_Block), '.png']))
plt.close('all')
newFile.close()
