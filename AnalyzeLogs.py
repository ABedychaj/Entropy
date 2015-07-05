import math
import re
import glob

import numpy as np
import matplotlib.pyplot as plt

pattern = re.compile('([^\s\w]|_)+')  # usuwamy wszystko poza bialymi znakami i literami/liczbami
Teksty = glob.glob('TekstyLirykaAnaliza/*.log')
probability = []
empiricalEntropy = []

for tekst in Teksty:
    helper = re.search('\\\(.*)\.log', tekst, flags=0)
    f = open(''.join(['TekstyLirykaAnaliza/', helper.group(1), '.log']), 'r', encoding='utf-8')
    hlp = [float(i.strip('\n')) for i in f.readlines()[1:3]]
    probability.append(hlp[0])
    empiricalEntropy.append(hlp[1])

''''''''''''''''''''''''''''''''''''''

newFile = open(''.join(['FinalResultForLirykaProbabilityAndEmpiricalEntropy.log']), 'w')
print(probability, file=newFile)
plt.plot(np.arange(0, len(probability), 1), probability, label='Prawdopodobienstwo', color="green", lw=1)
plt.ylabel('prawdopodobienstwo')
plt.legend(loc='best')
plt.savefig(''.join(['FinalResultForLirykaProbability.png']))
plt.close('all')

print(empiricalEntropy, file=newFile)
plt.plot(np.arange(0, len(empiricalEntropy), 1), empiricalEntropy, label='Entropia', color="black", lw=1)
plt.ylabel('entropia')
plt.legend(loc='best')
plt.savefig(''.join(['FinalResultForLirykaEmpiricalEntropy.png']))
plt.close('all')
newFile.close()
