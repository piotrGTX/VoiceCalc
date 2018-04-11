import soundfile as sf
import numpy
import glob
from scipy import signal

def loadData(rootPath, symbols=[0,1,2,3,4,5,6,7,8,9,'plus','minus','razy','przez']):
	data = []
	labels = []
	paths = []
	MAX = 4000

	EMPTY_INPUT = [0]*14
	for x in symbols:
		for path in glob.glob(rootPath + "/" + str(x) + "/outSilent/*.wav"):
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

				_, _, d = signal.stft(d, 8000, nperseg=800) 

				data.append(d)
				labels.append(tab)
				paths.append(path)
	
	data = numpy.array(data)
	labels = numpy.array(labels)

	randomize = numpy.arange(len(data))
	numpy.random.shuffle(randomize)
	data = data[randomize]
	labels = labels[randomize]

	return data, labels, paths
