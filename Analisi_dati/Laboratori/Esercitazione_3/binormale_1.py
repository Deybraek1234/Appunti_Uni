import numpy as np
import matplotlib.pyplot as plot

# Constants
px = 1/plot.rcParams['figure.dpi']
n = 10000
fig, axs = plot.subplots(nrows = 2, ncols = 2, figsize = [1900*px, 1000*px])
std_dev = 0.0002
mu1 = 0.01
mu2 = 0.02

# funzione per generare dati e creare primi istogrammi
def initialize():
    global gaussian_func
    def gaussian_func(x, mu, sigma):
        return (1/(np.sqrt(2*np.pi)*sigma) * np.exp(-((x-mu)**2)/(2*sigma**2)))
    
    # genera dati, global così anche la funzione plot_graphs può vederla
    global l1 
    l1 = np.random.normal(loc = mu1, scale = std_dev, size = n)
    global l2 
    l2 = np.random.normal(loc = mu2, scale = std_dev, size = n)

    # histogramma normale prima misura
    counts, borders, _ = axs[0,0].hist(l1, bins = 80, range=[mu1-4*std_dev, mu1+4*std_dev], edgecolor = 'k', label="Valori generati mu1")
    axs[0,0].set_xlabel("Valori generati centrati in 0.01 (m)")
    axs[0,0].set_ylabel("Frequenza")
    # calcoli per gaussiana prima
    centers = (borders[:-1] + borders[1:])/2
    bin_width = borders[1] - borders[0]
    expected_centers = gaussian_func(centers, mu1, std_dev) * n * bin_width
    axs[0,0].plot(centers, expected_centers, '-', label="Gaussiana Aspettata l1")
    axs[0,0].set_ylim(bottom=0.0)
    # errori
    errors = np.sqrt(counts)
    axs[0,0].errorbar(centers, counts, yerr=errors, elinewidth=1, capsize=2, ecolor='red', fmt='none', alpha=0.6, label = "Errori l1")
    axs[0,0].legend()
    axs[0,0].set_title("Dati generati per l1")

    # histogramma normale seconda misura
    counts, borders, _ = axs[0,1].hist(l2, bins = 80, range=[mu2-4*std_dev, mu2+4*std_dev], edgecolor = 'k', label="Valori generati mu2")
    axs[0,1].set_xlabel("Valori generati centrati in 0.02 (m)")
    axs[0,1].set_xlabel("Frequenza")
    # calcoli per gaussiana seconda
    centers = (borders[:-1] + borders[1:])/2
    bin_width = borders[1] - borders[0]
    expected_centers = gaussian_func(centers, mu2, std_dev) * n * bin_width 
    axs[0,1].plot(centers, expected_centers, '-', label="Gaussiana Aspettata l2")
    axs[0,1].set_ylim(bottom=0.0)
    # errori
    errors = np.sqrt(counts)
    axs[0,1].errorbar(centers, counts, yerr=errors, elinewidth=1, capsize=2, ecolor='red', fmt='none', alpha=0.6, label = "Errori l2")
    axs[0,1].legend()
    axs[0,1].set_title("Dati generati per l2")

# funzione per fare i calcoli della covariansa e coefficiente correlazione
def calcolo_cov():
    # funzione per calcolare covarianza di xy
    def covariance_xy(x,y):
        x_mean = np.sum(x)/n
        y_mean = np.sum(y)/n
        cov_xy = np.sum((x - x_mean)*(y - y_mean))/(n-1)

        return cov_xy
    # funzione per calcolare q2
    def q2(r, x, y, mux, muy, std_devx = std_dev, std_devy = std_dev):
        return 1/(1-r**2)*(((x-mux)/std_devx)**2 + ((y-muy)/std_devy)**2 - 2*r*((x-mux)/std_devx)*((y-muy)/std_devy))

    # calcoli della covarianza e r di l1, l2
    cov_xy = covariance_xy(l1, l2)
    r = cov_xy/(np.std(l1)*np.std(l2))
    valori_q2 = q2(r, l1, l2, mu1, mu2) 
    # bool per stabilire quali punti sono all'interno di 1
    punti_interni_bool = valori_q2 <= 1

    # filtra punti
    punti_interni_1 = l1[punti_interni_bool]
    punti_interni_2 = l2[punti_interni_bool]
    # plottare i punti
    axs[1,0].scatter(l1, l2, label="Tutti punti", s=1)
    axs[1,0].scatter(punti_interni_1, punti_interni_2, label=f"Punti Interni: {len(punti_interni_1)} \nRapporto: {len(punti_interni_1)/len(l1)*100}%", s=1)
    axs[1,0].axis('equal')
    axs[1,0].set_xlabel("Valori di L1 (m)")
    axs[1,0].set_ylabel("Valori di L2 (m)")
    axs[1,0].set_title("Plot L2 vs L1")

    # fisso valori per prob.condizionata
    valore_fissato = 0.0197
    tolleranza = 0.00005

    # filtro punti interni
    fascia_interna_bool = (valore_fissato - tolleranza <= l2) & (l2 <= valore_fissato + tolleranza)
    punti_fascia = l1[fascia_interna_bool]
    axs[1,0].axhline(y=valore_fissato, alpha=0.2, color = 'forestgreen', label=f"Valore Fissato:{valore_fissato}")
    axs[1,0].axhline(y=valore_fissato+tolleranza, alpha=0.2, color = 'purple', label=f"Limite Superiore: {valore_fissato+tolleranza}")
    axs[1,0].axhline(y=valore_fissato-tolleranza, alpha=0.2, color = 'purple', label=f"Limite Inferiore: {valore_fissato-tolleranza}")
    axs[1,0].legend()

    # plottare istogramma con errori
    counts, borders, _ = axs[1,1].hist(punti_fascia, bins=int(np.sqrt(len(punti_fascia))), edgecolor = 'k', label=f"Punti Interno Fascia {len(punti_fascia)}")
    centers = (borders[:-1] + borders[1:])/2
    bin_width = borders[1] - borders[0]
    centers_expected = gaussian_func(centers, mu1, std_dev) * len(punti_fascia) * bin_width
    errors = np.sqrt(counts)
    axs[1,1].plot(centers, centers_expected, label="Curva Aspettata")
    axs[1,1].errorbar(centers, counts, yerr=errors, fmt='none', elinewidth=1, capsize=2, color='red', alpha=0.6, label="Errori punti interni fascia")
    axs[1,1].set_title("Istogramma Punti Interno della Fascia (m())")
    axs[1,1].legend()
    axs[1,1].set_xlabel("Punti all'interno della fascia")
    axs[1,1].set_ylabel("Frequenza")

if __name__ == "__main__":
    initialize()
    calcolo_cov()
    plot.tight_layout()
    plot.show()