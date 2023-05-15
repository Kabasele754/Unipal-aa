
## Qu’est-ce que NumPy Python ?

NumPy (Numerical Python) est une bibliothèque de python qui comporte des fonctions permettant de manipuler des matrices ou tableaux multidimensionnels.

NumPy est la base de SciPy, qui n’est rien d’autre qu’un ensemble de bibliothèques Python pour des calculs scientifiques. Il est beaucoup plus adapté pour les problématiques qui requièrent l’usage des matrices ou des tableaux multidimensionnels, comme la Data Science, l’ingénierie, les mathématiques ou encore les simulations.

C’est en 2005 que NumPy fut créé par Travis Oliphant. C’est un logiciel open source et compte de nombreux contributeur. NumPy est un projet parrainé financièrement par NumFOCUS.

Pourquoi utiliser NumPy ?
Lors des calculs logiques et mathématiques sur des matrices et tableaux, c’est NumPy qui est très sollicité. Il permet d’effectuer rapidement et efficacement les opérations par rapport aux listes Python.

Les tableaux NumPy utilisent d’abord moins de mémoire et d’espace de stockage, ce qui le rend plus avantageux que les tableaux traditionnels de python.

En effet, un tableau NumPy est de petite taille et ne dépasse pas les 4MB. Mais une liste peut atteindre les 20MB. De plus, les tableaux NumPy sont faciles à manipuler.


Différence entre tableau NumPy et liste Python
Tout le long de cet article, nous allons voir des codes dans le langage Python, vu que NumPy est l’une de ses bibliothèques. Donc, il serait plus pratique que vous ayez les bases nécessaires afin de pouvoir tout suivre. Notre article sur la programmation Python vous aidera à acquérir cette base.

La question à se poser est : pourquoi ne pas utiliser les listes Python qui agissent comme de tableau au lieu d’utiliser les tableaux NumPy ? C’est la manière dont Python stocke un objet dans la mémoire qui répondra au mieux à cette question.

Un objet Python n’est rien d’autre qu’un pointeur, il pointe vers l’emplacement mémoire où vous pouvez trouver toutes les informations sur l’objet comme les octets et la valeur. 

Les listes Python sont des tableaux pointeur, qui pointent chacun vers un emplacement qui contient les détails relatifs à l’élément. Cela augmente la surcharge de mémoire et parfois, ces informations se répètent lorsque les objets stockés sont de même type.

C’est pour éviter ce problème qu’il faut utiliser les tableaux NumPy. Ceux-ci prennent des éléments homogènes (des éléments qui ont les mêmes types de données), ce qui facilite la manipulation du tableau. 

Cette différence est remarquable quand vous voulez traiter avec des tableaux ayant des milliers d’éléments. De plus, avec les tableaux NumPy, vous serez en mesure d’effectuer des opérations par éléments, ce qui est impossible avec les listes Python. 

Voilà la vraie raison pour laquelle les tableaux NumPy sont les plus utilisés par rapport aux listes, pendant les opérations d’une grande quantité de données.

Démarrer avec NumPy Python
Installation de NumPy
Si vous avez installé Anaconda, alors NumPy est déjà installé sur votre système. Mais dans le cas contraire, tapez cette ligne de commande dans votre terminal : 
``` pip install numpy   ```
``` import numpy as np ```