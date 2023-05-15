#les fonctions sans parametre ou argument et qui ne renvoie rien.
def salutation():
    print("salut")
salutation()

def produit():
    nbre1=8
    nbre2=5
    print(nbre1*nbre2)
produit()


def affiche_jour_semaine():
    jour_semaine=[
    "lundi"
    "mardi"
    "mercredit"
    "jeudi"
    "vendredi"
    "samedi"
    "dimanche" ]
        
    for jour in jour_semaine:
        print(jour)
affiche_jour_semaine()
# les fonctions avec argument et qui renvoie un resultat

def test_age(age=0, nom="sinai"):
    if age < 18:
        print(f"{nom} tu es mineur")
    else:
        print(f"{nom} tu es majeur")
test_age(age=23,nom="ianis")
test_age()


# les fonctions qui retourne une valeur

def somme(a,b):
    somme= a+b
    return somme
# on peux l'afficher directement dans print
calcul=somme(23, 32)

print(calcul)
print(somme(3, 7))
