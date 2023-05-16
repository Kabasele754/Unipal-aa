#!/usr/bin/env python
# coding: utf-8

# 4.MODULE

# In[4]:


#Un module est grossièrement un bout de code que l'on a enfermé dans un fichier.Ils permettent de regrouper plusieurs fonctions selon le même principe. 
#Toutes les fonctions mathématiques, par exemple, peuvent être placées dans un module dédié aux mathématiques.
#exemple
import math
math.sqrt(16)# pour trouver la racine carrée de 16


# In[5]:


# ou encore:
import math as mathematiques
mathematiques.sqrt(25)


# In[6]:


from math import fabs
fabs(-33)# pour donner la valeur absolue d'un nombre


# In[7]:


from math import * #Vous pouvez appeler toutes les variables et fonctions d'un module en tapant * à la place du nom de la fonction à importer
from math import * 
sqrt(4) 


# In[8]:


fabs(-90)


# In[ ]:




