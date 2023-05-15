
# Panda : une bibliothèque incontournable pour le traitement de données en Python


L’une des forces de Panda est qu’il se base sur la très populaire bibliothèque NumPy. Elle fournit diverses structures de données et opérations pour le traitement de données numériques et de séries chronologiques. En plus de cela, les données produites par Panda sont souvent utilisées comme données en entrée pour les fonctions de plotting de Matplotlib, l’analyse statistique en SciPy, les algorithmes de machine learning en Scikit-learn. Les data scientists l’utilisent pour le chargement, le traitement et l’analyse des données tabulaires (données stockées sous format .csv, .tsv ou .xlsx) à l’aide de requêtes de type SQL.


## Pourquoi utiliser Panda Python ?

Maintenant que le mystère est levé sur ce que c’est que Pandas et son importance dans le domaine de la data, nous détaillerons dans cette partie les principaux points forts de cet outil.

Ce qui fait la force de Panda est qu’elle :

fournit une structure de donnée appelée Dataframe rapide et efficace pour la manipulation des données avec indexation intégrée ;
dispose d’outils pour lire et écrire dans des fichiers de différents formats (.csv, .txt, .xlsx, .sql, .hdf5, etc…) ;
offre une flexibilité pour traiter les données de type hétérogènes ou manquantes ;
est open source ;

fournit une documentation très détaillée et facile à lire ;
est utilisée dans une grande variété de domaines universitaires et commerciaux, notamment la finance, les neurosciences, l’économie, les statistiques, la publicité, l’analyse Web.

## Démarrez avec Panda Python

Dans cette partie de l’article nous allons vous montrer comment installer pandas et nous étudierons les différentes structures qu’il propose.

Pour une meilleure maîtrise de la bibliothèque, vous devez avoir une connaissance de base sur le langage de programmation python. Nous avons un article qui traite particulièrement de ce sujet.

## Installation de Pandas

La façon la plus simple d’installer non seulement Panda, mais aussi Python et ses packages les plus populaires (IPython, NumPy, Matplotlib, ...) est avec Anaconda, une distribution Python multiplateforme (Linux, macOS, Windows) pour l’analyse de données et le calcul scientifique.

Après avoir exécuté le programme d’installation, vous aurez accès à Pandas et au reste de l’écosystème SciPy sans avoir besoin d’installer un autre logiciel, ce qui rend l’outil pratique. Les instructions d’installation pour Anaconda sont disponibles ici.

Nous utiliserons dans la suite de cet article l’outil Jupyter Notebook pour écrire nos codes. Il est intégré directement dans Anaconda.

Après l’installation de Pandas et pour commencer à l’utiliser, vous devez l’importer dans votre script comme suit :

```import pandas as pd ```


Ici, pd est considéré comme un alias de Pandas. Cependant, il n’est pas nécessaire d’importer la bibliothèque en utilisant un alias, cela permet simplement d’écrire moins de code à chaque fois qu’une méthode ou une propriété est appelée.

Alors démarrons sans plus tarder à étudier les structures de données proposées par Pandas pour la manipulation et l’analyse de données.

## Les principales structures de données de Python Panda

Pandas fournit généralement deux structures de données pour manipuler les données, ce sont : les Series et les Dataframe.

## Les series

Une série est un tableau étiqueté unidimensionnel pouvant contenir tout type de données (entiers, chaînes de caractères, nombres à virgule flottante, objets Python, etc.). Les étiquettes des axes représentent l’index de la série. Pour être plus simple, une série n’est rien d’autre qu’une colonne dans une feuille Excel. La méthode de base pour créer une série est la suivante :

``` ser = pd.Series(data,  index=index) ```

data peut être un dictionnaire Python, un ndarray (tableau multi-dimensionnel de NumPy) ou même une valeur scalaire.

L’index passé en argument est une liste d’étiquettes correspondant à chaque ligne de la série.