from LoadData import loadData

X, Y = loadData('./Train', spectrogram_step=50)
X_test, Y_test = loadData('./Test', spectrogram_step=50)

import tflearn
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

# Building Residual Network	

# # 93%
net = tflearn.input_data(shape=[None, 401, 11])

net = tflearn.max_pool_1d(net, 4)
net = tflearn.conv_1d(net, 128, 6, activation='relu')
net = tflearn.dropout(net, 0.9)
net = tflearn.avg_pool_1d(net, 2)

net = tflearn.fully_connected(net, 256, activation='relu')
net = tflearn.dropout(net, 0.7)
net = tflearn.fully_connected(net, 128, activation='relu')
net = tflearn.dropout(net, 0.8)

net = tflearn.fully_connected(net, 14, activation='softmax')

net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy', learning_rate=0.005)
	
# Train model

model = tflearn.DNN(net)
model.fit(X, Y, n_epoch=18, validation_set=(X_test, Y_test), show_metric=True)

model.save('models/my_model2.tflearn')	