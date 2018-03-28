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

dico={}
pays = ['afghanistan',
'afrique du sud',
'albanie',
'algerie',
'allemagne',
'andorre',
'angleterre',
'angola',
'anguilla',
'antarctique',
'antigua',
'antilles', 
'arabie saoudite',
'argentine',
'armenie',
'aruba',
'australie',
'autriche',
'azerbaïdjan',
'bahamas',
'bahrain',
'bangladesh',
'belgique',
'belize',
'benin',
'bermudes',
'bhoutan',
'bielorussie',
'birmanie',
'bolivie',
'bosnie-herzegovine',
'botswana',
'bouvet',
'bresil',
'brunei',
'bulgarie',
'burkina faso',
'burundi',
'cambodge',
'cameroun',
'canada',
'cap vert',
'cayman',
'chili',
'chine',
'christmas',
'chypre',
'cocos',
'colombie',
'comores',
'congo',
'coree du nord',
'coree du sud',
'costa rica',
'cote d ivoire',
'croatie',
'cuba',
'danemark',
'djibouti',
'dominique',
'egypte',
'equateur',
'erythree',
'espagne',
'estonie',
'unis',
'ethiopie',
'falkland',
'feroe',
'fidji',
'finlande',
'france',
'gabon',
'gambie',
'georgie',
'ghana',
'gibraltar',
'grece',
'grenade',
'groenland',
'guadeloupe',
'guam',
'guatemala',
'guinee',
'guinee equatoriale',
'guinee-bissau',
'guyane',
'guyane française',
'haïti',
'honduras',
'hongrie',
'inde',
'indonesie',
'irak',
'iran',
'irlande',
'islande',
'israël',
'italie',
'jamaïque',
'japon',
'jordanie',
'kazakhstan',
'kenya',
'kirghizistan',
'kiribati',
'koweit',
'la barbad',
'laos',
'lesotho',
'lettonie',
'liban',
'liberia',
'libye',
'liechtenstein',
'lithuanie',
'luxembourg',
'macau',
'macedoine',
'madagascar',
'malaisie',
'malawi',
'maldives',
'mali',
'malte',
'mariannes du nord',
'maroc',
'marshall',
'martinique',
'maurice',
'mauritanie',
'mayotte',
'mexique',
'micronesie',
'moldavie',
'mongolie',
'montserrat',
'mozambique',
'myanmar',
'namibie',
'nauru',
'nepal',
'nicaragua',
'niger',
'nigeria',
'niue',
'norfolk',
'norvege',
'nouvelle caledonie',
'nouvelle-zelande',
'oman',
'ouganda',
'ouzbekistan',
'pakistan',
'palau',
'panama',
'papouasie-nouvelle-guinee',
'paraguay',
'pays-bas',
'perou',
'philippines',
'pitcairn',
'pologne',
'polynesie française',
'porto rico',
'portugal',
'qatar',
'republique centrafricaine',
'republique dominicaine',
'republique tcheque',
'reunion',
'roumanie',
'royaume-uni',
'russie',
'rwanda',
'sahara occidental',
'saint pierre et miquelon',
'saint vincent et les grenadine',
'saint-kitts et nevis',
'saint-marin',
'sainte helene',
'sainte lucie',
'samoa',
'senegal',
'seychelles',
'sierra leone',
'singapour',
'slovaquie',
'slovenie',
'somalie',
'soudan',
'sri lanka',
'suede',
'suisse',
'suriname',
'syrie',
'tadjikistan',
'taiwan',
'tanzanie',
'tchad',
'thailande',
'timor',
'togo',
'tokelau',
'tonga',
'trinite et tobago',
'tunisie',
'turkmenistan',
'turquie',
'tuvalu',
'ukraine',
'uruguay',
'vanuatu',
'vatican',
'venezuela',
'vietnam',
'yemen',
'yougoslavie',
'zaïre',
'zambie',
'zimbabwe']

for i in range(len(tab)): #on parcourt la liste de mots et on implémente le dictionnaire
    for j in range (len(tab[i])):
       if tab[i][j] in pays:
           if str(tab[i][j])=='unis': #cas particulier états unis
               if str('états-unis') in dico.keys():
                   dico[str('états-unis')] = dico[str('états-unis')] +1
               else:
                   dico['états-unis'] = 1
           else:
               
               if str(tab[i][j]) in dico.keys():
                   dico[str(tab[i][j])] = dico[str(tab[i][j])] +1
               else:
                   dico[str(tab[i][j])] = 1
         
            
############ Nuage de mots
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# génère le nuage de mots à partir des fréquences des mots
wc = WordCloud(background_color="white",width=1600, height=900).generate_from_frequencies(dico)

plt.figure(figsize=(35,35))
plt.subplot(1,2,1)
plt.axis("off")
plt.imshow(wc)

