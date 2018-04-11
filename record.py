import sounddevice as sd
import numpy
import tflearn
import os
from scipy import signal

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def recordSymbol():
	fs = 8000
	duration = 3  # seconds
	power = 0
	r = sd.rec(int(duration * fs), samplerate=fs, channels=1).reshape(int(duration*fs))
	print("Nagrywam")
	sd.wait()
	return r

SYMBOLS = [0,1,2,3,4,5,6,7,8,9,'+','-','*','/']

# # 25%
net = tflearn.input_data(shape=[None, 401, 11])
net = tflearn.max_pool_1d(net, 5)
net = tflearn.dropout(net, 0.7)
net = tflearn.fully_connected(net, 64, activation='relu')
net = tflearn.fully_connected(net, 14, activation='softmax')

net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy', learning_rate=0.01)
	
# Evaluate model

model = tflearn.DNN(net)
model.load('models/my_model.tflearn')

def whatIsIt(sound):
	_, _, sound = signal.stft(sound, 8000, nperseg=800) 
	X = model.predict([sound]).tolist()[0]
	answer = SYMBOLS[X.index(max(X))]
	print("Answer = " + str(answer))


while True:
	r = recordSymbol()

	start_element = next((x for x in r if x > 0.01), None)

	if start_element is not None:

		r = r.tolist()
		start_index = r.index(start_element)

		if start_element + 4000 >= len(r):
			continue

		r = r[ start_index : start_index + 4000]

		# A = 1000
		# B = 4000 - A

		# if (max_id < A) or (max_id + B >= len(r)):
		# 	print("Ucięcie..")
		# 	continue
		# else:
		# 	r = r[max_id-A : max_id + B]

		# sd.playrec(r, 8000, channels=1)
		# sd.wait()

		whatIsIt(r)
		sd.playrec(r, 8000, channels=1)
		sd.wait()
		print("")