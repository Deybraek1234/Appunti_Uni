import math
import matplotlib.pyplot as plot
import numpy as np

lista_punti = []

N=1000
nbins = 10

def distrib_uniforme():
    data = np.random.uniform(0,1,N)

    n, bins = np.histogram(data, bins=nbins)
    return n[5]

for x in range(N):
    lista_punti.append(distrib_uniforme())

binom = []
def distrib_binomiale(k):
    p = 1/nbins

    coeff_binomiale = math.comb(N, int(k))
    return (coeff_binomiale * (p**k)* ((1-p)**(N-k)))

n, bordi, patches = plot.hist(lista_punti, bins=30, edgecolor='k', alpha=0.6, range=[70,130], label="Distribuzione Uniforme")
centri = (bordi[:-1] + bordi[1:])/2
delta_x = bordi[1] - bordi[0]

for k in centri:
    result = distrib_binomiale(k)*N*delta_x
    binom.append(result)

poisson = []
def distrib_poisson(k):
    lam = N * 1/nbins

    return (lam**(k)/math.factorial(int(k)) * np.exp(-lam))

for k in centri:
    result = distrib_poisson(k) * N * delta_x
    poisson.append(result)
    

print("Done")
plot.plot(centri, binom, 'o', label="Distribuzione Binomiale")
plot.plot(centri, poisson, 'o', label="Distribuzione Poissoniana")
plot.xlabel('Valori')
plot.ylabel('Frequenza')
plot.title('Istogramma dei dati')
plot.legend()
plot.show()