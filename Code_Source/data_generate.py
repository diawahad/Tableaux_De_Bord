# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 11:14:46 2018

@author: serigneabdoulahad
"""

from pandas import *
from numpy import *
import json
import os
import nltk
from nltk.corpus import stopwords
from collections import defaultdict
os.chdir('D:/CMI_SID/M1_SID/Tableau_de_bord/Bureau_Etude/Tableaux_De_Bord')

#%%
stop_words=stopwords.words('french')
with open('Donnees/articles.json', 'r',encoding="utf8") as file:
        data = json.load(file)
list_phrase=[]
for i in range(len(data)):
    for phrase in data[i]["intro"]:
        list_phrase.append(phrase)
#print(len(mot_cles))
tab={}

for i in range(len(list_phrase)):
    select=[]
    for mot in list_phrase[i].split():
        if (mot not in stop_words and len(mot)>3):
            select.append(mot)
    tab[i]=select
#print(tab)

#%%
print(data[6]['date'])
#%%
print((len(list_phrase)))
#%%
# Algorithm for classification
def algorithm_classification(don):
    mot_cles=[]
    dict=set()
    for i in range(len(don)):
        for tex in (don[i]["content"]):
            for mot in tex.split():
                if (mot not in stop_words and len(mot)>3):
                    mot_cles.append(mot)
    sel = max(set(mot_cles), key=mot_cles.count)
    dict.add(sel)
    return dict
print(algorithm_classification(data))