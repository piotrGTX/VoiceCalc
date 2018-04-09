from LoadData import loadData
import os

X, _, P = loadData("./Train")

i = 0
for elem in X:
	value = abs(sum(elem))
	if value < 1:
		os.remove(P[i])
		print("Bardzo slaby plik: " + P[i])
	elif value < 3:
		print("Slaby plik: " + P[i])	
	i = i + 1
