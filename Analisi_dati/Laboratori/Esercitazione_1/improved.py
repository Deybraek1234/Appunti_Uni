import matplotlib.pyplot as plot
import numpy as np
import scipy.special as sp

n_graphs = int(input("How many graphs?"))
px = 1/plot.rcParams['figure.dpi']
N=100000
n_trials = 1000
nbins = 100

fig, axs = plot.subplots(nrows=1, ncols=n_graphs, figsize=(1900*px, 1000*px))

def Main(n_iteration):
    lista_punti = []
    binom = []
    poisson = []

    for _ in range(N):
        lista_punti.append(distrib_uniforme())

    counts, borders, _ = axs[n_iteration].hist(lista_punti, bins=30, edgecolor='k', alpha=0.6, range=[70,130], label="Data Distribution")
    centers = (borders[:-1] + borders[1:])/2
    delta_x = borders[1] - borders[0]
    
    for k in centers:
        binom.append(distrib_binomiale(k, n_trials) * N *delta_x)
        poisson.append(distrib_poisson(k) * N * delta_x)

    axs[n_iteration].plot(centers, binom, 'o', label = "Distribuzione Binomiale")
    axs[n_iteration].plot(centers, poisson, 'o', label = "Distribuzione Poissoniana")
    axs[n_iteration].set_title(f"Iteration: {n_iteration + 1}")

def distrib_uniforme():
    data = np.random.uniform(0,1,N)
    n, bins = np.histogram(data, bins=nbins)
    return n[5]

def distrib_binomiale(k, n):
    p = 1/nbins
    k = int(k)
    coeff_binomiale = sp.comb(n, k)
    return (coeff_binomiale * (p**k) * ((1-p)**(n-k)))

def distrib_poisson(k):
    lam = n_trials * (1/nbins)
    k = int(k)
    return(lam**(k)/sp.factorial(int(k)) * np.exp(-lam))

if __name__ == "__main__":
    for _ in range(n_graphs):
        Main(_)

    handles, labels = axs[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper right', bbox_to_anchor=(0.98, 0.98))
    fig.tight_layout(rect=[0,0.03, 1, 0.95])
    fig.suptitle("Uniform Distributions")
    plot.show()