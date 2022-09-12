# Match_stages

Le programme match est destiné à attribuer des lieux de stages à des étudiants, qui seront appelés joueurs, de manière optimisée.

Ce programme exige une connaissance exhaustive des préférences des joueurs. Chacun classe les lieux de stage selon ses préférences, de son préféré,
classé numéro 1, à celui qu'il aime le moins, ici classé numéro 40. Il y a plus de stages que de joueurs, tous les stages ne sont donc pas attribués.

Cet exigence d'exhaustivité peut sembler lourde, un joueur ne distinguant pas forcément quel est son préféré entre le 39e et le 40e stage.
Néanmoins la connaissance des préférences est la seule manière de limiter le recours au tirage au sort, ce que ce programme vise précisément.

Une liste des préférences de chaque joueur est fournie au programme sous forme d'un fichier txt formatée, nommé preferences.txt. 
Cette liste est lue par le programme, traitée,puis actualisée, et ainsi de suite jusqu'à attribution d'un stage à chaque joueur.

À chaque tour le programme se préoccupe uniquement des lieux de stages pour lesquels une préférence de valeur 1 à été attribuée.
Si un seul joueur a affecté une préférence 1 a un lieu, ce lieu lui est attribué.
Si plusieurs joueurs ont affecté une préférence 1 a un même lieu, un tirage au sort est organisé entre eux, et entre eux seulement.
Tous les lieux affectés d'une préférence 1 par au moins un joueur sont donc attribués et les joueurs ayant reçus un lieu de stage sortent du jeu.
Le jeu continue pour les autres : toutes leurs préférences concernant des lieux déjà attribuées sont amenées à 0, 
toutes leurs autres préférences non nulles sont abaissées de 1. Ainsi, un nouveau tour d'attribution peut avoir lieu, et ainsi de suite, jusqu'à
ce que chaque joueur se soit vu attribuer un lieu de stage.


Dans un esprit de transparence, le programme generate est aussi disponible. Il s'agit d'un autre programme python utilisé pour créer des listes aléatoires de préférences, de noms et prénoms ainsi que de ville, puis de créer un fichier preference.txt de démonstration. 
Cela a servi à tester le programme match, mais peut aussi servir à illustrer son fonctionnement, afin que chacun le comprennne en détail s'il le souhaite.
