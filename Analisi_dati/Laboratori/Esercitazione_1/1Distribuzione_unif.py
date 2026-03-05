import matplotlib.pyplot as plot
import numpy as np
import math

N = 1000
data = np.random.uniform(0,1,N)
nbins = 10

n_in_each_bin, bins, patches = plot.hist(data, bins=nbins, edgecolor='k', alpha=0.6, label="Istogramma")

centri = (bins[:-1] + bins[1:])/2

print("Preso il bin numero 5:")
print(f"Il numero di punti in questo bin è {n_in_each_bin[5]}")
print(f"Il valore di aspettazione in questo bin è {N*1/nbins}")
print(f"La deviazione standard di questo bin è {1/math.sqrt(12)}")

prob = np.full(10, N/nbins)

plot.plot(centri, prob, 'o', label="Distribuzione Uniforme teorica")
plot.xlabel('Valori')
plot.ylabel('Frequenza')
plot.title('Istogramma dei dati')
plot.legend()
plot.show()