import sounddevice as sd
import numpy
import tflearn
import os
from scipy import signal
from statistics import mode
import soundfile as sf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def recordSymbols(duration=5):
	FS = 8000
	r = sd.rec(int(duration * FS), samplerate=FS, channels=1).reshape(int(duration*FS))
	print("Nagrywam")
	sd.wait()
	return r

SYMBOLS = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/']

# # 95%
net = tflearn.input_data(shape=[None, 401, 11])

net = tflearn.max_pool_1d(net, 4)
net = tflearn.conv_1d(net, 128, 6, activation='relu')
net = tflearn.avg_pool_1d(net, 2)

net = tflearn.fully_connected(net, 256, activation='relu')
net = tflearn.dropout(net, 0.8)
net = tflearn.fully_connected(net, 128, activation='relu')
net = tflearn.dropout(net, 0.9)

net = tflearn.fully_connected(net, 14, activation='softmax')

net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy', learning_rate=0.005)
	
# Evaluate model

model = tflearn.DNN(net)
model.load('models/my_model.tflearn')

C = 5

def cutSounds(r, limit):
	answers = []
	i = 0
	while i < (len(r) - 4000 - C):
		element = r[i]
		if element > limit:
			for y in range(C):
				this_answer = r[i + y : i + 4000 + y]

				answers.append(this_answer)

			# 100 ms przerwy między nagraniami
			i = i + 4000 + 100 # Przerwa conajmniej 100 ms między słowami
		i = i + 1
	return answers

def whatIsIt(sound):
	_, _, sound = signal.stft(sound, 8000, nperseg=800) 
	X = model.predict([sound]).tolist()[0]
	return SYMBOLS[X.index(max(X))]

while True:
	input("Wcisnij Enter !")
	rs = recordSymbols()
	rs = cutSounds(rs, limit=0.22)

	line = ''
	X_ARR = []
	for r in rs:
		new_char = whatIsIt(r)
		X_ARR.append(new_char)

		if (len(X_ARR) == C): 
			try:
				new_char = mode(X_ARR)
			except:
				new_char = X_ARR[0]

			print(f"TAB: {X_ARR}")
			print(new_char)
			line += new_char
			X_ARR = []

	answer = ''
	try:
		answer = eval(line)
	except:
		answer = "???"
	print(f"{line} = {answer}")


