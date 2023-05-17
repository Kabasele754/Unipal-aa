####Algorithme de recherche dichotomique
def recherche_dichotomique(x, tableau):
	debut = 0
	fin = len(tableau) - 1
	mil = 0

	while debut <= fin:

		mil = (fin + debut) // 2

		# On ignore la première partie du tableau
        # Si x est plus grand que l'élément au milieu du tableau
		if tableau[mil] < x:
			debut = mil + 1

		# On ignore la seconde partie du tableau
        # Si x est plus petit que l'élément au milieu du tableau
		elif tableau[mil] > x:
			fin = mil - 1

		# Valeur x trouvée dans le tableau à la position mil
		else:
			return mil

	# Si on est ici, c'est que x ne se trouve pas dans le tableau
	return -1


tableau = [ 1, 1, 2, 3, 5, 8, 13, 21, 34 ]
x = 21

result = recherche_dichotomique(x, tableau)

if result != -1:
	print("x est présent à la position ", str(result))
else:
	print("x ne se trouve pas dans le tableau")
