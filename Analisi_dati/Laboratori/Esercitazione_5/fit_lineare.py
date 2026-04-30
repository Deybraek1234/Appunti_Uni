import numpy as np
import math
import matplotlib.pyplot as plot

tempo = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
conteggi = np.array([997, 520, 265, 127, 70, 35, 16, 7, 3])

ln_conteggi = np.log(conteggi)
sigma = 1/np.sqrt(conteggi)

#plot.plot(tempo, conteggi, 'o')
plot.errorbar(tempo, ln_conteggi, yerr=sigma, fmt='o', label="Dati con Errore")
plot.grid(True)
plot.legend()

N = len(t)

plot.show()

