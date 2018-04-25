import soundfile as sf
import numpy
import glob
import uuid
import random
from concurrent.futures import ThreadPoolExecutor
import os

# Ścieżka do katalogu z folderami
DIR_PATH = 'E:\Projekty\AI\Train'
OUT_DIR_NAME = 'out'
# Nazwy folderów do przeszukania
ALL_SYMBOLS = ['0','1','2','3','4','5','6','7','8','9','plus','minus','razy','przez']
LENGTH = int(0.5 * 8000)

def cutSounds(r, limit):
	answers = []

	i = 100
	while i < (len(r) - LENGTH):
		element = r[i]
		if element > limit:
			# Plik oryginalny
			this_answer = r[i : i + LENGTH]
			answers.append(this_answer)

			i = i + LENGTH + 200 # Przerwa conajmniej 200 ms między słowami
		i = i + 1
	return answers

def cutFromFile(path):
	d, _ = sf.read(path)
	d = cutSounds(d, limit=0.12) + cutSounds(d, limit=0.22)
	return d

def cutAllInFolder(x):
	# Utworzenie nowego kanalogu i wytłumienie outputu jeśli katalog istnieje
	os.system(f"mkdir {DIR_PATH}\{x}\{OUT_DIR_NAME} 2> NUL")
	count = 0
	for path in glob.glob(f"{DIR_PATH}\{x}\*.wav"):
		i = 0
		random_name = str(uuid.uuid4().hex)
		rs = cutFromFile(path)
		count += len(rs)
		for r in rs:
			i = i+1
			sf.write(f"{DIR_PATH}\{x}\{OUT_DIR_NAME}\{random_name}{i}.wav", r, 8000)
	print(f"{count} plików z symbolem {x}")

def cutAllFiles():
	executor = ThreadPoolExecutor(3)
	for x in ALL_SYMBOLS:
		executor.submit(cutAllInFolder, x)


# cutAllFiles()
rs = cutFromFile('E:\\Projekty\\AI\\Train\\3\\3d.wav')
i = 0
random_name = str(uuid.uuid4().hex)
for r in rs:
	i = i+1
	sf.write(f"{DIR_PATH}\\3\\{OUT_DIR_NAME}\{random_name}{i}.wav", r, 8000)