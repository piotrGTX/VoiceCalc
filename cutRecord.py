import soundfile as sf
import numpy
import glob
import uuid
import random
import threading

# Ścieżka do katalogu z folderami
DIR_PATH = 'E:/Projekty/AI/Train'
# Nazwy folderów do przeszukania
ALL_SYMBOLS = ['0','1','2','3','4','5','6','7','8','9','plus','minus','razy','przez']

def cutSound(r):
	answers = []
	i = 0
	while i < (len(r) - 4000):
		element = r[i]
		if element > 0.2:
			# Plik oryginalny
			this_answer = r[i : i + 4000]
			answers.append(this_answer)
			# Plik zgłośniony
			this_answer = this_answer * random.uniform(1.2, 1.5)
			answers.append(this_answer)
			# Plik zcisoszony
			this_answer = this_answer * random.uniform(0.8, 0.5)
			answers.append(this_answer)

			# 100 ms przerwy między nagraniami
			i = i + 4100 
		i = i + 1
	return answers

def cutFromFile(path):
	d, _ = sf.read(path)
	return cutSound(d)

def cutAllFiles():
	for x in ALL_SYMBOLS:
		t = threading.Thread(target=cutAllInFolder, args=(x,))
		t.start()

def cutAllInFolder(x):
	count = 0
	for path in glob.glob(f"{DIR_PATH}/{x}/*.wav"):
		i = 0
		random_name = str(uuid.uuid4().hex)
		rs = cutFromFile(path)
		count += len(rs)
		for r in rs:
			i = i+1
			sf.write(f"{DIR_PATH}/{x}/outSilent/{random_name}{i}.wav", r, 8000)
	print(f"{count} plików z symbolem {x}")

cutAllFiles()