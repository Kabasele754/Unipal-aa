# -*- coding: utf-8 -*-
"""
Created on Thu May  4 01:17:38 2023

@author: FIM VAINQUEUR
"""

"""
Écrire un script qui pour une température T donnée affiche l’état de l’eau à cette
température c’est à dire "SOLIDE", "LIQUIDE" ou "GAZEUX". On prendra comme
conditions les suivantes :
si la température est strictement négative alors l’eau est à l’état solide,
si la température est entre 0 et 100 (compris) l’eau est à l’état liquide,
si la température est strictement supérieure à 100.
"""
T=input("entrer la temperature: ")
T=int(T)
if T < 0:
    print("l'eau est a l'etat solide")
elif T > 0 and T <= 100 :
    print("l'eau est a l'etat liquide")
elif T > 100:
    print("l'eau est a l'etat gazeuse " )
else:
    print("suis pas programmer pour donner l'etat de l'eau")# lorsque le user saisi 0