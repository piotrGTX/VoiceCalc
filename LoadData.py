import soundfile as sf
import numpy
import glob
from scipy import signal

def loadData(rootPath, symbols=[0,1,2,3,4,5,6,7,8,9,'plus','minus','razy','przez'], spectrogram_step=50):
	data = []
	labels = []
	EMPTY_INPUT = [0]*14

	# Częstotliwość
	FREQUENCY = 8000
	# Długość nagrania
	MAX = int(0.5 * FREQUENCY)
	
	for x in symbols:
		for path in glob.glob(f"{rootPath}/{x}/out/*.wav"):
			d, sample = sf.read(path)
			if len(d) >= MAX:
				d = d[:MAX]
				tab = list(EMPTY_INPUT)
				if isinstance(x, int) and x <= 9:
					tab[x] = 1
				elif x == 'plus':
					tab[10] = 1
				elif x == 'minus':
					tab[11] = 1
				elif x == 'razy':
					tab[12] = 1
				else:
					tab[13] = 1

				# 1600 nperseg = 100 ms
				# 800 nperseg = 50 ms
				_, _, d = signal.stft(d, FREQUENCY, nperseg=(16*spectrogram_step)) 
				d = numpy.abs(d)

				data.append(d)
				labels.append(tab)
	
	# Zamiana listy na numpy
	data = numpy.array(data)
	labels = numpy.array(labels)

	# Mieszanie danych
	randomize = numpy.arange(len(data))
	numpy.random.shuffle(randomize)
	data = data[randomize]
	labels = labels[randomize]

	return data, labels

