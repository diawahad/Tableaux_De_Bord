# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:26:28 2018

@author: samba
"""
import matplotlib.pyplot as plt
import json
import pandas as pd
import numpy as np
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
from nltk.corpus import stopwords
stop_words=stopwords.words('french')


# lecture du fichier
with open('C:/Users/samba/Desktop/info sid/M2/projet_tab_bord/wade_scrapy/wade_scrapy/spiders/articles.json', 'r',encoding='utf8') as file:
        data = json.load(file)

# nettoyage sur des données
def sentense2cleanTokens(sent):
    sent = sent.lower()
    sent = "".join([x if x.isalpha() else " " for x in sent])
    sent = " ".join(sent.split())
    return sent

# Pretraitement de l'introduction des articles
data2={}
for i in range(len(data)):
    data2[i]=[sentense2cleanTokens(x) for x in data[i]["intro"]]
    data2[i]=[" ".join(data2[i])]

# enlever les stops words et remplace les contenus vides par Nan
from nltk.corpus import stopwords
stop_words=stopwords.words('french')
list_phrase=[]
for i in range(len(data2)):
    if data2[i]==[]:
        list_phrase.append('Nan')
    else:
        list_phrase.append(data2[i][0])

# Prediction de la polarite de chaque article 
def polarity(list_phrase,data):
    polarite=[]
    for i in range(len(list_phrase)):
        if list_phrase[i]=='':
            polarite.append('vide')
        else:
            text = list_phrase[i]
            blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
            if (blob.sentiment[0] < 0.15 and blob.sentiment[0] > -0.15):
                polarite.append(['neutre',data[i]['date']])
            elif (blob.sentiment[0] > 0.15):
                polarite.append(['positif',data[i]['date']])
            else:
                polarite.append(['negatif',data[i]['date'],list_phrase[i]])
    return(polarite)

polarite=polarity(list_phrase,data)

# listes des articles negatifs
hist_neg=[]
for i in range(len(polarite)):
    if polarite[i][0]=='negatif':
        hist_neg.append(polarite[i][1][0][6:8])
neg_content=[]
for i in range(len(polarite)):
    if polarite[i][0]=='negatif':
       neg_content.append(polarite[i][2])
neg_content[0]
neg_content1=[]
for i in range(len(neg_content)):
    select=[]
    for mot in neg_content[i].split():
        if (mot not in stop_words and len(mot)>4):
            select.append(mot)
    neg_content1.append(select)
tab={}
for i in range(len(neg_content1)):
    count=0
    for x in neg_content1[i]:
        tab[x]=count+1
mat={}
for x in sorted(set(tab.keys())):
    mat[x]=0
    for i in range(len(neg_content1)):
        for v in neg_content1[i]:
            if x==v:
                mat[x]=mat[x]+1
mat
dict = {}
dict["0"] =mat
# on le stock dans un fichier json nommé lien2759.json
with open('C:/Users/samba/Desktop/info sid/M2/projet_tab_bord/neg_cloud.json', "w") as f_write:
    json.dump(dict, f_write)
sorted(mat.items(), key=lambda t: t[1],reverse=True)[:20]             
    
     
        
# listes des articles positifs
hist_pos=[]    
for i in range(len(polarite)):
    if polarite[i][0]=='positif' and polarite[i][1]!=[] :
        hist_pos.append(polarite[i][1][0][6:8])
               
# Histogrammes des articles nigatifs
hist2_neg=np.zeros((len(set(hist_neg))) ,dtype=np.int)
columns=set(hist_neg)
for  position, valeur in enumerate(sorted(columns)):
    for j in range(len(hist_neg)):
        if hist_neg[j]==valeur:
            hist2_neg[position] = hist2_neg[position] +1
            
# Histogrammes des articles positifs
hist2_pos=np.zeros((len(set(hist_pos))) ,dtype=np.int)
columns2=set(hist_pos)
for  position, valeur in enumerate(sorted(columns2)):
    for j in range(len(hist_pos)):
        if hist_pos[j]==valeur:
            hist2_pos[position] = hist2_pos[position] +1
            

c=0
for i in range(len(polarite)):
    if polarite[i][0]=='positif':
        c+=1
#liste des nombres d'articles selon leurpolarite        
liste_polarite=[143,872,1744] 

x1=[1,2,3]           
plt.bar(x1,liste_polarite)           
plt.title("La répartition des articles selon la polarité") 
plt.xticks(x1, ('Negatif', 'Positif', 'Neutre'))

         
x=['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
plt.subplot(212)
plt.plot(sorted(x),hist2_pos)
plt.plot(sorted(x),hist2_neg,'r')
plt.title("L'évolution de la polarité des articles")
plt.xlabel("Année")
plt.ylabel("Nombre d'article")
plt.show()


mat=pd.DataFrame(hist2_neg)
mat[1]=hist2_pos
mat[2]=x
# fichier csv des polarités  
mat.to_csv('C:/Users/samba/Desktop/info sid/M2/projet_tab_bord/polarite.csv')

# lire le fichier contenant les mots clés
with open('C:/Users/samba/Desktop/info sid/M2/projet_tab_bord/first_key_words3.json', 'r',encoding='utf8') as file:
        words = json.load(file)

# permet d'avoir les effectifs pour chaque mots clés   
def effectif(words):
    key1=[]
    key2=[]
    for k,v in words.items():
        if v !=[]:
            key1.append(v[0][0])
            if len(v)==2:
                key2.append(v[1][0])
    dist_word=set(key1+key2)
    tab=sorted(dist_word)
    eff_word=np.zeros((len(sorted(dist_word))) ,dtype=np.int)
    for position, valeur in enumerate(sorted(dist_word)):
        for k,v in words.items():
            if v !=[] and v[0][0]==valeur:
                eff_word[position] = eff_word[position] + v[0][1]
            if len(v) == 2 and v != [] and v[1][0] == valeur:
                eff_word[position] = eff_word[position] + v[1][1]
    return eff_word, tab

eff_word,tab= effectif(words)
eff_word_pd=pd.DataFrame(eff_word)
eff_word_pd[1]=tab
eff_word=eff_word_pd.sort_values(0, ascending=False)
# creer un fichier csv
eff_word.to_csv('C:/Users/samba/Desktop/info sid/M2/projet_tab_bord/key_words_ef.csv',index=False)
 