# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:31:10 2023

@author: ianis
"""

class Personne:
    def __init__(self,c_nom,c_Age):
        self.nom=c_nom
        self.Age=c_Age
        
    def sePresenter(self):
        print(f"salut! {self.nom} tu as {self.Age} ans")
        
        
    def  Tester_Age(self):
        if self.Age>18:
            print(f" {self.nom} tu as {self.Age} ans et tu es majeur ")
        else:
            print(f" {self.nom} tu as {self.Age} ans et tu es mineur ")
            
p1=Personne("sinai", 28)
#print(f"bonjour {p1.nom} tu as { p1.Age} ans") 
p2=Personne("ianis",14)
p2.sePresenter()
p1.sePresenter() 
p1.Tester_Age()
p2.Tester_Age()