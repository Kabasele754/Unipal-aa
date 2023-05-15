a=1 #variable entier
b=3.5#variable reel
nom="cyril" #chaine de charactere
led=True # boolen
x,y=6,8
print(x)
print(y)
print(y**2) # 2 montre la puissance
nbr1=10
nbr2=2
cos1=nbr1/nbr2
cos2=nbr1//nbr2
print(cos1)
print(cos2)
# les operateurs de comparaison
# <=, >=, == ,> ,<,!=
print(nbr1<nbr2)
print(nbr1<=nbr2)
# les operateurs logique
# et=and, ou=or,non=not
# avec and le resultat est vrai losque le deux condition sont vrai
# avec or le resultat est vrai losque l'une de reponse est vrai 
# avec not le resultat est vrai lorsque la reponse est vrai
print("je suis not", not nbr1 > nbr2)
# les structures de données sequencielle
# les tuples et les listes , string ce sont le structure de données sequentielle
# les tuples ne sont pas modifiable
# les listes sont modifiable
# le indexing, les slecing
# quelques methodes ou operations a appliquer sur les listes
tuple_nom=("cyril","cyrio","hillaire",34,65.7,4,39)
print(tuple_nom) 
# indecing
print(tuple_nom[3])# afficher un element du tuple appartir de son indice
#print(tuple_nom[10])
# la methode len()# elle permet de connaitre les nobre d'element
nbr_element=len(tuple_nom)
print(nbr_element)
print("le dernier element",tuple_nom[6])
#ou encore
print(tuple_nom[-7])
jour_semaine=("lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche")
# slesing
#afficher les jours ouvrable de la semaine anglaise
print(jour_semaine[0:5])
print(jour_semaine[:5])
print(jour_semaine[-7:-2])