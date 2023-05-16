#!/usr/bin/env python
# coding: utf-8

# PROGRAMME AIRTEL MONEY D'ENVOI D'ARGENT AVEC LES STRUCTURES CONDITIONNELLEES

# In[2]:


code=input("entrez le code client: ")
if (code=='*501#'):
    a=int(input("choisissez votre devise:\n1.USD\n2.CDF \n3.Bureau de Change \n4.1GB 48h-100u \n5.Achat Unites/Forfait \n6.Balance \n 100u a 20350 FC. Des unites et forfaits au meilleur prix \n "))
    if (a==1 or a==2):
        b=int(input("choisissez: \n1.Envoi Argent\n2.Retrait d'argent \n3.Paiement \n4.Achat Forfaits \n5.Achat Unites \n6.Mon compte \n7.Services Financiers \n8.Surprise Bonus \n9.Aides  \n#Retour \n "))
        if b== 1:
            c=int(input("\n1.Entrer numero/Surnom \n2.Numeros favoris \n3.Annuler la transaction \n#Retour \n"))
            if c==1:
                d=int(input("\n Entrer numero/Surnom \n#Retour \n"))
                e=int(input("\n Entrer montant en CDF \n#Retour \n"))
                Pin=int(input("Entrer votre PIN pour confirmer que vous voulez envoyer CDF"))
                if Pin==2029:
                    print("Vous avez envoyé ", e , "CDF à ", d)
                else:
                    print("code incorrect")


# In[ ]:




