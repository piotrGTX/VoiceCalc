from LoadData import loadData

X, Y = loadData("./Train")
X_test, Y_test = loadData("./Test")

import tflearn
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

# Building Residual Network	

# # 93%
net = tflearn.input_data(shape=[None, 401, 11])

net = tflearn.max_pool_1d(net, 6)
net = tflearn.max_pool_1d(net, 5)	

net = tflearn.fully_connected(net, 128, activation='relu')
net = tflearn.dropout(net, 0.6)

net = tflearn.fully_connected(net, 14, activation='softmax')

net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy', learning_rate=0.02)
	
# Train model

model = tflearn.DNN(net)
model.fit(X, Y, n_epoch=15, validation_set=(X_test, Y_test), show_metric=True)
# model.fit(X, Y, n_epoch=15, validation_set=0.08, show_metric=True)

model.save('models/my_model.tflearn')	