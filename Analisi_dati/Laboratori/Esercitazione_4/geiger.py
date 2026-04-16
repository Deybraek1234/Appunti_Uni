import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plot
import math

px = 1/plot.rcParams['figure.dpi']
fig, a = plot.subplots(nrows = 1, ncols = 3, figsize=[1900*px, 1000*px])
axs = a.flatten()
dati = np.loadtxt("gruppo2.txt")/1000

def likelihood_calcolo():
    def esponenziale(x, tau):
        return np.exp(-x/tau)/tau

    global tau_hat, std_dev_tau_bar
    tau_hat = np.sum(dati)/len(dati)
    std_dev_tau_bar = np.sqrt(tau_hat**2/len(dati))
    print(f"Valore Calcolato: {tau_hat:.3f} \u00B1 {std_dev_tau_bar:.3f}")

    counts, bounds, _ = axs[0].hist(dati, bins=int(np.sqrt(len(dati))), edgecolor = 'k', label="Dati")
    errs = np.sqrt(counts)
    centers = (bounds[:-1] + bounds[1:])/2
    bin_width = bounds[1] - bounds[0]
    expected_centers = esponenziale(centers, tau_hat) * bin_width * len(dati)
    axs[0].plot(centers, expected_centers, label="Curva Aspettata")
    axs[0].errorbar(centers, expected_centers, yerr=errs, capsize=2, elinewidth=1, color='red')

    axs[0].set_xlabel("Tempo Atteso")
    axs[0].set_ylabel("Frequenza")
    axs[0].set_title("Histogramma Dati Misurati Geiger")
    axs[0].legend()
    
def likelihood_grafico():
    def lnlikelihood(t):
        return -len(dati) * np.log(t) - (np.sum(dati)/t)
    
    tau = np.linspace(tau_hat - 3*std_dev_tau_bar, tau_hat + 3*std_dev_tau_bar, 10000)
    ln_tau = lnlikelihood(tau)
    # Per trovare max, in questo modo, il numero di dati generati con tau determina accuratezza
    for i in range(len(tau)):
        slope = ln_tau[i+1] - ln_tau[i]
        if (slope <= 0):
            tau_max = tau[i]
            tau_max_index = i
            break


    tau_target = lnlikelihood(tau_max) - 0.5
    saved_diff_1 = float("inf")
    saved_diff_2 = float("inf")
    tau_1= 0.0
    tau_2 = 0.0
    # for looop to find ln_max - 0.5
    for i in range(len(tau)):
        temp_difference = np.abs(tau_target - ln_tau[i])

        if (i < tau_max_index):
            if (temp_difference < saved_diff_1):
                saved_diff_1 = temp_difference
                tau_1 = tau[i]
            
        if(i > tau_max_index):
            if(temp_difference < saved_diff_2):
                saved_diff_2 = temp_difference
                tau_2 = tau[i]

    sigma_tau_hat = tau_hat - tau_1
    print(f"Valore Grafico: {tau_max:.3f} \u00B1 {sigma_tau_hat:.3f}")

    axs[1].axhline(lnlikelihood(tau_max)-0.5, c='#CA4D1F', label="Lmax-0.5")
    axs[1].axvline(tau_1, c="#42D73D")
    axs[1].axvline(tau_2, c='#42D73D')

    axs[1].plot(tau, ln_tau)
    axs[1].axvline(x=tau_max, c='m', linewidth=1.0, label=f'Tau_max: {tau_max:.5f}')
    
    axs[1].set_xlabel("Valori di Tau")
    axs[1].set_ylabel("ln L(tau)")
    axs[1].set_title("Metodo Maximum Likelihood")
    axs[1].legend()

def Monte_Carlo():
    def funz_ripartizione(u):
        return(-tau_hat*np.log(1-u))
    def gauss_func(x, mu, sigma):
        return 1/(np.sqrt((2*np.pi))*sigma) * np.exp(-(x-mu)**2/(2*sigma**2))
    
    medie_tau_hat = []
    for i in range(5000):
        data_esponenziale = funz_ripartizione(np.random.uniform(0,1, size=len(dati)))
        medie_tau_hat.append(np.sum(data_esponenziale)/len(data_esponenziale))

    counts, bounds, _ = axs[2].hist(medie_tau_hat, bins=int(np.sqrt(5000)), edgecolor='k')
    errs = np.sqrt(counts)
    bin_width = bounds[1] - bounds[0]
    centers = (bounds[:-1] + bounds[1:])/2
    tau_MC = np.sum(medie_tau_hat)/len(medie_tau_hat)
    std_dev_MC = np.std(medie_tau_hat)
    
    print(f"Valore Monte Carlo {tau_MC:.3f} \u00B1 {std_dev_MC:.3f}")
    expected_centers = gauss_func(centers, tau_MC, std_dev_MC) * bin_width * 5000
    axs[2].errorbar(centers, counts, yerr=errs, fmt='none', elinewidth=1, color='red', capsize=2)
    axs[2].plot(centers, expected_centers, label="Gaussiana")
    axs[2].legend()

if __name__ == "__main__":
    likelihood_calcolo()
    likelihood_grafico()
    Monte_Carlo()
    plot.show()
