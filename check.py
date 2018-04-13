import numpy
from LoadData import loadData

X, Y = loadData("./Train")

last = Y[0]
print(last)

for y in Y:
	if not numpy.array_equal(y, last):
		print(y)
		last = y