### importation du module numpy
import numpy as np
tableau = np.array([1, 2, 4])
for i in tableau:
    print(i)
    #### creation du tableau
scalaire_1 = np. array(5)
scalaire_2 = np. array(6)
Resultat = scalaire_1 + scalaire_2
# Créer un tableau numpy 2-D: np.array([[]])
identité_2 = np.array([[1,0],[0,1]])
print(type(identité_2))
print(identité_2)
## creation du Tableau numpy 3-D :
three_dim = np.array([ [[1,2],[3,4]] , [[4,5],[5,6]] ])
print(three_dim)
print(three_dim.ndim)
# Créer la matrice identité : np.eye(nb)
identité_2_np = np.eye(2 , dtype = int)
print(type(identité_2_np))
print(identité_2_np)
# Créer la matrice nulle : np.zeros((nb lignes, nb colonnes))
zeros_2_np = np.zeros((2,2), dtype = int)
print(type(zeros_2_np))
print(zeros_2_np)
##Créer des tableaux 1-D
# 1ére solution : np.linspace(start, end, nb_elements), le end est pris en compte ici
# 2éme solution : np.arange(start, end, pas), le end est exclu ici
A = np.linspace(5,15,9)
B = np.arange(5,16.25,1.25)
print(A)
print(B)
# Créer des tableaux 2-D à partir de linspace ou arange
# On utilise la fonction reshape
#
A = np.linspace(5,15,9)
B = np.arange(5,17.5,1.25)
print("taille A : ", A.shape)
print("taille B : ", B.shape)
new_A = A.reshape((5,2))
new_B = B.reshape((2,5))
print("new_A taille: ",new_A.shape)
print("new_B taille: ",new_B.shape)
# Addition, soustraction, multiplication
A = np.array([[1,2],[3,4]])
B = np.eye(2)
somme = A + B
diff = A - B
ele_par_ele = A * B #elles doivent avoir la même taille ! multiplication élément par élément
ele_par_ele_2 = np.multiply(A,B) #elles doivent avoir la même taille ! multiplication élément par é lément
produit = np.dot(A,B) # vrai produit de matrice
print(A)
print(B)
print("somme :", somme)
print("diff :", diff)
print("multiplication élément par élément :", ele_par_ele)
print("multiplication élément par élément 2 :", ele_par_ele_2)
print((ele_par_ele == ele_par_ele_2))
print("produit : ", produit)
#syntaxe : array.sum(A, axis = )
# si le tableau est 2-D alors axis = 0 (colonne) ou 1 (ligne)
A = np.array([[1,2,3],[4,5,6]])
somme = np.sum(A)
somme_ligne = np.sum(A, axis = 1)
somme_col = np.sum(A, 0)
print(A)
print("somme tous les élé de A : ", somme)
print("somme chaque ligne: ",somme_ligne)
print("somme chaque colonne: ",somme_col)
# syntaxe : array.mean(A, axis)
A = np.array([[1,2,3],[4,5,6]])
moy = np.mean(A)
moy_ligne = np.mean(A, axis = 1)
moy_col = np.mean(A, 0)
print(A)
print("moyenne tous les élé de A : ", moy)
print("moyenne chaque ligne: ",moy_ligne)
print("moyenne chaque colonne: ",moy_col)
# Simple boucle for
A = np.array([[1,2,3],[4,5,6]])
count_ele = 0
for i in A:
    count_ele += 1
print(count_ele)
print(i)

# On peut récupérer en même temps l'indice et l'élément avec
# la commande np.ndenumerate(A)
A = np.array([[1,2,3],[4,5,6]])
for indice, ele in np.ndenumerate(A):
    print(indice, ele)
print("matrice A : ")
print(A)
