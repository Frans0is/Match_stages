'''
Ce programme est sensible à l'ordre dans lequel sont rangés les stages
Cet ordre sera donc tiré au sort
'''


#### Bibliothèque #####

import random

#### Programme ########

# Exemples de listes de préférences des étudiants a, b, c et d : l'étudiant a (0) préfère le stage 0 quand l'étudiant b (1) préfère le stage 4
# En réalité ces listes seront extraites d'un document csv (tableur)

a = [1,2,3,4,5]
b = [2,5,3,4,1]
c = [1,4,3,2,5]
d = [1,3,2,4,5]

# Pour tester ce programme en conditions réelles, on génère 35 listes des 40 premiers entiers naturels (à partir de 1) ordonnées aléatoirement.

# I.  Constitution de la liste des préférences

# L : list[list[int]]
L = []

for x in range(35):
	
	l =[]
	
	while len(l) < 40:
		a = random.randint(1,40)
		if a not in l:
			l.append(a)
			
	L.append(l)

for x in L:
	print(x)	

# II. Initialisation des différentes listes utiles

# liste_comptage : list[list[int]] : la i-ème sous-liste rassemble les numéros des étudiants
# ayant attribué la préférence 1 au i-ème stage
liste_comptage = []

# stagesprov
stagesprov =[]
stagesatt =[]
etudprov =[]
etudatt=[]



# III. Attribution des stages

while len(etudatt) != len(L):

	#### III. 1. Tour d'attribution des stages ####

	# j : int ; indice du stage
	for j in range(40):				# ! correspond au nombre de stages, il doit être 
									# ! au moins égal au nombre d'étudiants 
	
		# on initialise la sous-liste du stage considéré
		liste_comptage.append([])
	
		# i : int ; indice de l'étudiant
		for i in range(len(L)):
			if L[i] != []:
				if L[i][j] == 1:
					liste_comptage[j].append(i)
			
	for x in range(len(liste_comptage)):
		if len(liste_comptage[x]) == 1:
			print('Le stage numéro', x, 'est attribué à l\'étudiant numéro', liste_comptage[x][0])
			stagesprov.append(x)
			etudprov.append(liste_comptage[x][0])
		
		elif len(liste_comptage[x]) > 1:
			chanceux = random.choice(liste_comptage[x])
			print('Le stage numéro', x, 'est attribué à l\'étudiant numéro', chanceux)
			stagesprov.append(x)
			etudprov.append(chanceux)
		

	#### III. 2. Actualisation de la liste des préférences ####


	# On vide les sous-listes des préférences des étudiants matchés
	for x in range(len(etudprov)):
		L[etudprov[x]] = []

	# On amène les préférences pour les stages matchés à 0
	# et on abaisse chaque préférence de 1
	for x in L:
		if x != []:
			for y in range(len(x)):
				if x[y] != 0:
					if y in stagesprov:
						x[y]=0
					else:
						x[y] -= 1

	
	#### III. 3. Stockage des informations et ménage ####
	
	
	for x in etudprov:
		etudatt.append(x)
	etudprov = []
	
	for x in stagesprov:
		stagesatt.append(x)
	stagesprov = []
	
	liste_comptage =[]
	

print(stagesatt)
print(etudatt)

# en imprimant bien j'aurais même les lettres 
