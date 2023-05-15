def password_fuction():
    password="1234"
    #password_enter=input("Entrer un mot de passe: ")
    while password!=True :
        password_enter=input("Entrer un mot de passe: ")

        if password == password_enter:
            print("Bienvenue")
            break
password_fuction
def calcul_nbr(nbr1,nbr2):
    return nbr1*nbr2
produit= calcul_nbr(4,5)
print (produit)
