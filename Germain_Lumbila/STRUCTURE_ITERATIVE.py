# programme qui fait la table de multiplication d'une valeur saisie par l'utilisateur
n=int (input("entrez la valeur de n: "))
print("voici la table de multiplication de",n)
for i in range(1,10):
  print(i, " x ",n," = " ,i*n)