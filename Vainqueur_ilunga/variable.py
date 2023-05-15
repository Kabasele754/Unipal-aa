# la declaration de variable en python, python est dynamiquement typé 
#il n'est pas necessaire de determiner le type de valeur a chaque declaration
Nbr1=12 # est une valeur du type entier (int)
Nbre2= 12.5 # est une variable du type float pour le reel
Nom = "Ilunga" # variable du type Str
led = True # variable du type boolean
#une autre forme de declaration de trois variables differentes de deux type de donn�e !=
Nbr_1, Nbr_2, nom= 12, 15.2, "Vainqueur" 
#une fonction qui permet d'afficher un message ou la valeur d'une variable � l'ecran

#======================================================================================================
# la fonction print() est une fonction qui peux prendre plusieur arguments de tous les types de donn�e
#======================================================================================================
print(Nbr_1, Nbr_2, nom) 
#les variables ou les messsage peuvent etre separ� soit par ;
# une virgule (,)
# le symbole d'addition (+), 
#l'utilisation de (+) entre les Str appel� concatenation
postnom = "Mutambayi"
salutation = "Hey"
print(salutation + " " + postnom)
# l'utilisation de (+) entre un Str et un int et un float
age= 18
# nous allons utiliser la fonction Str qui permet de convertir(caster) une variable du type int ou float en Str
# nous utilisons le sasting car il est impossible de d'additionner un int a un Str
print(salutation + " " + postnom + " "+str(age) + " "+ "ans") 
# NB: si vous n'ajouter pas d'espace entre les variables les variables seront coll�es l'une apres l'autre
print(salutation + postnom +str(age)) 

# utilisation de la virgule est simple a utiliser
print(salutation, postnom, str(age)) 

# la conversion de type de variable 
# str(), int(), float(), la fonction Str() est deja utilis�
x_string="123" # la variable x contient 123 et non cent vingt trois
y_string= "14.5" 
# pour calculer la somme de deux variable il faut le convertir en un type calculable soit int ou float
# convertisons en float
x_float=float(x_string)
y_float=float(y_string)
somme_float= x_float+y_float
print(somme_float)
#convertisons en int
x_int=int(x_string)
y_int=int(y_float)
somme_int= x_int+y_int
print(somme_int)
# le formatage de texte dans la fonction print, nous allons utiliser la fonction format 
print(f"{salutation} {nom} ! tu as {age} ans")
# les operateurs arthmetique et logique, operateur de comparaison
# les operateurs arthmetiques, addition(+), multiplication(*), puissance(**), division entiere (//), division decimale(/)
nbre1=10
nbre2= 5
somme= nbre1+nbre2
produit= nbre1*nbre2
dif= nbre1-nbre2
div_int= nbre1//nbre2
div_float=nbre1/nbre2 
puissance= nbre1**nbre2
print(somme)
print(produit)
print(dif)
print(div_float)
print(div_int)
print(puissance)
# les operateurs logiques en python: et=and; ou=or, non = not
# ces operateurs serons mieux detaill� lors de la structure conditionnelle
# structure de comparaison : <=, <, >=, >, ==
print(nbre1<=nbre2) # nous aurons un resultat du type boolean
print(nbre1<nbre2)
print(nbre1>=nbre2)
print(nbre1>nbre2)
print(nbre1==nbre2)
#NB: a ne pas confondre entre l'affectation(=) et la comparaison (==)
# la fonction input, elle permet de recuperer la valeur saisie par l'utilisateur 
# NB: toute valeur qui viens de la fonction input est du type Str, pour recuperer une valeur du type int ou float nous devont utiliser la fonction int ou float
nom_ville=input("Entrer votre villle: ")
num_parcelle=int(input("Entrer le numero de la parcelle: "))# premier fa�on
num_telephon=input("Entrer votre numero de telephone: ")
print(type(num_telephon))#la fonction type permet de savoir le type de la valeur
num_telephon=int(num_telephon)
print(type(num_telephon))
PI=float(input("entrer de pi: "))



