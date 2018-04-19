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

def cutSounds(r, limit=0.07):
	answers = []

	i = 0
	while i < (len(r) - 4000):
		element = r[i]
		if element > limit:
			# Plik oryginalny
			this_answer = r[i : i + 4000]
			answers.append(this_answer)

			# # Cicha wersja
			# answers.append(this_answer * random.uniform(0.5, 0.2))

			# # Głośna wersja
			# answers.append(this_answer * random.uniform(1.5, 1.8))

			# 100 ms przerwy między nagraniami
			i = i + 4000 + 100 # Przerwa conajmniej 100 ms między słowami
		i = i + 1
	return answers

def cutFromFile(path):
	# Utworzenie nowego kanalogu i wytłumienie outputu jeśli katalog istnieje
	d, _ = sf.read(path)
	return cutSounds(d)

def cutAllInFolder(x):
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
	executor = ThreadPoolExecutor(4)
	for x in ALL_SYMBOLS:
		executor.submit(cutAllInFolder, x)

# cutAllFiles()