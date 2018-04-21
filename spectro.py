import soundfile as sf
import numpy
from scipy import signal
import matplotlib.pyplot as plt

def print_plot(d, nperseg):
	f, t, Zxx = signal.stft(d, 8000, nperseg=nperseg)
	plt.pcolormesh(t, f, numpy.abs(Zxx), vmin=0)
	plt.title(f'STFT Magnitude of {nperseg/1600} ms')
	plt.ylabel('Frequency [Hz]')
	plt.xlabel('Time [sec]')
	plt.show()

def read_Sound(symbol):
	d, _ = sf.read(f"E:/Projekty/AI/Train/{symbol}/out/1c7d7110bf9b4af69ca157e81f78324911.wav")
	return d

sound = read_Sound('3')

print_plot(sound, 16*50)
