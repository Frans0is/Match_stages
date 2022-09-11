import random

L = []

for x in range(35):
	
	l =[]
	
	while len(l) < 40:
		a = random.randint(1,40)
		if a not in l:
			l.append(a)
			
	L.append(l)
	
print(L)