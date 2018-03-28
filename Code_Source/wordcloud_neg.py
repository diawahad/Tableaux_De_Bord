# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 21:25:52 2018

@author: samba
"""

import json

with open('C:/Users/sceli/Documents/ProjetTableauBord/neg_cloud.json', 'r',encoding='utf8') as file:
        data = json.load(file)


dico = {}

for x,v in data['0'].items():
    if x not in ['cette','chaque','celui','avoir','quels','leurs','comme','quelles']:
        dico[x] = v
    
    
############ Nuage de mots
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# génère le nuage de mots à partir des fréquences des mots
wc = WordCloud(background_color="white",width=1600, height=900).generate_from_frequencies(dico)

plt.figure(figsize=(35,35))
plt.subplot(1,2,1)
plt.axis("off")
plt.imshow(wc)

