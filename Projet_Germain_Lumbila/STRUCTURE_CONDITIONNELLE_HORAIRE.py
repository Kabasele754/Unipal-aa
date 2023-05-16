# programme qui affiche l'horaire de cours de quelques jours
N= int(input("entrer un chiffre entre 1 à 6, correspondant au jour de la semaine que vous cherchez"))
if N==2:
    print("Ce mardi vous aurez le cours d'intelligence artificiel avec Master Achille, de 08h00-12h00")
elif N==4:
    print("Ce jeudi vous aurez le cours d'intelligence artificiel avec Master Achille, de 08h00-12h00")
elif N==5:
    print("Ce vendredi vous aurez le cours d'intelligence artificiel avec Master Achille, de 08h00-12h00")
elif N== 6:
    print("Ce samedi vous aurez le cours de programmation resaux avec Ir Daniel, de 12hOO-17h30")
elif N==1 or N==3:
    print("L'horaire ne prevoit rien pour vous. Veillez contacter votre Cp pour plus d'information")
else:
    print("Le jour selectionné ne figure pas sur votre horaire")