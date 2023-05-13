# -*- coding: utf-8 -*-
"""
Created on Wed May  3 13:11:24 2023

@author: FIM VAINQUEUR
"""

# la structure de deonnée sequecielle string
nom = "franck"
phrase= "j'apprend le python!"
# convertir une chaine en maj ou en miniscule
print(phrase.lower()) # afficher le string en minuscule
print(nom.upper())# affichera le maj 
# la taille du string
nom_caractere= len(nom)
print(nom_caractere)
# nous pouvons itéré sur le string
for caracter in nom:
    print(caracter.upper())# les caraceres serons afficher en maj
    

# nous pouvons chercher un caracter dans le string
if "o" in nom:
    print(" je suis là!")
else:
    print("je suis absent! ")

# nous pouvons compter le nombre d'occurence
print(phrase.count("i")) # nous pouvons chercher n'importe quel caractere dans le string
# nous pouvont chercher meme les nombres d'espaces dans un string
print(phrase.count(" "))

# l'indexing 
print(nom[5])
# le slecing
print(nom[3::2])
