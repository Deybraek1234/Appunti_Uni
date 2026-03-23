import math
import matplotlib.pyplot as plot
import numpy as np

px = 1/plot.rcParams['figure.dpi']
nb = 5
m = 5000
fig, axs = plot.subplots(nrows = 3, ncols = 3, figsize = (1900*px, 1000*px))
nbins = 80

def Main():
    valore_atteso_uniforme, dev_strd_uniforme = 0.5, 1/np.sqrt(12)
    valore_atteso_esponenziale, dev_strd_esponenziale = 5, 5

    medie_uniforme = [] 
    medie_esponenziale = [] 
    medie_cauchy = []
    for j in range(3):
        match j:
            case 0:
                nb = 5
            case 1:
                nb = 30
            case 2:
                nb = 100

        for i in range(m):
            medie_uniforme.append(media(distrib_uniforme(nb)))
            medie_esponenziale.append(media(distrib_esponenziale(nb)))
            medie_cauchy.append(media(distrib_cauchy(nb)))


        q_medie_uniforme = q(medie_uniforme, np.full(m, valore_atteso_uniforme), np.full(m, dev_strd_uniforme), nb)
        _, borders, _ = axs[j,0].hist(q_medie_uniforme, bins = nbins, range = [-4,4], edgecolor = 'k')
        axs[j,0].set_title(f"Distribuzione Uniforme, n={nb}")
        centers = (borders[:-1] + borders[1:])/2 
        bin_width = borders[1] - borders[0]
        axs[j,0].plot(centers, distrib_normale(centers) * bin_width * m)
        
        q_medie_esponenziale = q(medie_esponenziale, np.full(m, valore_atteso_esponenziale), np.full(m,dev_strd_esponenziale), nb)
        _, borders, _ = axs[j,1].hist(q_medie_esponenziale, bins = nbins, range= [-4,4], edgecolor = 'k')
        axs[j,1].set_title(f"Distribuzione Esponenziale, n={nb}")
        centers = (borders[:-1] + borders[1:])/2
        bin_width = borders[1] - borders[0]
        axs[j,1].plot(centers, distrib_normale(centers) * bin_width * m)

        _, borders, _ = axs[j,2].hist(medie_cauchy, bins = nbins, range = [-4,4], edgecolor = 'k')
        axs[j,2].set_title(f"Distribuzione di Cauchy, n={nb}")
        centers = (borders[:-1] + borders[1:])/2
        bin_width = borders[1] - borders[0]
        axs[j,2].plot(centers, distrib_normale(centers) * bin_width * m)
        axs[j,2].plot(centers, distrib_cauchy_funz(centers) * bin_width*m)

        medie_uniforme.clear()
        medie_esponenziale.clear()
        medie_cauchy.clear()

def q(media, valore_atteso, dev_strd, n):
    return((media - valore_atteso)/(dev_strd/np.sqrt(n)))

def media(data):
    return(np.sum(data)/float(np.size(data)))

def distrib_uniforme(n):
    return(np.random.uniform(0,1,n))

def distrib_esponenziale(n):
    tau = 5
    return(-tau*np.log(1-np.random.uniform(0,1,n)))

def distrib_cauchy(n):
    return(np.divide(np.random.normal(size=n), np.random.normal(size=n)))

def distrib_normale(x):
    return(1/(np.sqrt(2*np.pi )) * np.exp(-(x**2)/2))

def distrib_cauchy_funz(x):
    return(1/np.pi * 1/(1+x**2))

if __name__ == "__main__":
    Main()
    plot.tight_layout()
    plot.show()