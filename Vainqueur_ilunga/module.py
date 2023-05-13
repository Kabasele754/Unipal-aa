# -*- coding: utf-8 -*-
"""
Created on Mon May  8 12:51:05 2023

@author: FIM VAINQUEUR
"""
import math
import random
import statistics
import os  
import glob
# le module math permet d'avoir accés aux differentes fonctions de math
# si nous voulon afficher la valeur de pi par exemple
# module math
print(math.pi)
print(math.cos(60)) # savoir le cosinus de 60
print(math.cos(math.pi)) # avoir le cosinus de pi
# le module statistiques
# ecrire un programme qui calcul la moyenne de cote des etudiants enregistrés dans une liste
liste_cote=[50,63,50,45,25,36]
print(statistics.mean(liste_cote))# il va additionné toutes les valeur et le divise par 6 qui est le nombre d'element

# le module random
# nous allons declarer une liste ou un tuple et afficher un element aleatoirement
tuples_nom=("fim", "franck", "ilunga", "vainqueur")
print(random.choice(tuples_nom))# il va affiché un nom aléatoirement
print(random.choice(liste_cote))# il affichera une cote aléatoirement
from datetime import datetime
print(datetime.now())