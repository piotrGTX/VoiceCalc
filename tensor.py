from LoadData import loadData

X, Y, _ = loadData("./Train")
X_test, Y_test, _ = loadData("./Test")

import tflearn
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

# Building Residual Network	

# # 25%
net = tflearn.input_data(shape=[None, 2001])	
net = tflearn.fully_connected(net, 128, activation='crelu')
net = tflearn.dropout(net, 0.5)
net = tflearn.fully_connected(net, 64, activation='crelu')
net = tflearn.dropout(net, 0.7)
net = tflearn.fully_connected(net, 14, activation='softmax')

proxi_adagrad = tflearn.ProximalAdaGrad(learning_rate=0.001, initial_accumulator_value=0.001)
net = tflearn.regression(net, optimizer=proxi_adagrad)
	
# Evaluate model

model = tflearn.DNN(net)
model.fit(X, Y, n_epoch=12, batch_size=25, validation_set=(X_test, Y_test), show_metric=True)
#model.fit(X, Y, n_epoch=12, validation_set=0.05, show_metric=True)