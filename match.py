#### Bibliothèque #####

import random

#### Programme ########

i = 0
NOMBRE_STAGES = 40

# 0. Lecture du tableau des préférences

# L : list[list[int]]
L = []
# iden : list[str]
iden = []
# villes : list[str]
villes = []


flux = open('preferences.txt','r')

for ligne in flux :
	
	if i == 0:
		elements = ligne.split()
		for x in elements:
			villes.append(x)
		i = 0.5
		
	else:
		if i == 0.5:
			i = 0
			
		L.append([])
		elements = ligne.split()
		
		iden.append(elements[0])
		
		for x in range(len(elements)-1):
			L[i].append(int(elements[x+1]))
			
		i += 1

flux.close()



# I. Initialisation des différentes listes utiles

# liste_comptage : list[list[int]] : la i-ème sous-liste rassemble les numéros des étudiants
# ayant attribué la préférence 1 au i-ème stage
liste_comptage = []

# stagesprov
stagesprov =[]
stagesatt =[]
etudprov =[]
etudatt=[]



# II. Attribution des stages

while len(etudatt) != len(L):

	#### II. 1. Tour d'attribution des stages ####

	# j : int ; indice du stage
	for j in range(NOMBRE_STAGES):				
		
		# on initialise la sous-liste du stage considéré
		liste_comptage.append([])
	
		# i : int ; indice de l'étudiant
		for i in range(len(L)):
			if L[i] != []:
				if L[i][j] == 1:
					liste_comptage[j].append(i)
			
	for x in range(len(liste_comptage)):
		if len(liste_comptage[x]) == 1:
			num_etu = liste_comptage[x][0]
			print('Le stage à', villes[x], 'est attribué à', iden[num_etu])
			stagesprov.append(x)
			etudprov.append(liste_comptage[x][0])
		
		elif len(liste_comptage[x]) > 1:
			chanceux = random.choice(liste_comptage[x])
			print('Le stage à', villes[x], 'est attribué à', iden[chanceux])
			stagesprov.append(x)
			etudprov.append(chanceux)

	#### II. 2. Actualisation de la liste des préférences ####

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

	#### II. 3. Stockage des informations et ménage ####
	
	for x in etudprov:
		etudatt.append(x)
	etudprov = []
	
	for x in stagesprov:
		stagesatt.append(x)
	stagesprov = []
	
	liste_comptage =[]

