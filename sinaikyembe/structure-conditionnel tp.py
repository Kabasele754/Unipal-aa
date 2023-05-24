#Exercice 1.1 Notes et mention d’un étudiant
#Voici les notes d’un étudiant : 14, 9, 13, 15 et 12. Créez un script qui affiche la note maximum (utilisez la
#fonction max()), la note minimum (utilisez la fonction min()) et qui calcule la moyenne.
#Affichez la valeur de la moyenne avec deux décimales. Affichez aussi la mention obtenue sachant que la mention
#est « passable » si la moyenne est entre 10 inclus et 12 exclus, « assez bien » entre 12 inclus et 14 exclus et «
#bien » au-delà de 14 

cote_etud=(14,16,13,17,12)
maxm=max(cote_etud)
print(f"la cote maximale est: {maxm}")
mini=min(cote_etud)
print(f"la cote minimale est: {mini}")
som=sum(cote_etud)

sommEl= len(cote_etud)
moy=som/sommEl
print(f"la moyenne est de : {moy}")
if moy == 10 and moy < 12:
    print(f"la moyenne est de :{moy} et à pour mension passable!")
elif moy >= 12 and moy < 14:
    print(f"la moyenne est de :{moy} et à pour mension assez bien!")
elif moy >= 14:
     print(f"la moyenne est de :{moy} et à pour mension bien!")