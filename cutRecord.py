import sounddevice as sd
import soundfile as sf
import numpy
import matplotlib.pyplot as plt
import glob

def recordSymbol():
	fs = 8000
	duration = 5  # seconds
	r = sd.rec(int(duration * fs), samplerate=fs, channels=1).reshape(int(duration*fs))
	print("Nagrywam 10 sekund !")
	sd.wait()
	print("Koniec...")
	return r

def cutSound(r):
	answers = []
	i = 0
	while i < (len(r) - 4000):
		element = r[i]
		if element > 0.1	:
			this_answer = r[i : i+4000]
			answers.append(this_answer)
			i = i + 4200
		i = i + 1
	return answers

def cutFromFile(path):
	d, _ = sf.read(path)
	return cutSound(d)

def cutAllFiles():
	for x in [0,1,2,3,4,5,6,7,8,9,'plus','minus','razy','przez']:
		i = 0
		count = 0

		for path in glob.glob("E:/Projekty/AI/Test/" + str(x) + "/*.wav"):
			rs = cutFromFile(path)
			count = len(rs)
			for r in rs:
				i = i+1
				sf.write("E:/Projekty/AI/Test/" + str(x) + "/outSilent/cutRecord" + str(i) + ".wav", r, 8000)
		print(str(count) + " plików z symbolem " + str(x))

cutAllFiles()