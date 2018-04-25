from LoadData import loadData

X, Y = loadData('./Train', spectrogram_step=15)
X_test, Y_test = loadData('./Test', spectrogram_step=15)

import tflearn
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

# Building Residual Network	

# | Adam | epoch: 040 | loss: 0.03133 - acc: 0.9901 | val_loss: 0.06419 - val_acc: 0.9819 -- iter: 5206/5206
net = tflearn.input_data(shape=[None, 121, 35])

net = tflearn.max_pool_1d(net, 4)
net = tflearn.conv_1d(net, 128, 6, activation='relu')
net = tflearn.max_pool_1d(net, 2)
net = tflearn.conv_1d(net, 128, 3, activation='relu')
net = tflearn.avg_pool_1d(net, 2)

net = tflearn.fully_connected(net, 128, activation='relu')
net = tflearn.dropout(net, 0.7)

net = tflearn.fully_connected(net, 14, activation='softmax')

net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy', learning_rate=0.005)
	
# Train model

model = tflearn.DNN(net)
model.fit(X, Y, n_epoch=50, validation_set=(X_test, Y_test), show_metric=True)

model.save('models/my_modelR.tflearn')	