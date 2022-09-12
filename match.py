#### Bibliothèque #####

import random

#### Programme ########

# 0.  Génération de la liste des préférences et affichage
# On génère des listes de noms d'étudiants, de villes de stages et de préférences 

# Exemples de listes de préférences des étudiants a, b, c et d : l'étudiant a (n°0) préfère le stage n°0 quand l'étudiant b (n°1) préfère le stage n°4 (python commence son compte à 0)
# En réalité ces listes seront extraites d'un document csv (tableur)

a = [1,2,3,4,5]
b = [2,5,3,4,1]
c = [1,4,3,2,5]
d = [1,3,2,4,5]

# liste de 35 identités
iden = ['Thélio Lalau', 'Othman Matuszak', 'Judicael Vignolles', 'Noélie Lecompte', 'Lyes Hamzaoui', 'Jaden Grancher', 'Tolga Lin', 'Leyna Deyres', 'Souhayl Pantalacci', 'Pablo Tranier', 'Roxane Gadal', 'Stevens Mourrain', 'Safia Ritz', 'Alyson Fardin', 'Castille Beaujour', 'Belinda Scotto', 'Elma Belorgey', 'Taylor Liogier', 'Lambert Le Provost', 'Jean-Francis Beduneau', 'Ezechiel Depoilly', 'Marc-Antoine Meckes', 'Myriane Oudard', 'Giuseppe Croizer', 'Aidan Mihoubi', 'Zita Housseau', 'Adelin Hauser', 'Shelly Baris', 'Christèle Legault', 'Graziella Capoulade', 'Noura Caillon', 'Annik Despierres', 'Marguerite Verez', 'Céleste Coulais', 'Eslem Coulaud']
# liste de 40 lieux de stages
villes = ['Naperville', 'Lancaster', 'Killeen', 'Ocala', 'New London', 'Frederick', 'Santa Ana', 'Temecula', 'Oceanside', 'Santa Maria', 'Mobile', 'Aurora', 'Huntsville', 'Denver', 'Concord', 'Henderson', 'San Jose', 'Port Arthur', 'Orem', 'Pueblo', 'Rancho Cucamonga', 'Springfield', 'Beaumont', 'Kissimmee', 'Odessa', 'Cedar Rapids', 'Mission Viejo', 'Clearwater', 'Davenport', 'Austin', 'Punta Gorda', 'Victorville', 'Overland Park', 'Naples', 'Trenton', 'Plano', 'Havre de Grace', 'Davidson County', 'Tyler', 'El Paso']


# Pour tester ce programme en conditions réelles, on génère 35 listes des 40 premiers entiers naturels (à partir de 1) ordonnées aléatoirement.


# L : list[list[int]]
L = []

for x in range(35):
	
	l =[]
	
	while len(l) < 40:
		a = random.randint(1,40)
		if a not in l:
			l.append(a)
			
	L.append(l)
	

### On regarde les préférences en détails dans un fichier
### En réalité on partira de ce fichier pour la suite, 
### au lieu de l'écrire comme ici, on le lira !

flux = open('preferences.csv','w')

# La liste des lieux de stages en haut du tableau
flux.write ('\t')
for x in villes:
	flux.write(x)
	flux.write('\t')
flux.write('\n')

# À chaque ligne un étudiant et ses préférences
for x in range(len(iden)):
	flux.write(iden[x])
	flux.write('\t')
	for y in range(len(L[x])):
		flux.write(str(L[x][y]))
		flux.write('\t')
	flux.write('\n')
	
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
			#print('Le stage numéro', x, 'est attribué à l\'étudiant numéro', liste_comptage[x][0])
			num_etu = liste_comptage[x][0]
			print('Le stage à', villes[x], 'est attribué à', iden[num_etu],'*')
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
	

print(stagesatt)
print(etudatt)
