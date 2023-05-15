list_identité=["beya","ilunga",12]
print(list_identité) #afficher les valeurs du tableau
print(list_identité[0])#afficher la valeur à l'indice 0
list_identité[0]="elgra"#modifier la valeur d'une indice
#le dictionnaire
dic_ville={"hk":["l'shi","kasile", "likasi"]}
print(dic_ville.values())
print(dic_ville.keys())
#structure des données séquentiels: les types de données sont ordonnée par ordre d'indice
#les tuples:ne peuvent pas être modifier.
tuple_nom=("elgra","dygra","elgra",23,16,18.3,16.4)
print(tuple_nom)
#indexing,
"""print(tuple_nom[3])#permet d'afficher un élément du tuple à travers son indice
print(tuple_nom[7])"""
#la methode len:permet de connaitre les nombres d'éléments se trouvant dans une structure de donnée séq
nb_element=len(tuple_nom)
print(nb_element)
print("le dernier élément du tuple est:",tuple_nom[6])#pour afficher le derier élément
print(tuple_nom[-1])
# slecing : permet de selectionner une partie d'éllément dans une structure de donnée seq
tuple_jr_sem=("lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche")
#afficher les jours ouvrables de la semaine anglaise
print(tuple_jr_sem[0:5])
print(tuple_jr_sem[:5])
print(tuple_jr_sem[-7:-2])
print(tuple_jr_sem[5:])
tuple_nb=(0,1,2,3,4,5,6,7,8,9,10)
#pour afficher les nombres pairs
print(tuple_nb[2::2])#:2 pour le nombre de pas
#quelques methodes ou opérations utilisé dans les structure des données séquentielles
#les strings:
prenom="elgra"
print(prenom[0:2])
#notion sur les boucles
#for
for i in tuple_jr_sem:
    print(i)
for i in tuple_nb[2::2]:
    print(i)
    # Notion sur le structure conditionnelee dans les structures de données séquentielle
if 7 in tuple_nb:
    print("je suis là") 
else:
     print("je ne suis pas là")
if not"lundi"  in tuple_jr_sem:
    print("je ne suis pas là") 
else:
     print ("je suis là")
#les listes:peuvent être modifier.
liste_tele=["techno","itel","Iphone","vivo","samsung","infinix"]
if "Techno".lower() in liste_tele:#la methode lower permet de convertir le majiscule en minuscule
    print("je suis là") 
else:
     print("je ne suis pas là")
print(len(liste_tele))
#remplacer un élément de la liste
liste_tele[3]="lenovo"
print(liste_tele)
#ajouter un élément dans une liste: la methode APPEND 
liste_tele.append("hp")
print(liste_tele)
#la metode INSERT permet d'ajouter un élément à unemplacement bien précis
liste_tele.insert(4,"oppo")
print(liste_tele)
#pour renverser les élément de la liste on iutilise la methode reverse
liste_tele.reverse()
print(liste_tele)