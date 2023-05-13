import numpy as np
#un tableau à une dimension
a= np.array([1,2,3])
print(a) #Afficher le tzbleau
# verifier la dimension
print(a.ndim)
# voir sa forme
print(a.shape)
print(a.size)# donne la taille du tableau 

# initialiser le projet avec les zeros
# les arguments doivent etre dans un tuple,
#le premier argument c'est le nombre de ligne
# le deuxieme argument l=c'est le nombre de colonne
b= np.zeros((5,3))
print(b)

#initialiser le tableau qu'avec les 1
c = np.ones((3,2)) 
print(c)

# remplir le table avec une valeur donner
# un tableau a deux dimension qui n'affichera que 5
print(np.full((2,3), 5))

# initialiser le tableau avec les nombres aléatoire
print(np.random.randn(3,5))
