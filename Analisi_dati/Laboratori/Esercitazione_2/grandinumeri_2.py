import math
import matplotlib.pyplot as plot
import numpy as np

# set constants
px = 1/plot.rcParams['figure.dpi']
nb = 5
m = 5000
fig, axs = plot.subplots(nrows = 3, ncols = 3, figsize = (1900*px, 1000*px))
nbins = 80

def Main():
    # valori per valori attesi/deviazioni standard per le distribuzioni
    valore_atteso_uniforme, dev_strd_uniforme = 0.5, 1/np.sqrt(12)
    valore_atteso_esponenziale, dev_strd_esponenziale = 5, 5

    # initialize arrays
    medie_uniforme = [] 
    medie_esponenziale = [] 
    medie_cauchy = []
    # for loop to repeat 3 times
    for j in range(3):
        # for every for loop run once, nb impone quanti dati generare per ciclo
        match j:
            case 0:
                nb = 5
            case 1:
                nb = 30
            case 2:
                nb = 100

        # fill arrays with data from distributions
        for i in range(m):
            medie_uniforme.append(media(distrib_uniforme(nb)))
            medie_esponenziale.append(media(distrib_esponenziale(nb)))
            medie_cauchy.append(media(distrib_cauchy(nb)))

        # calculate Q=(bar(x)-mu)/(stddev / sqrt(nb))
        q_medie_uniforme = q(medie_uniforme, np.full(m, valore_atteso_uniforme), np.full(m, dev_strd_uniforme), nb)
        # make histogram
        counts, borders, _ = axs[j,0].hist(q_medie_uniforme, bins = nbins, range = [-4,4], edgecolor = 'k', label = "Dati Generati")
        centers = (borders[:-1] + borders[1:])/2 
        # calculate statistical error
        err = np.sqrt(counts)
        # plot statistical errors
        axs[j,0].errorbar(centers, counts, yerr=err, ecolor = "red", fmt = "none", elinewidth=1, capsize = 2, label = "Errore Statistico", alpha = 0.6)
        bin_width = borders[1] - borders[0]
        # sovrapporre distribuzione scalata
        axs[j,0].plot(centers, distrib_normale(centers) * bin_width * m, label = "Distribuzione Normale Attesa")    

        axs[j,0].set_title(f"Distribuzione Uniforme, n={nb}")
        axs[j,0].set_xlabel("Valori di Q")
        axs[j,0].set_ylabel("Frequenza")
        
        q_medie_esponenziale = q(medie_esponenziale, np.full(m, valore_atteso_esponenziale), np.full(m,dev_strd_esponenziale), nb)
        counts, borders, _ = axs[j,1].hist(q_medie_esponenziale, bins = nbins, range= [-4,4], edgecolor = 'k', label = "Dati Generati")
        centers = (borders[:-1] + borders[1:])/2
        err = np.sqrt(counts)
        bin_width = borders[1] - borders[0]
        axs[j,1].plot(centers, distrib_normale(centers) * bin_width * m, label = "Distribuzione Normale attesa")
        axs[j,1].errorbar(centers, counts, yerr=err, fmt = "none", ecolor = "red", elinewidth = 1, capsize = 2, label = "Errore Statistico", alpha = 0.6)

        axs[j,1].set_title(f"Distribuzione Esponenziale, n={nb}")
        axs[j,1].set_xlabel("Valori di Q")
        axs[j,1].set_ylabel("Frequenza")

        # no Q for Cauchy Distribution because doesn't have mean/std_dev
        counts, borders, _ = axs[j,2].hist(medie_cauchy, bins = nbins, range = [-4,4], edgecolor = 'k', label = "Dati Generati")
        centers = (borders[:-1] + borders[1:])/2
        err = np.sqrt(counts)
        bin_width = borders[1] - borders[0]
        axs[j,2].plot(centers, distrib_normale(centers) * bin_width * m, label = "Distribuzione Normale")
        axs[j,2].plot(centers, distrib_cauchy_funz(centers) * bin_width*m, label = "Distribuzione di Cauchy")
        axs[j,2].errorbar(centers, counts, yerr=err, fmt = "none", ecolor = "red", elinewidth = 1, capsize = 2, label = "Errore Statistico", alpha = 0.6)

        axs[j,2].set_title(f"Distribuzione di Cauchy, n={nb}")
        axs[j,2].set_xlabel("Valori di Q")
        axs[j,2].set_ylabel("Frequenza")

        # clear data for next run
        medie_uniforme.clear()
        medie_esponenziale.clear()
        medie_cauchy.clear()

# funzione per calcolare Q
def q(media, valore_atteso, dev_strd, n):
    return((media - valore_atteso)/(dev_strd/np.sqrt(n)))

def media(data):
    return(np.sum(data)/float(np.size(data)))

def distrib_uniforme(n):
    return(np.random.uniform(0,1,n))

def distrib_esponenziale(n):
    tau = 5
    return(-tau*np.log(1-np.random.uniform(0,1,n)))

# funzione per generare dati seguendo distribuzione Cauchy
def distrib_cauchy(n):
    return(np.divide(np.random.normal(size=n), np.random.normal(size=n)))

def distrib_normale(x):
    return(1/(np.sqrt(2*np.pi )) * np.exp(-(x**2)/2))

# funzione per distribuzione di Cauchy standardizzata
def distrib_cauchy_funz(x):
    return(1/np.pi * 1/(1+x**2))

if __name__ == "__main__":
    Main()

    handles, labels = axs[0,2].get_legend_handles_labels()
    fig.legend(handles, labels, loc = 'upper right')
    plot.tight_layout()
    plot.show()