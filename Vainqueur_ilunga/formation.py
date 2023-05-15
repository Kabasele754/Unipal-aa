# -*- coding: utf-8 -*-
"""
Created on Fri May  5 10:59:55 2023

@author: FIM VAINQUEUR
"""

nbr1= 10
nbr2= 2
print(nbr1**2)
# les operateurs de comparaison
# < , <= , ==,>, >= , !=
print(nbr1 < nbr2)
print(nbr1 <= nbr2)
# les operateurs logique
# et = and, ou = or , non = not
#avec le and la resultat est vrai lorsque les deux conditions sont vrai
# avec le or le resultat est vrai lorsque l'une de condition est vrai
print(not nbr1 > nbr2)

# les structures de données sequencielle
# les tuples et les listes, les string
# les tuples
# l'indexing, les slecing ,
#quelques methodes ou operrations a appliquer sur les listes
tuples_nom=("franck", "fim", "vainqueur", 36, 45, 45.3, 25.9 )
print(tuples_nom)
# indecing
print(tuples_nom[3])# afficher un element du tuple appartir de son indice
#print(tuples_nom[10])
# la methode len()
nombre_element= len(tuples_nom)
print(nombre_element)
print("le dernier element",tuples_nom[6])
# ou encore 
print(tuples_nom[-7])
jour_semaine= ("lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi","dimanche")
#slecing
# afficher les jours ouvrable de la semaine anglaise
print(jour_semaine[0:5])
print(jour_semaine[:5])
print(jour_semaine[-7:])
# afficher les le jour weekend
tuple_nombre= (0,1,2,3,4,5,6,7,8,9,10)
# afficher que les nombres pair
print(tuple_nombre[2::3])
prenom="vainqueur"
# notion de boucle sur les structures de donnée sequebncielle
# for
for jour in jour_semaine:
    print(jour)
    
for i in tuple_nombre[2::2]:
    print(i)
 # les if sur les structures de données sequencielle
 
if 15 in tuple_nombre:
     print("je suis la!")
else:
    print("je suis pas là!")

if not "lundi" in jour_semaine:
    print("je  ne suis pas là!")
else: 
    print("je suis là!")    

# les methodes sur les liste
liste_telephone= ["techno","itel", "iphone", "lenovo", "enes", "vivo"]
# indecing
print(liste_telephone[2])
# slecing
print(liste_telephone[0:4])
# boucle
for i in liste_telephone:
    print(i)
    
if "Techno".lower() in liste_telephone:
    print("tu m'as trouvé")
else:
    print("tu m'as pas trouvé")
# nombre d'elemn
print(len(liste_telephone))
# remplacer un element de la liste par un autre
liste_telephone[3]="oppo"
print(liste_telephone)
# ajouter  dand une liste nous allons utilisez la methode append()
liste_telephone.append("etel")
print(liste_telephone)
# la methode insert permet d'ajouter un element à un indice precis
liste_telephone.insert(4, "inphinix")
print(liste_telephone)

liste_telephone.reverse()
print(liste_telephone)
def check_password():
    mot = "1234"
    while  mot != True:
        mot_=input("entrer le mot de passe: ")
        if mot == mot_:
            print("bienvenue!")
        break








