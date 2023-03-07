import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from unicodedata import normalize

table_radio = pd.read_html('https://www.vases.lv/lv/broadcasting_fm')
frex =[]

df = table_radio[0]
df.head()


frey = df['Frekv., MHz'].values.tolist()
frey.sort()
print(frey)
freq = set(frey)


for i in range(875,1080):
    i = i/10
    frex.append(i)

for j in freq:
    if j in frex:
        frex.remove(j)
    else: continue
    
print('Aiznemtās frekvences:\n{}\n'.format(freq))
print('Brīvās frekvences:\n{}'.format(frex))
