# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 21:25:52 2018

@author: samba
"""
import pandas as pd

      
data = pd.read_csv('C:/Users/sceli/Documents/ProjetTableauBord/key_words_ef.csv')


dico = data.to_dict()
dico['0']
dico['1']
tab=[]
tab2=[]
for k,v in dico['1'].items():
    tab.append(v)
for k1,v2 in dico['0'].items(): 
    tab2.append(v2)
dico3={}
for i in range(len(tab)):
    dico3[tab[i]]=tab2[i]
############ Nuage de mots
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# génère le nuage de mots à partir des fréquences des mots
wc = WordCloud(background_color="lightcoral",width=1600, height=900).generate_from_frequencies(dico3)

plt.figure(figsize=(35,35))
plt.subplot(1,2,1)
plt.axis("off")
plt.imshow(wc)

