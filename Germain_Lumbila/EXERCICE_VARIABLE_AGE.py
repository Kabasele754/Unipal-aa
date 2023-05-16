nom=(input("entrez votre nom"))
postnom=(input("entrez votre postnom"))
prenom=(input("entrez votre prenom"))
age=int(input("entrez votre age"))
if(age<=10 and age>0):
    print(f"bonjour{nom}{postnom}{prenom} vous avez {age} ans. Vous etes bébé")
elif (age<=17 and age >=10):
    print(f"bonjour {nom}{postnom}{prenpm} vous avez {age} ans. Vous etes mineur")
elif(age>=18 and age<50):
    print(f"Bonjour{nom}{postnom}{prenom} vous avez {age} ans. Vous etes majeur")
elif(age>=50 and age <=100):
    print(f"Bonjour{nom}{postnom}{prenom} vous avez {age} ans. Vous etes vieux")
else:
     print(f"Bonjour{nom}{postnom}{prenom} vous avez {age} ans. On ne vous reconnait pas")