
import matplotlib.pyplot as plt
import numpy as np

import librosa
import librosa.display
import soundfile as sf
import IPython.display
from IPython.display import Audio

np.set_printoptions(linewidth=170, edgeitems=105)

audio, sr = sf.read('AnalisisTextos_convertido.wav')

print(audio)
print("\n Largo array: ", len(audio))
print("\n Frecuencia de Muestreo: ", sr)
print("\n Duracion: ", len(audio)/sr)

plt.plot(audio)
plt.show()

sf.write('AnalisisTextos_acelerado.wav', audio, samplerate = sr*2)
print("\n Archivo acelerado")

sf.write('AnalisisTextos_desacelerado.wav', audio, samplerate = int(sr/2))
print("\n Archivo desacelerado")

# reproducción de array diferente profundidad de bits
audio_8bits = (audio*(2**3)).astype(np.float32)

sf.write("AnalisisTextos_8bits.wav", audio_8bits, samplerate = sr, subtype = "PCM_U8")
print("\n Calidad degradada")

plt.plot(audio_8bits)
plt.show()