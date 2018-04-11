from LoadData import loadData

X, Y, _ = loadData("./Train")
X_test, Y_test, _ = loadData("./Test")

import tflearn
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

print(X.shape)

# Building Residual Network	

# # 88%
net = tflearn.input_data(shape=[None, 401, 11])
net = tflearn.max_pool_1d(net, 5)
net = tflearn.dropout(net, 0.7)
net = tflearn.fully_connected(net, 64, activation='relu')
net = tflearn.fully_connected(net, 14, activation='softmax')

net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy', learning_rate=0.01)
	
# Train model

model = tflearn.DNN(net)
model.fit(X, Y, n_epoch=20, validation_set=(X_test, Y_test), show_metric=True)
# model.fit(X, Y, n_epoch=12, validation_set=0.08, show_metric=True)

model.save('models/my_model.tflearn')