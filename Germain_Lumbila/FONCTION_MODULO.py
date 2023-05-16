# Programme qui determine , avec la fonction modulo, si un nombre est pair ou impair
nbr=int(input("entrez un nombre: "))
modulo2=nbr%2
if modulo2==0:
    print("ce nombre est pair")
else:
    print("ce nombre est impair")