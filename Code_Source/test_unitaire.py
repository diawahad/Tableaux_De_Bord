# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 10:34:41 2018

@author: samba
"""
from nltk.corpus import stopwords
stop_words=stopwords.words('french')
from nltk.tag import StanfordPOSTagger
import os


def sentense2cleanTokens(sent):
    sent = sent.lower()
    sent = "".join([x if x.isalpha() else " " for x in sent])
    sent = " ".join(sent.split())
    return sent

def rp_vide(data2):
    list_phrase = []
    for i in range(len(data2)):
        if data2[str(i)] == ['']:
            list_phrase.append('Nan')
        else:
            list_phrase.append(data2[str(i)][0])
    return list_phrase

def stop_word(list_phrase):
    tab={}
    for i in range(len(list_phrase)):
        if list_phrase[i]=='Nan':
            tab[i]=['Nan']
        else:
            select=[]
            for mot in list_phrase[i].split():
                if (mot not in stop_words and len(mot)>3):
                    select.append(mot)
            tab[i]=select
    return tab

jar = 'C:/Users/samba/Desktop/info sid/M2/projet_tab_bord/stanford-postagger-full-2018-02-27/stanford-postagger-3.9.1.jar'
model = 'C:/Users/samba/Desktop/info sid/M2/projet_tab_bord/stanford-postagger-full-2018-02-27/models/french.tagger'
java_path = "C:/Program Files/Java/jdk-9.0.1/bin/java.exe"
os.environ['JAVAHOME'] = java_path
pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')
def key_word(tab):
    words = {}
    tab2 = {}
    for i in range(len(tab)):
       select = []
       # predit les endités nommées
       pos = pos_tagger.tag(tab[i])
       stops_verb = ['NC', 'N', 'NPP']
       # on recupere les mots ayant comme entités nommées Nom Commun,Nom ou Nom Propre
       for x in pos:
           if x[1] in stops_verb:
               select.append(x[0])
       words = {}
       for word in set(select):
           # on compte la frequence du mot dans l'intoduction de l'article
           count = 0  
           for j in range(len(select)):
               if word == select[j]:
                   count += 1
           words[word]= count
           # on ordonne et on recupere les 2 mots ayant les plus frequents dqns l'introduction de l'article
       tab2[i] = (sorted( words.items(), key = lambda x : -x[1]))[:2]
    return(tab2)
key_word({0: ['Nan'], 1: ['voiture', 'panne']})

#test unitaire
def test_sentense2cleanTokens():
    text = 'le voiture %% est en panne/00'
    return sentense2cleanTokens(text) == 'le voiture est en panne'

def test_rp_vide():
    data={'0':[''],'1':['le voiturer est en panne']}
    return rp_vide(data) == ['Nan', 'le voiture est en panne']   

def test_stop_word():
    list_phrase=['Nan', 'le voiturer est en panne']
    return stop_word(list_phrase) == {0: ['Nan'], 1: ['voiture', 'panne']} 
    
def test_key_word():
    data={0: ['Nan'], 1: ['voiture', 'panne']}
    return key_word(data) == {0: [('Nan', 1)], 1: [('panne', 1), ('voiture', 1)]}

# Print les resultats des test unitaires:

if test_sentense2cleanTokens()== True:
    print('test unitaire sentense2clean Valide')
if test_rp_vide()== True:
    print('test unitaire test_rp_vide Valide')
if test_stop_word()== True:
    print('test unitaire test_stop_word Valide')
if test_key_word()== True:
    print('test unitaire test_key_word Valide')
