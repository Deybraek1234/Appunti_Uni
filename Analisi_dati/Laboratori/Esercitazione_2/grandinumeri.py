import math
import numpy as np
import matplotlib.pyplot as plot

px = 1/plot.rcParams['figure.dpi']
N = 1000
fig, axs = plot.subplots(nrows=3, ncols = 2, figsize=(1900*px, 1000*px))

numbers = []
for i in range(N):
    numbers.append(i)

def Main():
    Distrib_uniforme_grafico()
    Distrib_esponenziale_grafico()
    Distrib_cauchy_grafico()

def Distrib_uniforme_grafico():
    nbins = 10
    data = []

    data = np.random.uniform(0,1,N)
    _ , borders, _  = axs[0,0].hist(data,bins=nbins,edgecolor = 'k')
    centers = (borders[:-1] + borders[1:])/2
    axs[0,0].plot(centers, np.full(nbins, N/nbins), 'o', label = "Distribuzione Uniforme")
    axs[0,0].set_title("Distribuzione Uniforme")

    medie = []
    for i in range(N):
        medie.append(np.sum(data[:i]/i))
    
    #plot delle misure
    axs[0,1].plot(numbers, medie)
    #plot della riga
    axs[0,1].plot(numbers, np.full(N,0.5))
    axs[0,1].set_title("Convergenza Media Distribuzione Uniforme")

def Distrib_esponenziale_grafico():
    nbins = 60
    data = []
    def funz_ripartizione(u):
        tau = 5
        return (-tau*np.log(1-u))
    def funz_esponenziale(x):
        tau = 5
        return(np.exp(-x/tau)/tau)

    data = np.array(np.random.uniform(0,1,N))
    esponenziale = np.array(funz_ripartizione(data))

    counts, borders, _ = axs[1,0].hist(esponenziale, bins = nbins, range=[0,30])
    
    centers = (borders[:-1] + borders[1:])/2
    bin_width = borders[1]-borders[0]
    centers_esponenziale = funz_esponenziale(centers)* bin_width * N

    axs[1,0].plot(centers, centers_esponenziale, 'o')
    axs[1,0].set_title("Distribuzione Esponenziale")

    medie = []
    for i in range(N):
        medie.append(np.sum(esponenziale[:i]/i))
    axs[1,1].plot(numbers, medie)
    axs[1,1].plot(numbers, np.full(N, 5))
    axs[1,1].set_title("Convergenza Media Distribuzione Esponenziale")

def Distrib_cauchy_grafico():
    nbins = 50
    punti_1 = np.random.normal()
    punti_2 = np.random.normal()

    distrib_cauchy = np.divide(punti_1, punti_2)
    axs[2,0].hist(distrib_cauchy, bins=nbins, range=[-5,5], edgecolor='k')
        


if __name__ == "__main__":
    Main()
    plot.show()