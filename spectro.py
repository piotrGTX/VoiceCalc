import soundfile as sf
import numpy
from scipy import signal
import matplotlib.pyplot as plt

def print_plot(d, step):
	f, t, Zxx = signal.stft(d, 8000, nperseg=(16*step))
	plt.pcolormesh(t, f, numpy.abs(Zxx), vmin=0)
	plt.title(f'STFT Magnitude of {step} ms')
	plt.ylabel('Frequency [Hz]')
	plt.xlabel('Time [ms]')
	plt.show()

sound, _ = sf.read('E:\\Projekty\\AI\\Train\\3\\out\\d067a620092b4204bc2ff797b0773cff31.wav')
print_plot(sound, 15)

sound, _ = sf.read('E:\\Projekty\\AI\\Train\\4\\out\\6d545321fb3d48debe0d23dac256446f9.wav')
print_plot(sound, 15)