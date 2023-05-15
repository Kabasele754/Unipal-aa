# -*- coding: utf-8 -*-
"""
Created on Wed May  3 13:11:58 2023

@author: FIM VAINQUEUR
"""
for i in range(10):# il va affiche 10 valeur int en debutant par 0
    print(i)

# on peux ecrire un programme qui affiche le nombre qui sont entre 0 à 20
for i in range(2,20,2):
    print(f"valeure paire {i}")
    
liste_mois=[
    "Janvier",
    "Fevrier",
    "Mars",
    "Avril",
    "Mai",
    "Juin",
    "Juillet",
    "Aout",
    "Septembre",
    "Octobre",
    "Novembre",
    "Decembre"

]

#parcourir un tableau a l'aide de la boucle for

for mois in liste_mois:
    print(mois)

# afficher l'element de la liste et son index a l'aide de la boucle
for index,  mois in enumerate(liste_mois):
    print(index, mois)
# nous allons ecrire une table de multiplication
# nous pouvons imbriquer les conditions
for i in range(1,13): # une table de multiplication qui va jusqu'a 12
    for j in range(1,11):# de 1 à 10
        print(f"{j} x {i} = {j*i}")
         
    
