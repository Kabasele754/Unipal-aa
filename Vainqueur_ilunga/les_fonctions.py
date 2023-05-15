# -*- coding: utf-8 -*-
"""
Created on Thu May  4 01:41:25 2023

@author: FIM VAINQUEUR

"""
# une fonction qui permet de calculer des fonction mathematique
# nous allons ecrire une fonction  f(x)= 2x + 3
f= lambda x: 2 * x + 3
print(f"la valeur de la fonction est :{f(5)}") # l'utilisation de la fonction
# declaration d'une fonction sans argument
def somme():
    nbr1=5
    nre2=5
    print(nbr1+nre2)
    
#apple de la fonction ou utilisation de la fonctio
somme()

def produit():
    nbr1=5
    nre2=5
    return nbr1*nre2

# appel de la fonction
prod = produit()
print(prod)
# ou encore 
print(produit())
# la suite c'
# une fonction avec argument
# nous allons ecrire une fonction qui calcul la valeur de deltat 
# la formule de deltat est : deltat = b*b - 4ac
def deltats (a, b, c):
    deltat= b**2 - 4*a*c
    return deltat
# pour appeler une fonction avec l'instruction 
print(deltats(5, 5, 3))
# ou en core 
resultat= deltats(3, 6, 3)
print(f"la valeur de deltat est de :{resultat}")

# nous pouvons deja affecter une valeur a un argument de la fonction
# une fonction qui qui dit bonjour nom tu as age ans 
def salutation(nom, age=15):
    print(f"bonjour {nom} tu as {age} ans")
    
#appel de la fonction
print(salutation("franck"))# avec ça franck prendra l'age par defaut
# ou encore
print(salutation("fim", 25))
#ou encore
print(salutation(nom="ilunga", age=45))


#print() qui permet d'afficher le message à l'ecran que nous utilison deja
