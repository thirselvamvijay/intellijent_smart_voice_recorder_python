import numpy as np
from scipy.fftpack import fft as fft
from scipy.io import wavfile
from numpy import mean


class FindEnergyOfTheVoice:
    @staticmethod
    def findEnergyOfTheVoice(path):
        rate, audData = wavfile.read(path)
        print(rate)
        print(audData)
        length = audData.shape[0] / rate
        print("length: ", length)
        fourier = fft(audData)
        n = len(audData)
        energy = 10 * np.log10(fourier)
        energy = int(mean(energy))
        return energy
