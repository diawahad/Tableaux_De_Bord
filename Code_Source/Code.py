# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:38:34 2018

@author: Etudiant
"""

######################################################################################

from nltk.tag import StanfordPOSTagger
jar = 'C:/Users/Etudiant/Documents/Tableau de bord/stanford-postagger-full-2018-02-27/stanford-postagger-3.9.1.jar'
model = 'C:/Users/Etudiant/Documents/Tableau de bord/stanford-postagger-full-2018-02-27/models/french.tagger'
import os
java_path = "C:/Program Files/Java/jdk1.8.0_151/bin/java.exe"
os.environ['JAVAHOME'] = java_path
pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')
words={}
tab2 = {}
for i in range(5):
   select=[]
   n=pos_tagger.tag(tab[i])
   stops_verb=['NC','N','NPP']
   for x in n:
       if x[1] in stops_verb:
           select.append(x[0])
           #sel = max(set(select), key=select.count)
   #tab2[i]=sel
   words={}
   for word in set(select):
       
       count = 0  
       for j in range(len(select)):
           if word == select[j]:
               count += 1
       words[word]= count
   tab2[i] = (sorted( words.items(), key = lambda x : -x[1]))[:2]
   
# Ce code permet de créer un dictionnaire(tab2) qui contiendra deux mots pour chaque 
#articles 

#################################   1    ############################
years = ['07','08','09','10','11','12','13','14','15','16','17','18']
nb_articles_an = {}
for year in years:
   nb_articles_no_date = 0
   nb_articles_with_date = 0    
   for i in range (len(data)):
       if data[i]['date']==[]:
           nb_articles_no_date += 1
       elif data[i]['date'][0].split()[0][6:8] == year:
           nb_articles_with_date += 1
   nb_articles_an[year] = nb_articles_with_date
   
plt.bar(list(nb_articles_an.keys()), nb_articles_an.values(), color='g')
plt.show()
   
# Ce code donne le nombre d'articles par année ainsi que l'histogramme associé 
#   à cette évolution
   
   
##############################     2    ##############################################

list_word = []
for i in range(len(tab)):
    for j in range(len(tab[i])):
        list_word.append(tab[i][j])

words = {} 
tab3 = {} 
i = 0      
for word in set(list_word):
    count = 0
    for j in range(len(list_word)):
        if word == list_word[j]:
            count += 1
        words[word]= count
    tab3 = sorted( words.items(), key = lambda x : -x[1])

# Ce code donne la fréquence des mots par ordre décroissante.


def file_trend(data):
    """ data preprocessing for groupe 9
    param : data -> json data
    return json with trend, period and most important word"""
    dict = {}
    for cle, valeur in data.items():
        if(cle != 'period'):
            for val in range(1, len(valeur)):
                word, trend = test_trend(data, cle, val)
            dict[cle] = trend
        else:
            dict[cle] = valeur
    return(dict)

