# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:41:34 2023

@author: FIM VAINQUEUR
"""

password= "1234"
while not  password :
    print("mot depasse errné")
    password_enter= input("entrer un mot de passe")
    if password == password_enter:
        print("bienvenue!")
    break
    