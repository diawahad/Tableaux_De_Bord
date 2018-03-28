# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 23:33:14 2018

@author: serigneabdoulahad
"""

#Import de la librairie
import pypyodbc

#Connexion au serveur
connexion = pypyodbc.connect('Driver={SQL Server};'
'Server=DIAW\SEALAHSQL;'
'Database=MASTER;'
'uid=sa;pwd=Sealah12'
)
cursor = connexion.cursor()

#Exemple de requêtes
#Requête avec un seul résultat 
SQLQ = "SELECT count(*)  FROM [dbo].[Auteurs] "
cursor.execute(SQLQ)
row = cursor.fetchone()
print(row)
    
#%%
# les nuages de mots (titre intro et date)
#Requête avec plusieurs résultats
SQLQ = "SELECT titre,introduction,Date_Article  
        FROM [dbo].[Articles] order by Date_Article "
cursor.execute(SQLQ)

# Method 1, simple reading using cursor
titre_intro_date_articles=[]
while True:
    row = cursor.fetchone()
    if not row:
        break
    else:
        #print(row)
        titre_articles.append(row)
#Impression de toutes les langues de traductions de TED
#print(row)
#%%
# mots_cles freq et date
#%%
# les nuages de mots (titre intro et date)
#Requête avec plusieurs résultats
SQLQ1 = "
        SELECT Mots1,Mots2,frequence_Mot1,frequence_Mot2,Date_Article 
        FROM [dbo].[Mots_cles] M, [dbo].[Articles] A,[dbo].[Associer] Ass
             WHERE M.Id_mots_cles=Ass.Id_mots_cles 
             AND Ass.Id_articles=A.Id_articles "
cursor.execute(SQLQ1)

# Method 1, simple reading using cursor
mots_cles=[]
while True:
    row = cursor.fetchone()
    if not row:
        break
    else:
        #print(row)
        mots_cles.append(row)
#Impression de toutes les langues de traductions de TED
#print(row)
