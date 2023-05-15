# -*- coding: utf-8 -*-
"""
Created on Wed May  3 13:01:58 2023

@author: FIM VAINQUEUR
"""
# une liste qui contient les string
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
print(liste_mois)
 # une liste des int
listt_nombre_jours=[31,28,31,30,31,30,31,31,30,31,30,31]
print(listt_nombre_jours)
# une liste qui contient deux listes
liste_mois_jours=[liste_mois, listt_nombre_jours]
print(liste_mois_jours)
# une liste vide
nom=[]
#indexing
# nous pouvons afficher seul mois selon son indice
print(f" le 7eme mois {liste_mois[-6]}")
print(f" le 7eme mois {liste_mois[6]}")
# Notion de slecing
# afficher les 6 premiers mois 
print(liste_mois[:-6])
# ou encore
print(liste_mois[0:6])
# la notion de pas avec le slecing
# afficher les mois 
print(liste_mois[1::2])# on va affiche a toute la liste a partir de l'indice 1 à 2 pas
#pour afficher la liste de mois a partir de decembre
print(liste_mois[::-1])
# afficher de decembre a juin
print(liste_mois[:4:-1])
#Modifier une valeur d'une liste
liste_article=["savon","sardine","savon", "bougie", "flash", "ordinateur"]
print(liste_article)
#pour modifier l'article flash et mettre le disque dur
#l'article flash est a l'indice 4
liste_article[4]= "hard disk"
print(liste_article)
# les operations qui peuvent etre appliquer sur le list "les methodes"
# la methode Append: permet d'ajouter un element a la fin de la liste ou à la derniere indice
liste_article.append("Switch")
print(liste_article)
# pour ajouter un element à l'indice precis la methode insert est faite pour ça
liste_article.insert(2, "Routeur")
print(liste_article)
# pour ajouter une liste à la fin d'une autre liste on utilise la methode extend()
liste_mois.extend(listt_nombre_jours)
print(liste_mois)
# connaitre la taille d'une liste ou le nombre d'element dans une liste on utilise len()

print(len(liste_mois))

# pour trier une liste selon l'ordre alphabetique croissant ou decroissant la  sort
liste_ville=["likasi","lubumbashi","kinshasa","goma","boma"]
liste_ville.sort() # liste croissant
print(liste_ville)
liste_ville.sort(reverse=True)
print(liste_ville)# liste decroissante
liste_int=[2,3,5,45,69,52,36,17,25]
liste_int.sort()
print(liste_int) # liste croissant
liste_int.sort(reverse=True)
print(liste_int) # liste decroissant
# la methode qui permet de compter le nombre de fois qu'un element est repris dans une liste
listes_ville=["likasi","lubumbashi","kinshasa","goma","boma","likasi"]
print(listes_ville.count("likasi"))
# une methode qui permet d'effacer tous les elements de la liste clear()
new_liste=[1,5,6,8,]
print(new_liste)
new_liste.clear()
print(new_liste)
#◘ il est possible de copier une liste dans une autre liste
liste_pays_afrique=["RDC", "congo-brazza", "rwanda","algerie","burundi"]
liste_pays=liste_pays_afrique.copy()
print(liste_pays_afrique)
print(liste_pays)
# pour suprimer le dernier element de la liste
liste_sup=[5,4,3,2,1]
sup=liste_sup.pop()
print(liste_sup) # affiche le reste des elements
print(sup)# affiche l'element suprimer
# pour suprimer un element specifique de la liste il suffit de passer son indice comme argument de pop()
sup_indice=liste_sup.pop(2)
print(sup_indice) # la valeur suprimer grace a son indice
# la methode del fait la meme chose
liste_del=[3,5,6,4,]
del(liste_del[0])# suprission l'element a l'indice indiquer
print(liste_del)
# la methode remove suprime un seul element d'une liste 
liste_article=["savon","sardine","savon", "bougie", "flash", "ordinateur"]
print(liste_article)
liste_article.remove("savon")# l'element savon est repris deux fois mais remove n'a suprimer qu'une seule fois savon

print(liste_article)


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
# la methode reverse(), qui permet d'inverser l'ordre d'une liste
liste_mois.reverse()
print(liste_mois)

#parcourir un tableau a l'aide de la boucle for

for mois in liste_mois:
    print(mois)

# afficher l'element de la liste et son index a l'aide de la boucle
for index, mois  in enumerate(liste_mois):
    print(index, mois)
    
# les structures conditionnelles sur une liste
if "janvier" in liste_mois:
    print("je suis là!")
else:
    print("je ne suis pas là!")


"""
Soient les listes suivantes :
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
Écrivez un petit programme qui crée une nouvelle liste t3. Celle-ci devra contenir tous les éléments des deux listes
en les alternant, de telle manière que chaque nom de mois soit suivi du nombre de jours correspondant :
"""

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

# nous allons utiliser la boucle for et la methode zip()
for mois, jour in zip(t2, t1):
    print(mois, jour)


# le slicing sur une liste imbriquée
liste_cote= [20,25,36]
liste_nom = ["franck","bea", "tegra"]
print
















