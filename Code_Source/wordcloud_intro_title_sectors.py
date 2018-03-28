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
# dans tab on a pour chaque article l'intro 
# et le titre splités par mot et les mots vides enlevés

############ Compte effectifs noms d'enseignes de e-commerce

dico_effectifs={}
dico_secteurs = {}
dico_secteurs_eff = {}
enseignes = ['accorhotels', 'airfrance', 'airbnb', 'alloresto', 'amazon', 'asos', 'blablacar', 'booking', 'carrefour', 'casino', 'cdiscount', 'chronoresto' , 'conforama', 'darty', 'deliveroo', 'easyjet', 'ebay', 'etam', 'expedia', 'fnac', 'foodchéri', 'foodora', 'glamour', 'groupon', 'occitane', 'redoute', 'lafourchette', 'lastminute', 'leclerc', 'lafayette', 'oreal', 'louis vuitton', 'lvmh', 'mcdonald', 'monoprix', 'nestlé', 'oogarden', 'ouiscnf', 'popchef', 'priceminister', 'restoin', 'sarenza', 'showroomprivé', 'sodexo', 'spartoo', 'takeeateasy', 'ubereats', 'venteprivée', 'voyageprivé', 'voyagessncf', 'wholefood', 'zalando', 'marionnaud', 'nocibé', 'sephora', 'agatha', 'cleo', 'maty','birchbox','aquarelle', 'bebloom', 'florajet', 'interflora', 'aubade', 'darjeeling','frichti',
'aramis','oscaro','allopneus','mister auto', 'pixmania', 'rueducommerce','photobox', 'brandalley', 'ticketnet', 'materiel', 'fotolia', 'bazarchic', 'meninvest', 'delamaison','placedestendances','madeindesign','planetveo','florajet','boulanger','auchan', 'but']

dico_secteurs = {'accorhotels':'voyage', 'airfrance':'voyage', 'airbnb':'voyage', 
                 'alloresto':'alimentaire', 'amazon':'général', 'asos':'mode/beauté', 
                 'blablacar':'voyage', 'booking':'voyage', 'carrefour':'général', 'casino':'général', 
                 'cdiscount':'général', 'chronoresto':'alimentaire' , 'conforama':'high-tech', 
                 'darty':'high-tech', 'deliveroo':'alimentaire', 'easyjet':'voyage', 'ebay':'général', 
                 'etam':'mode/beauté', 'expedia':'voyage', 'fnac':'high-tech', 'foodchéri':'alimentaire', 
                 'foodora':'alimentaire', 'glamour':'mode/beauté', 'groupon':'général', 'occitane':'mode/beauté', 
                 'redoute':'mode/beauté', 'lafourchette':'alimentaire', 'lastminute':'voyage', 'leclerc':'général', 
                 'lafayette':'mode/beauté', 'oreal':'mode/beauté' , 'louis vuitton':'mode/beauté', 'lvmh':'mode/beauté', 
                 'mcdonald':'alimentaire', 'monoprix':'général', 'nestlé':'alimentaire', 'oogarden':'autre', 'ouiscnf':'voyage', 
                 'popchef':'alimentaire', 'priceminister':'général', 'restoin':'alimentaire', 'sarenza':'mode/beauté', 
                 'showroomprivé':'mode/beauté', 'sodexo':'alimentaire', 'spartoo':'mode/beauté', 'takeeateasy':'alimentaire',
                 'ubereats':'alimentaire', 'venteprivée':'général', 'voyageprivé':'voyage', 'voyagessncf':'voyage', 'wholefood':'alimentaire', 
                 'zalando':'mode/beauté', 'marionnaud':'mode/beauté', 'nocibé':'mode/beauté', 'sephora':'mode/beauté', 'agatha':'mode/beauté',
                 'cleo':'mode/beauté', 'maty':'mode/beauté', 'birchbox':'mode/beauté','aquarelle':'mode/beauté', 'bebloom':'autre', 
                 'florajet':'autre', 'interflora':'autre', 'aubade':'mode/beauté', 'darjeeling':'mode/beauté','frichti':'alimentaire',
                 'aramis':'automobile','oscaro':'automobile','allopneus':'automobile','mister auto':'automobile', 
                 'pixmania':'high-tech', 'rueducommerce':'général','photobox':'high-tech', 'brandalley':'mode/beauté',
                 'ticketnet':'autre', 'materiel':'high-tech', 'fotolia':'high-tech', 'bazarchic':'mode/beauté', 'meninvest':'mode/beauté', 
                 'delamaison':'autre','placedestendances':'mode/beauté','madeindesign':'autre','planetveo':'voyage','florajet':'autre',
                 'boulanger':'high-tech','auchan':'général', 'but':'high-tech', 'celio':'mode/beauté'}



for i in range(len(tab)): #on parcourt la liste de mots et on implémente le dictionnaire
    for j in range (len(tab[i])):
       if tab[i][j] in enseignes:
           if str(tab[i][j]) in dico_effectifs.keys():
               dico_effectifs[str(tab[i][j])] = dico_effectifs[str(tab[i][j])] +1
           else:
               dico_effectifs[str(tab[i][j])] = 1


for i in dico_effectifs.keys(): #compte le nombre d'occurences d'enseignes citées par catégorie

   if str(dico_secteurs[i]) in dico_secteurs_eff.keys():
       dico_secteurs_eff[str(dico_secteurs[i])] = dico_secteurs_eff[str(dico_secteurs[i])] + dico_effectifs[i]
   else:
       dico_secteurs_eff[str(dico_secteurs[i])] = dico_effectifs[i]
       
       

############ Nuage de mots
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib


# génère le nuage de mots à partir des fréquences des mots
wc = WordCloud(background_color="white",width=1600, height=900, colormap=matplotlib.cm.inferno).generate_from_frequencies(dico_secteurs_eff)


plt.figure(figsize=(35,35))
plt.subplot(1,2,1)
plt.axis("off")
plt.imshow(wc)


############ Camembert 
# 7 catégories
# Fait sur excel en parallèle

labels = [x for x in dico_secteurs_eff.keys()] # récupère les clefs
sizes = [dico_secteurs_eff[i] for i in labels] # récupère les effectifs
colors = ['pink', 'orchid', 'lightyellow', 'lightcyan', 'lightcoral','gold', 'yellowgreen']

# Décaler le morceau le plus gourmand
highest = max(sizes)
explode = [0.1 if k == highest else 0 for k in sizes]

# Le camembert
plt.pie(sizes, labels=labels, colors=colors, explode=explode, labeldistance = 1.2,
        autopct='%1.1f%%', shadow=True, startangle=90)

# Le titre du camembert
plt.suptitle("Répartition des sites de e-commerce selon leur secteur d'activité")

# Les axes doivent être égaux pour un cambembert rond
plt.axis('equal')


plt.savefig('camembert_secteurs.png')
plt.show()

############


