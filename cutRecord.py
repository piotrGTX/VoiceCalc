import sounddevice as sd
import soundfile as sf
import numpy
import matplotlib.pyplot as plt
import glob
import uuid

def cutSound(r):
	answers = []
	i = 0
	while i < (len(r) - 4000):
		element = r[i]
		if element > 0.05:
			this_answer = r[i : i + 4000]
			answers.append(this_answer)
			i = i + 4200
		i = i + 1
	return answers

def cutFromFile(path):
	d, _ = sf.read(path)
	return cutSound(d)

def cutAllFiles():
	for x in ['0','1','2','3','4','5','6','7','8','9','plus','minus','razy','przez']:
		i = 0
		count = 0
		for path in glob.glob(f"E:/Projekty/AI/Train/{x}/*.wav"):
			random_name = str(uuid.uuid4().hex)
			rs = cutFromFile(path)
			count = len(rs)
			for r in rs:
				i = i+1
				sf.write(f"E:/Projekty/AI/Train/{x}/outSilent/{random_name}{i}.wav", r, 8000)
			print(f"Tworze serie plików o nazwie: {random_name}")
		print(f"{count} plików z symbolem {x}")

cutAllFiles()