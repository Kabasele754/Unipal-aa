  # Notion sur le structure conditionnelee 
nom=input("veuillez entrer votre nom: ") #donne à l'utilisateur la possibilité d'entrer les caractère
postnom=input("veuillez entrer votre postnom: ")
prénom=input("veuillez entrer votre prénom: ")
age=int(input("quelle est votre age: "))
if age<10: #stucture conditionelle
    print(f"bonjour {nom} {postnom} {prénom} tu es bébé")
elif age<=18 and age>10:
    print(f"bonjour {nom} {postnom} {prénom} vous êtes Mineur")    
elif age>=18 and age<50:
    print(f"bonjour {nom} {postnom} {prénom} vous êtes jeune majeur")
elif age>=50 and age<100:
    print(f"bonjour {nom} {postnom} {prénom} vous êtes Vieux majeur")
else:
    print(f"bonjour {nom} {postnom} {prénom} vous êtes un veuillard")
tuple_nb=(0,1,2,3,4,5,6,7,8,9,10)
tuple_jr_sem=("lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche")
if 7 in tuple_nb:
    print("je suis là") 
else:
     print("je ne suis pas là")
if not"lundi"  in tuple_jr_sem:
    print("je ne suis pas là") 
else:
     print ("je suis là")

liste_tele=["techno","itel","Iphone","vivo","samsung","infinix"]
if "Techno".lower() in liste_tele:#la methode lower permet de convertir le majiscule en minuscule
    print("je suis là") 
else:
     print("je ne suis pas là")

