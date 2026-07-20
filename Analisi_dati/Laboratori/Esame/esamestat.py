import numpy as np
import matplotlib.pyplot as plot
from scipy.stats import chi2

fig, a = plot.subplots(nrows=2, ncols=2)
axs = a.flatten()

def Main():
    def distrib_esponenziale(x, tau):
        return np.exp(-x/tau)/tau
    
    def ln_likelihood(x, data):
        return -len(data) * np.log(x) - (np.sum(data)/x)

    data = np.loadtxt("conteggi_geiger_terraEtna_notte.txt")/1000
    # -------------------------------------------------------
    # Istogramma di Partenza
    # -------------------------------------------------------
    counts, bounds, _ = axs[0].hist(data, bins = 60, range=(0,20), edgecolor = 'k', label="Dati Misurati")
    axs[0].set(xlabel="Tempo Atteso (S)", ylabel="Eventi Rilevati", title="Istogramma dei Dati Misurati")
    # Errori per Istogramma 
    centers = (bounds[:-1] + bounds[1:])/2
    axs[0].errorbar(centers, counts, yerr=np.sqrt(counts), capsize=2, elinewidth=1, color='red', fmt='none', label="Errore")

    # calcolo tau_hat e varianza + strd dev
    tau_hat = np.sum(data)/float(len(data))
    std_dev_tau_hat = np.sqrt(tau_hat**2 / float(len(data)))
    print(f"Tau calcolo diretto dai dati: {tau_hat:.3f} \u00B1 {std_dev_tau_hat:.3f}")

    # Sovrapporre curva teorica
    axs[0].plot(bounds, distrib_esponenziale(bounds, tau_hat)*(bounds[1]-bounds[0]) * len(data), label="Curva Attesa")

    #--------------------------------------------------------
    # Test Pearson
    #--------------------------------------------------------
    expected_centers = distrib_esponenziale(centers, tau_hat) * (bounds[1] - bounds[0]) * len(data)
    mask_pearson = counts >= 5
    chi2_pearson = np.sum((counts[mask_pearson] - expected_centers[mask_pearson])**2/expected_centers[mask_pearson])
    # P-valu
    m = len(counts[mask_pearson])
    ndf = m - 1
    p_value = chi2.sf(chi2_pearson, ndf)
    if p_value > 0.05:
        print(f"Non possiamo rigettare l'ipotesi nulla: p-value={p_value:.3f}>{0.05}")
    if p_value < 0.05:
        print(f"Possiamo rigettare l'ipotesi nulla: p-value={p_value:.3f}<{0.05}")
    
    chi2_soglia = chi2.isf(0.05, ndf)
    if chi2_pearson > chi2_soglia:
        print(f"Chi2 misurato > chi2_soglia: {chi2_pearson:.4f} > {chi2_soglia:.4f}, rigettiamo l'ipotesi nulla.\n")
    if chi2_pearson < chi2_soglia:
        print(f"Chi2 misurato < chi2_soglia: {chi2_pearson:.4f} < {chi2_soglia:.4f}, non possiamo rigettare l'ipotesi nulla.\n")
    
    #--------------------------------------------------------
    # Maximum Likelihood
    #--------------------------------------------------------
    tau = np.linspace(tau_hat - 3*std_dev_tau_hat, tau_hat + 3*std_dev_tau_hat, 500000)
    ln_tau = ln_likelihood(tau, data)
    
    # Trovare l'indice che massimizza ln_tau, estrai prendi tau_max(x), e ln_tau_max(y)
    tau_max_index = np.argmax(ln_tau)
    tau_g= tau[tau_max_index]
    ln_tau_max = ln_tau[tau_max_index]
    
    # Definire threshold e si cercano tutti i punti sopra, prendiamo primo e ultimo indici dell'elemento che sono i primi punti dove siamo leggermente sopra
    threshold_index = np.where(ln_tau >= (ln_tau_max - 0.5))[0]
    tau_1_index = threshold_index[0]
    tau_2_index = threshold_index[-1]
    # usando l'indice estrai il valore
    tau_1 = tau[tau_1_index]
    tau_2 = tau[tau_2_index]

    # plot dei valori
    axs[1].plot(tau, ln_tau)
    axs[1].axhline(ln_tau_max, c='orange', linewidth=1, label=f"Tau_max: {tau_g:.3f}")
    axs[1].axvline(tau_g, c='orange', linewidth=1)
    axs[1].axhline(ln_tau_max - 0.5, c='#CA4D1F', label=f"Lmax-0.5: {ln_tau_max - 0.5:.3f}")
    axs[1].axvline(tau_1, c='#42D73D', label=f"Tau1,2: {tau_1:.3f}; {tau_2:.3f}")
    axs[1].axvline(tau_2, c='#42D73D')
    axs[1].set(xlabel=r"$\tau$", ylabel=r"$\ln \mathcal{L}(\tau)$", title="Grafico del Likelihood dei dati")
    print(f"Valore di tau usando ML grafico:{tau_g:.3f} \u00B1 {(tau_2-tau_1)/2:.3f}\n")

    #--------------------------------------------------------
    # Monte-Carlo
    #--------------------------------------------------------
    def funz_ripartizione(x):
        return -tau_hat*np.log(1-x)
    def gauss_func(x, mu, sigma):
        return 1/(np.sqrt((2*np.pi))*sigma) * np.exp(-(x-mu)**2/(2*sigma**2))

    # Avvia la simulazione
    medie_tau_hat = []
    for i in range(5000):
        data_esponenziale = funz_ripartizione(np.random.uniform(0,1,size=len(data)))
        medie_tau_hat.append(np.sum(data_esponenziale)/len(data_esponenziale))
    
    # Istogramma
    counts, bounds, _ = axs[2].hist(medie_tau_hat, bins=int(np.sqrt(5000)), edgecolor='k', label="Dati Misurati")
    centers = (bounds[:-1] + bounds[1:])/2
    bin_width = bounds[1] - bounds[0]
    axs[2].errorbar(centers, counts, yerr=np.sqrt(counts), fmt='none', elinewidth=1, color='red', capsize=2, label="Errore")

    # Calcolo media/deviazione strd sui dati generati + plot
    tau_MC = np.sum(medie_tau_hat)/len(medie_tau_hat)
    std_dev_MC = np.std(medie_tau_hat, ddof=1)
    print(f"Valore generato dalla simulazione Monte Carlo: {tau_MC:.3f} \u00B1 {std_dev_MC:.4f}\n")
    axs[2].plot(centers, gauss_func(centers, tau_MC, std_dev_MC) * bin_width * 5000, label="Curva Attesa")
    axs[2].set(xlabel = "Media Dati Generati", ylabel="Frequenza", title="Simulazione Monte-Carlo")

    print(f"Incertezza sigma_tau_hat:{std_dev_tau_hat:.5f}; sigma_MC:{std_dev_MC:.4f}")

    #--------------------------------------------------------
    # Trasformazione Inversa
    #--------------------------------------------------------
    u = 1-np.exp(-data/tau_hat)
    counts, bounds, _ = axs[3].hist(u,bins=60, range=(0,1), edgecolor='k', label="Dati Trasformati(u)")
    centers = (bounds[:-1] + bounds[1:])/2
    bin_width = bounds[1] - bounds[0]
    curva_attesa = len(data) * bin_width
    axs[3].axhline(curva_attesa, color='orange',linestyle='-', linewidth=2, label=f"Curva Attesa: y = {curva_attesa:.3f}")
    axs[3].set(xlabel =r"u = 1-exp(-t/$\hat{\tau}$)", ylabel="Eventi Rilevati", title = "Istogramma della trasformazione inversa")
    axs[3].errorbar(centers, counts, yerr=np.sqrt(counts), fmt='none', elinewidth=1, color='red', capsize=2, label="Errore")
    # Chi2 Pearson
    ni_i = np.full_like(counts, curva_attesa)
    mask_pearson = counts >= 5
    chi2_pearson = np.sum((counts[mask_pearson] - ni_i[mask_pearson])**2/ni_i[mask_pearson])
    m = len(ni_i[mask_pearson])
    ndf = m - 1
    p_value = chi2.sf(chi2_pearson, ndf)
    if p_value <= 0.05:
        print(f"Possiamo rigettare l'ipotesi nulla: i dati generati dalla trasformazione inversa non sono compatibili: {p_value:.3f} < 0.05")
    if p_value > 0.05:
        print(f"Non possiamo rigettare l'ipotesi nulla: i dati generati dalla trasformazione inversa sono compatibili: {p_value:.3f} > 0.05")

    for ax in axs:
        ax.legend()
    
    plot.show()

 
if __name__ == "__main__":
    Main()