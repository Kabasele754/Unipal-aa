# -*- coding: utf-8 -*-
"""
Created on Wed May  3 13:12:46 2023

@author: FIM VAINQUEUR
"""
# =================
# la boucle while
#==================
# la boucle while fait la condition et la repetion en meme temps, donc tant que la condition est répetée le bloc d'instruction va se repeté

a = 0 # on initialiser la variable à 0
while a < 10: # la condition a respecter
    print("salut les genies") # le programme va afficher 10 fois le message
    print(a) # le programme affichera 10 variable de 0 a n-1,
    #0 est la variable initialisée et n=10 donc le programme affichera de 0 à 9 parce que la condition est strictement inferieur
    a +=1 # on fais l'incrementation sans laquelle la boucle va tournée sans arret, 

# la boucle precedente, la variable à été initialisée à 0, on peux l'initialiser a une autre valeur
# l'incrementation a ete faite a pas de 1, nous pouvons changée le nombre de pas 

x=5
while x >= 18:
    print(x)
    x +=3
# le programme va afficher premierement 5 
# et par apprés afficher les nombres qui sont  entre 5 et 18 en faisant un pas de 5

"""
Constituez une liste semaine contenant les 7 jours de la semaine.
Écrivez une série d’instructions affichant les jours de la semaine 
(en utilisant une boucle for), ainsi qu’une autre
série d’instructions affichant les jours du week-end (en utilisant une boucle while).
"""
# la boucle for
jours_semaine=["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
for jour in jours_semaine:
    print(jour)

# les jours week-end avec la boucle while
jour= 5
total= len(jours_semaine)# cette methode nous a permi de connaitre le nombre d'element de la liste
while jour < total:
    print(f"les jours du week-end avec la boucle while: {jours_semaine[jour]}")
    jour +=1

mot = "1234"
while  mot != True:
    mot_=input("entrer le mot de passe: ")
    if mot == mot_:
        print("bienvenue!")
    