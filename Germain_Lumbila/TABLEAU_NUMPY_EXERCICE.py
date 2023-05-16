#!/usr/bin/env python
# coding: utf-8

# MODULE NUMPY

# In[1]:


# Dès que l’installation est finie, on peut importer les modules. Pour cela, on utilise les instructions:import numpy as np
# Après avoir importé numpy, on peut commencer à créer nos premiers tableaux. Pour cela, il suffit d’utiliser l’instruction np.array, qui prend en paramètre la liste des nombres qui seront contenus dans le tableau.
# Par exemple si on veut initialiser un tableau avec les valeurs 23, 5, 12,45 et 76:
import numpy as np 
tableau = np.array([23, 5, 12,45,76]) 
tableau
#Les différences majeures entre les listes proposées par Python et les tableaux de Numpy sont: 
# — dans un tableau, tous les éléments doivent être du même type;
# — il y a un gain élevé de performance avec les tableaux.


# In[2]:


# on peut parcourir le tableau avec une boucle for, comme pour une liste
tableau = np.array([23, 5, 12,45,76]) 
for i in tableau:
    print(i) 


# In[3]:


#On peut aussi accéder manuellement à un élément du tableau (comme avec les listes, on commence à compter à partir de 0) et connaitre le nombre d’objet contenu dans le tableau:
tableau = np.array([23, 5, 12,45,76])
tableau[0]


# In[4]:


tableau[2] # afficher la valeur à l'indice 2


# In[6]:


#Nous avons aussi la possibilité d’ajouter, de supprimer et d’insérer des éléments dans les tableaux.
tableau = np.array([23, 5, 12,45,76]) 
np.append(tableau, 2) # Ajoute l'élément 2 à la fin du tableau 


# In[8]:


np.delete(tableau, 1) # Supprime l'élément à l'index 1 (ici l'entier 5)


# In[9]:


np.insert(tableau, 3, 14) # Insère l'élément 14 à l'index 3 


# In[10]:


#Les formules mathématiques s’utilisent directement sur les tableaux, celles-ci seront alors appliquées à tous les éléments du tableau:
tableau = np.array([23,  5, 12, 14, 45, 76])
tableau ** 2  # Met au carré les elements du tableau


# In[11]:


#Numpy permet aussi de créer un tableau avec des données aléatoires, en utilisant la fonction np.random.rand
#exemple
a=np.random.randint(1,5, size=(4,4))
a


# In[12]:


# Il y a aussi la fonction np.random.randint(max, size=n) qui retourne un tableau avec n valeurs comprises entre 0 et max (exclu).
a=np.random.randint(8, size=6) # retourne 6 elements compris entre 0 et 8 
a


# In[13]:


np.zeros(5) # Genere un tableau avec que le chiffre 0 


# In[14]:


np.ones(5) # Un tableau de longueur 4 avec que le chiffre 1 


# In[15]:


#Rechercher dans un tableau
#La fonction np.where prend en paramètre une condition sur les valeurs d’un tableau et va retourner l’index des éléments qui vérifient la condition. 
#La fonction np.extract renvoie les éléments qui vérifient la condition.
tableau=np.arange(1, 25) # Tableau avec les nombres entiers de 1 à 24 2 
np.where(tableau % 5 == 0) # L'index des nombres divisibles par 5 


# In[16]:


np.extract(tableau % 5 == 0, tableau) # Les nombres divisibles par 5 


# In[17]:


np.ones(shape=5) # pour créer un tableau à une dimension, contenant 5 elements
