# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:26:28 2018

@author: sceli
"""

import json

with open('C:/Users/sceli/Documents/ProjetTableauBord/articles.json', 'r',encoding='utf8') as file:
        data = json.load(file)

############################ nettoyage sur l'intro
def sentense2cleanTokens(sent):
    sent = sent.lower()
    sent = "".join([x if x.isalpha() else " " for x in sent])
    sent = " ".join(sent.split())
    return sent
data2={}
data3={}
data4={}
for i in range(len(data)):
    data2[i]=[sentense2cleanTokens(x) for x in data[i]["intro"]] #intros
    data2[i]=[" ".join(data2[i])]
    data3[i]=[sentense2cleanTokens(x) for x in data[i]["title"]] #titres
    data3[i]=[" ".join(data3[i])]
    data4[i] = data2[i]+data3[i]


############################# enleve les stops words et remplace les contenus vides par Nan
from nltk.corpus import stopwords
stop_words=stopwords.words('french')
list_phrase=[]
list_phrase2=[]
for i in range(len(data4)):
    for j in range (len(data4[i])):
        if data4[i][j]==[]:
            list_phrase.append('Nan')
        else:
            list_phrase.append(data4[i][j])

tab={} 
for i in range(len(list_phrase)):
    if list_phrase[i]=='Nan':
        tab[i]=['Nan']
    else:
        select=[]
        for mot in list_phrase[i].split():
            if (mot not in stop_words and len(mot)>2):
                select.append(mot)
        tab[i]=select
# dans tab on a pour chaque article l'intro et le titre splités par mot et les mots vides enlevés

############ Compte effectifs noms d'enseignes de e-commerce

dico_effectifs={}
enseignes = ['accorhotels', 'airfrance', 'airbnb', 'alloresto', 'amazon', 'asos', 'blablacar', 'booking', 'carrefour', 'casino', 'cdiscount', 'chronoresto' , 'conforama', 'darty', 'deliveroo', 'easyjet', 'ebay', 'etam', 'expedia', 'fnac', 'foodchéri', 'foodora', 'glamour', 'groupon', 'occitane', 'redoute', 'lafourchette', 'lastminute', 'leclerc', 'lafayette', 'oreal', 'louis vuitton', 'lvmh', 'mcdonald', 'monoprix', 'nestlé', 'oogarden', 'ouiscnf', 'popchef', 'priceminister', 'restoin', 'sarenza', 'showroomprivé', 'sodexo', 'spartoo', 'takeeateasy', 'ubereats', 'venteprivée', 'voyageprivé', 'voyagessncf', 'wholefood', 'zalando', 'marionnaud', 'nocibé', 'sephora', 'agatha', 'cleo', 'maty','birchbox','aquarelle', 'bebloom', 'florajet', 'interflora', 'aubade', 'darjeeling','frichti',
'aramis','oscaro','allopneus','mister auto', 'pixmania', 'rueducommerce','photobox', 'brandalley', 'ticketnet', 'materiel', 'fotolia', 'bazarchic', 'meninvest', 'delamaison','placedestendances','madeindesign','planetveo','florajet','boulanger','auchan', 'but', 'celio']



for i in range(len(tab)): #on parcourt la liste de mots et on implémente le dictionnaire
    for j in range (len(tab[i])):
       if tab[i][j] in enseignes:
           if str(tab[i][j]) in dico_effectifs.keys():
               dico_effectifs[str(tab[i][j])] = dico_effectifs[str(tab[i][j])] +1
           else:
               dico_effectifs[str(tab[i][j])] = 1

############ Nuage de mots
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib

# génère le nuage de mots à partir des fréquences des mots

wc = WordCloud(background_color="white",width=1600, height=900, colormap=matplotlib.cm.inferno).generate_from_frequencies(dico_effectifs)
#

plt.figure(figsize=(35,35))
plt.subplot(1,2,1)
plt.axis("off")
plt.imshow(wc)

