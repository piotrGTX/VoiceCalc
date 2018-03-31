import sys;

from LoadData import loadData

X, Y = loadData("./Train")
X_test, Y_test = loadData("./Test")

import tflearn

# Building Residual Network	

# 25%
net = tflearn.input_data(shape=[None, 4000])
net = tflearn.fully_connected(net, 941, activation='CReLU')
net = tflearn.fully_connected(net, 196, activation='CReLU')
net = tflearn.fully_connected(net, 14, activation='Softmax')
net = tflearn.regression(net, optimizer='momentum', loss='categorical_crossentropy', learning_rate=0.2)

# Evaluate model

model = tflearn.DNN(net)
model.fit(X, Y, n_epoch=75, validation_set=(X_test, Y_test), show_metric=True)

# Run the model on one example

# def getAnswer(data):
# 	tab = dict(zip([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+', '-', '*', '/'], data))
# 	return sorted(tab.items(), reverse=True, key=lambda y: y[1])

# while True:
# 	try:
# 		path = input("Ścieżka: ");
# 		example, _ = sf.read(path)

# 		if len(example) >= MAX:
# 			example = example[:MAX]
# 			# Run the model on one example
# 			prediction = model.predict([example])
# 			results = getAnswer(prediction[0])
# 			print('Wykryto: ' + str(results[:2]))
# 	except:
# 		print("Powtórz")