import soundfile as sf
import numpy
from scipy import signal
import matplotlib.pyplot as plt

def print_plot(d, nperseg=20):
	f, t, Zxx = signal.stft(d, 8000, nperseg=nperseg)
	plt.pcolormesh(t, f, numpy.abs(Zxx), vmin=0)
	plt.title(f'STFT Magnitude of {8000/nperseg} ms')
	plt.ylabel('Frequency [Hz]')
	plt.xlabel('Time [sec]')
	plt.show()

def print_plot2(d):
	f, t, Sxx = signal.spectrogram(d, 8000)
	plt.pcolormesh(t, f, Sxx)
	plt.title('Spectrogram')
	plt.ylabel('Frequency [Hz]')
	plt.xlabel('Time [sec]')
	plt.show()

def read_Sound(symbol):
	d, _ = sf.read(f"E:/Projekty/AI/Train/{symbol}/outSilent/out002.wav")
	return d

sound = read_Sound('1')

print_plot(sound, 800)
