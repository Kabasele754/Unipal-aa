#!/usr/bin/env python
# coding: utf-8

# UTILISATION DE SLICING DANS LE TABLEAU NUMPY

# In[7]:


import numpy as np
#On on peut utiliser les slices pour sélectionner une partie du tableau 
#Exemples
c = np.array([23, 5, 12,45,76]) 
c[0:2] # de 0 inclu à 2 exclu


# In[9]:


c[1:]# semlectionner les elements du tableau, de l'indice 1 jusqu'a la fin 


# In[10]:


c[:-1]


# In[16]:


# pour decouper le tableau. EX avec indexing
c= np.array([[3,4,5],[5,6,7],[8,9,1],[4,2,3]]) 
c


# In[17]:


e=c[:]# CA PREND TOUT
e


# In[18]:


d=c[2,2] #POUR RECUPER 1
d


# In[19]:


d=c[3,2]# pour recuperer 3
d


# In[21]:


# Pour recuperer seulement la premiere colonne
e=c[0,:]
e


# In[22]:


#ou encore
e=c[0:1]
e


# In[24]:


#POUR INITIALISER LE TABLEAU
c=np.zeros((4,4))
c


# In[25]:


d=c[1:3,1:3]# recuperer les elements  du milieu
d


# In[26]:


d=c[1:3,1:3]=1# les remplacer par 1
d
c


# In[30]:


# CODE EN BLOC pour remplacer le 0 de chaque coin du tableau par 1
f=c[0,:1]=1
g=c[0,3:]=1
b=c[3,:1]=1
j=c[3,3:]=1
c


# In[28]:


#POUR RECUPERER LES 2 dernieres lignes et colonnes du tableau
h=c[0:,2:]
h


# In[29]:


#ou 
h=c[:,2:]
h


# In[32]:


#Pour afficher les 4 dernieres valeurs du coin du tableau
j=c[2:,2:]
j


# In[ ]:




