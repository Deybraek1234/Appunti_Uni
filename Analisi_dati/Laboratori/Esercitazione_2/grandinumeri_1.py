import numpy as np
import matplotlib.pyplot as plot

px = 1/plot.rcParams['figure.dpi']
N = 1000
fig, axs = plot.subplots(nrows=3, ncols = 2, figsize=(1900*px, 1000*px))

def Main():
    Distrib_uniforme_grafico()
    Distrib_esponenziale_grafico()
    Distrib_cauchy_grafico()

def Media(data):
    medie = []
    for i in range(N):
        medie.append(np.sum(data[:i]/i))
    return medie

def Distrib_uniforme_grafico():
    nbins = 10

    #generate random numbers following uniform distribution
    data_uniforme = np.random.uniform(0,1,N)

    # plot histogram
    _ , borders, _  = axs[0,0].hist(data_uniforme, bins=nbins, edgecolor = 'k')
    #calculate centers
    centers = (borders[:-1] + borders[1:])/2
    #plot histogram
    axs[0,0].plot(centers, np.full(nbins, N/nbins), label = "Distribuzione Uniforme")

    #calcula media per i dati
    medie = Media(data_uniforme)

    #plot delle medie
    axs[0,1].plot(medie)
    #plot del valore di aspettazione
    axs[0,1].plot(np.full(N,0.5))

    axs[0,0].set_title("Distribuzione Uniforme")
    axs[0,1].set_title("Convergenza Media Distribuzione Uniforme")

def Distrib_esponenziale_grafico():  
    # definizione funzioni di ripartizione per generazione e funz_esponenziale per calcolo effettivo  
    tau = 5
    def funz_ripartizione(u):
        return (-tau*np.log(1-u))
    def funz_esponenziale(x):
        return(np.exp(-x/tau)/tau)
    
    nbins = 60
    
    # generate data for exponential funciton
    data_esponenziale = (funz_ripartizione(np.random.uniform(0,1,N)))

    # generate histogram
    _, borders, _ = axs[1,0].hist(data_esponenziale, bins = nbins, range=[0,30], edgecolor = 'k')
    
    #calculate centers and bin_width to scale histogram
    centers = (borders[:-1] + borders[1:])/2
    bin_width = borders[1]-borders[0]
    expected_value_centers = funz_esponenziale(centers)* bin_width * N

    # Plot curva aspettata
    axs[1,0].plot(centers, expected_value_centers)

    # Calcolo del vettore delle medie
    medie = Media(data_esponenziale)

    # Plot della convergenza delle medie
    axs[1,1].plot(medie)
    axs[1,1].plot(np.full(N, tau))

    axs[1,1].set_title("Convergenza Media Distribuzione Esponenziale")
    axs[1,0].set_title("Distribuzione Esponenziale")

def Distrib_cauchy_grafico():
    # Definizione della distribuzione di Cauchy
    def distrib_cauchy(x):
        return(1/(np.pi) * 1/(x**2 + 1))

    nbins = 50

    # Initialize array with data following Cauchy Distribution
    data_cauchy = np.divide(np.random.normal(size = N), np.random.normal(size = N))
    _, borders, _ = axs[2,0].hist(data_cauchy, bins=nbins, range=[-5,5], edgecolor='k')

    #calculate centers/bin_width
    centers = (borders[:-1] + borders[1:])/2
    bin_width = borders[1] - borders[0]

    # calculate centers expected values and plot them
    expected_value_centers = distrib_cauchy(centers)*bin_width*N
    axs[2,0].plot(centers, expected_value_centers)

    # Calcolo del vettore della media + plot, non esiste valore aspettato
    medie = Media(data_cauchy)
    axs[2,1].plot(medie)

    axs[2,0].set_title("Distribuzione di Cacuhy")
    axs[2,1].set_title("Media della Distribuzione di Cauchy")

if __name__ == "__main__":
    Main()
    plot.legend()
    plot.show()