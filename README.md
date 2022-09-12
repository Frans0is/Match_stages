# Match_stages

Le programme match est destiné à attribuer des lieux de stages à des étudiants, qui seront appelés joueurs, de manière optimisée.

Ce programme exige une connaissance exhaustive des préférences des joueurs. Chacun classe les lieux de stage selon ses préférences, de son préféré,
classé numéro 1, à celui qu'il aime le moins, ici classé numéro 40. Il y a plus de stages que de joueurs, tous les stages ne sont donc pas attribués.

Cet exigence d'exhaustivité peut sembler lourde, un joueur ne distinguant pas forcément quel est son préféré entre le 39e et le 40e stage.
Néanmoins la connaissance des préférences est la seule manière de limiter le recours au tirage au sort, ce que ce programme vise précisément.

Une liste des préférences de chaque joueur est fournie au programme sous forme d'un fichier txt formatée, nommé preferences.txt. 
Cette liste est lue par le programme, traitée, puis actualisée, et ainsi de suite jusqu'à attribution d'un stage à chaque joueur.

À chaque tour le programme se préoccupe uniquement des lieux de stages pour lesquels une préférence de valeur 1 à été attribuée.
Si un seul joueur a affecté une préférence 1 a un lieu, ce lieu lui est attribué.
Si plusieurs joueurs ont affecté une préférence 1 a un même lieu, un tirage au sort est organisé entre eux, et entre eux seulement.
Tous les lieux affectés d'une préférence 1 par au moins un joueur sont donc attribués et les joueurs ayant reçus un lieu de stage sortent du jeu.
Le jeu continue pour les autres : toutes leurs préférences concernant des lieux déjà attribuées sont amenées à 0, 
toutes leurs autres préférences non nulles sont abaissées de 1. Ainsi, un nouveau tour d'attribution peut avoir lieu, et ainsi de suite, jusqu'à
ce que chaque joueur se soit vu attribuer un lieu de stage.

Le principal avantage de cet algorithme est de maximiser le nombre de joueurs se voyant attribuer leur premier choix, et d'éviter les situations qualifiées de sous-optimales. Voilà un exemple.

On à la tableau des préférences qui suit.

|Institut|Monod|Pasteur|Curie|
|---|:---:|:---:|:---:|
| Alice  | 1  |  2 |  3 |
| Bob | 2  | 1  |  3 |
|  Carol |  1 |  2|  3 |


Un tirage au sort poduira six résultats possibles : ABC, ACB, BAC, BCA, CAB et CBA.
Dans 2 de ces 6 résultats (ACB et CAB), Bob fait son choix après Alice et Carol, et se voit donc attribuer le stage à Curie.
Si Alice chosit avant Carol alors, Alice à son premier choix, Carole son deuxième et Bob son troisième, tandis que si Carol choisit avant Alice, c'est Carol qui a son premier choix et Alice son deuxième. Dans ces deux cas, qui représentent 1/3 des possibilités, une seule personne obtient son premier choix.

Notre algorithme ne peut produire que deux résultats, en garantissant à Bob son premier choix puisqu'il est le seul à avoir classé le 
stage à l'institut Pasteur premier. La stage à l'insititut Monod échoit soit Alice soit à Carol, mais dans tous les cas, deux personnes obtiennent leur premier choix.



Dans un esprit de transparence, le programme generate est aussi disponible. Il s'agit d'un autre programme python utilisé pour créer des listes aléatoires de préférences, de noms et prénoms ainsi que de ville, puis de créer un fichier preference.txt de démonstration. 
Cela a servi à tester le programme match, mais peut aussi servir à illustrer son fonctionnement, afin que chacun le comprennne en détail s'il le souhaite.
