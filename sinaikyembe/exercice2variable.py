nom =input("Entrer votre nom ")
postnom=input("Entrer votre post-nom")
prenom=input("Entrer votre prenom ")
age=input("Entrer votre age ")
age =int(age)
print(f"bonjour {nom} {postnom} {prenom} vous avez {age} ans")
if age<18:
    print(f"bonjour {nom} {postnom} {prenom} vous avez {age} ans vous etes mineur")
elif age>=18 and age>50:
    print("bonjour {nom} {postnom} {prenom} vous avez {age} ans vous etes vieux")    
else :
    print(f"bonjour {nom} {postnom} {prenom} vous avez {age} ans vous etes majeur")