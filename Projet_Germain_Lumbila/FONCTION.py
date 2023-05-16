#!/usr/bin/env python
# coding: utf-8

# 3.FONCTION

# In[1]:


#3.  FONCTION
#Les fonctions permettent de regrouper plusieurs instructions dans un bloc qui sera appelé grâce à un nom
#On crée une fonction selon le schéma suivant :def nom_de_la_fonction(parametre1 , parametre2 , parametre3 , parametreN):
                                    # Bloc d'instructions
#Exemple
#Le code pour mettre une table de multiplication dans une fonction serait donc :

n=int(input("entrez la valeur de n: "))
def table_multiplication():
   print(n) 
i=0
while i<10:
    print(i+1,"x",n," = ",(i+1)*n)
    i+=1

    


# In[ ]:




