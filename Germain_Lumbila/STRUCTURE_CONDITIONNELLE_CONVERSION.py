# programme qui fait la conversion entre les dollars et les francs congolais
devise=input("devise : ")
montant=int(input("montant : "))
#1 dollar=2025 fc
Facteur_dollar_franc=2025
if devise=='Dollar':
    print("%f fc"%(montant*Facteur_dollar_franc))
elif devise=='fc':
    print("%f Dollar"%(montant/Facteur_dollar_franc))
else:
    print("cette devise n'est pas prise en charge")# afficher un message d'erreur