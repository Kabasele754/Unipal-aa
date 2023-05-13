# -*- coding: utf-8 -*-
"""
Created on Wed May  3 13:10:24 2023

@author: FIM VAINQUEUR
"""

#un tuple est une structure de donnée sequencielle qui dit sequencielle dit ordonner selon un ordre donné
# declaration d'un tuple
nom_semaine=("lundi","mardi","mercredi","jeudi","vendredi","samedi","dimache")
print(type(nom_semaine)) #determine le type de donnee
print(nom_semaine)
# l'indecing, on va affiher chaque element de la liste a travers son indice 
#NB: la plus petite indice c'est 0
print(nom_semaine[0]) #nous pouvons changer les indice selon la taille du tuple
# pour afficher le dernier element du tuple on peux faire
print(nom_semaine[-1]) # si tu ne connais pas la taille du tuple
print(nom_semaine[6]) # on aura le meme resultat 
#print(nom_semaine[7]) cette instruction ne passera pas car le tuple a 7 elements donc l'indice commence de 0 à 6
# pour connaitre la taille ou le nombre d'element d'un tuple nous allons utiliser la fonction len()
print(len(nom_semaine))
# on peux stocker cette taille dans une variable 
nombre_element=len(nom_semaine)
#nous pouvons parcourir dans un tiple a l'aide de la boucle For
for nom_jour in nom_semaine:
    print(nom_jour)
    break
# nous pouvons addition deux tuple donc mettre deux tuples dans un seul
val_pos=(1,2,3,4,5,6,7,8,9)
print(f"les valeures positives sont: {val_pos}")
val_neg=(-1,-2,-3,-4,-5,-6,-7,-8,-9)
print(f"les valeures negatives sont: {val_neg}")
valeur= val_pos + val_neg
print(f"les deux valeures mises ensemble: {valeur}")
# nous pouvons multiplier un tuple 
val_Str=("Franck", "vainqueur")
mutl_str= val_Str*2
print(f"les strins multiplier {mutl_str}")
# chercher une valeur dans un tuple
print(2 in val_pos) # la reponse sera du type boolean

# comparer deux tuples
print(val_neg != val_pos) # la reponse sera du type boolean

# un tuple dont les valeur sont les int ou les float il y'a possibilité de connaitre la plus grande valeur et la plus petite valeur
print(max(val_pos)) # la plus grande valeur
print(min(val_neg)) # la plus petite valeur

# notion de Slising
# dans le tuple val_pos nous allons afficher que les nombres pair
print(val_pos[1::2]) # l'affichage va commencer a partir de la valeur a l'indice 1 jusqu'a la fin du tuple mais il va se deplacer à 2 pas
print(val_pos[1:5:2])
# dans le tuple nom_semaine nous allons afficher les jours du travail selon la semaine anglaise
nom_semaine=("lundi","mardi","mercredi","jeudi","vendredi","samedi","dimache")
print("les jours ouvrable de la semaine anglaise", nom_semaine[0:5]) # python va affiche la valeur qui est à l'indice 0 = lundi jusqu'a l'element qui est à l'indice 4 = vendredi , l'indice 5 est exclu
# ou encore
print("les jours ouvrable de la semaine anglaise", nom_semaine[:-2])
# pour affichier les jours du week end donc samedi et dimanche
print("le week end", nom_semaine[5:])
print("le week end", nom_semaine[5:7])
print("le week end", nom_semaine[-2:])
# nous pouvons savoir les nombre de fois qu'un element reviens dans un tuple
article=("sardine","bougie", "sardine", "savon", "sardine", "savon")
nombre_repete=article.count("sardine")
print(nombre_repete)

# convertir un tuple en une liste et vise versa
nom_semaine=("lundi","mardi","mercredi","jeudi","vendredi","samedi","dimache")
print(type(nom_semaine)) # est un tuple
liste_semaine= list(nom_semaine) # convertir en une liste
print(liste_semaine)
print(type(liste_semaine))

    