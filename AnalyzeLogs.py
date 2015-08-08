# -*- coding: utf-8 -*-
import re
import glob
import math
import ast

import numpy as np
import matplotlib.pyplot as plt

Teksty = glob.glob('TestEpika32litery/*.log')
probability = []
empiricalEntropy = []
sredniaDlugoscTekstu = []
sredniaDlugoscPodciagu = []
ave14log = []
log14ave = []

for tekst in Teksty:
    helper = re.search('\\\(.*)\.log', tekst, flags=0)
    f = open(''.join(['TestEpika32litery/', helper.group(1), '.log']), 'r', encoding='utf-8')
    hlp = [ast.literal_eval(i.strip('\n')) for i in f.readlines()[0:6]]
    # hlpIndex = 14 if len(hlp[0]) > 14 else len(hlp[0]) - 1
    # ave14log.append(hlp[1][hlpIndex])
    # log14ave.append(hlp[0][hlpIndex])
    sredniaDlugoscTekstu.append(hlp[0])
    # probability.append(hlp[1])
    empiricalEntropy.append(hlp[2])
    sredniaDlugoscPodciagu.append(math.ceil(hlp[3]))

''''''''''''''''''''''''''''''''''''''

newFile = open(''.join(['TestAfterChanges.log']), 'w')
# print(empiricalEntropy, file=newFile)
# plt.plot(np.arange(0, len(probability), 1), ave14log, label='srednia logarytmu', lw=1, color='green')
# plt.ylabel('entropia')
# plt.xlabel('n')
# plt.legend(loc='best')
# plt.savefig(''.join(['ave14log.png']))
# plt.close('all')

print(empiricalEntropy, file=newFile)
plt.plot(np.arange(0, len(empiricalEntropy), 1), empiricalEntropy, label='Entropia', color="black", lw=1)
plt.ylabel('entropia')
plt.legend(loc='best')
plt.savefig(''.join(['TestAfterChangesEpika32Litery.png']))
plt.close('all')
newFile.close()

print(sum(sredniaDlugoscTekstu)/len(sredniaDlugoscTekstu))
print(sum(sredniaDlugoscPodciagu)/len(sredniaDlugoscPodciagu))
