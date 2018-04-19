import sounddevice as sd
import numpy
import tflearn
import os
from cutRecord import cutSounds
from scipy import signal


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def recordSymbols():
	fs = 8000
	duration = 5  # seconds
	power = 0
	r = sd.rec(int(duration * fs), samplerate=fs, channels=1).reshape(int(duration*fs))
	print("Nagrywam")
	sd.wait()
	return r

SYMBOLS = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/']

# # 92%
net = tflearn.input_data(shape=[None, 401, 11])

net = tflearn.max_pool_1d(net, 6)
net = tflearn.max_pool_1d(net, 5)	

net = tflearn.fully_connected(net, 128, activation='relu')
net = tflearn.dropout(net, 0.6)

net = tflearn.fully_connected(net, 14, activation='softmax')

net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy', learning_rate=0.02)
	
# Evaluate model

model = tflearn.DNN(net)
model.load('models/my_model.tflearn')

def whatIsIt(sound):
	_, _, sound = signal.stft(sound, 8000, nperseg=800) 
	X = model.predict([sound]).tolist()[0]
	return SYMBOLS[X.index(max(X))]

while True:
	input("Wciśnij enter aby zacząć nagrywać")
	rs = recordSymbols()
	rs = cutSounds(rs, limit=0.15)

	line = ''
	for r in rs:
		line += whatIsIt(r)

	answer = ''
	try:
		answer = eval(line)
	except:
		answer = "???"
	print(f"{line} = {answer}")


