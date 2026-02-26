# Dato che unan moneta pudare testa o croce d ogni lancio, la probabilitá che esca testa ad ogni lancio é p=0.5. Useremo la binomiale con k=6, n=10, p=0.5. 

#import math library for calculations
import math
from scipy.stats import binom

k = 6
n = 10
p = 0.5

coeff_binomiale = math.comb(n,k)
probabilita_binomiale = coeff_binomiale * (p**k) * ((1-p)**(n-k))
print(f"La probabilitá di ottenere {k} teste in {n} lanci é: ", probabilita_binomiale)
print(f"La stessa probabilitá usando la funzione binom.pmf é: ", binom.pmf(k, n, p))