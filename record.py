import sounddevice as sd
import numpy
import tflearn
import os
from scipy import signal

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def recordSymbol():
	fs = 8000
	duration = 5  # seconds
	power = 0
	r = sd.rec(int(duration * fs), samplerate=fs, channels=1).reshape(int(duration*fs))
	print("Nagrywam")
	sd.wait()
	return r

SYMBOLS = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/']

# # 25%
net = tflearn.input_data(shape=[None, 401, 11])
net = tflearn.max_pool_1d(net, 6)
net = tflearn.conv_1d(net, 24, 4, activation='crelu')
net = tflearn.dropout(net, 0.6)
net = tflearn.fully_connected(net, 96, activation='relu')
net = tflearn.dropout(net, 0.6)
net = tflearn.fully_connected(net, 14, activation='softmax')

net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy', learning_rate=0.01)
	
# Evaluate model

model = tflearn.DNN(net)
model.load('models/my_model.tflearn')

def whatIsIt(sound):
	_, _, sound = signal.stft(sound, 8000, nperseg=800) 
	X = model.predict([sound]).tolist()[0]
	return SYMBOLS[X.index(max(X))]

def cutSound(r):
	answers = []
	i = 0
	while i < (len(r) - 4000):
		element = r[i]
		if element > 0.5:
			this_answer = r[i : i + 4000]
			answers.append(this_answer)
			i = i + 4100
		i = i + 1
	return answers

while True:
	input("Wciśnij enter aby zacząć nagrywać")
	rs = recordSymbol()
	rs = cutSound(rs)
	line = ''
	for r in rs:
		char = whatIsIt(r)
		if char:
			line += char
			print(char, end=' ')
	print(f" = ...")
