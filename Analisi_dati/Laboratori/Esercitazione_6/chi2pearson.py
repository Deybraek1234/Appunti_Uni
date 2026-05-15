import numpy as np
import matplotlib.pyplot as plot
from scipy.stats import poisson
import scipy.special as sp
from scipy.stats import chi2

fig, a = plot.subplots(nrows=2, ncols=4)
axs = a.flatten()
data = np.loadtxt("dati/gruppo2.txt")/1000

def Erlang(dati):
    global media
    def media(data):
        return np.sum(data)/len(data)

    def distrib_Erlang(t, l):
        return t * l**2 * np.exp(-l*t)
    
    def ln_binned_likelihood(counts_bin, bin_centri, l, bin_width, N):
        prob = (distrib_Erlang(bin_centri, l) * bin_width * N)
        mask = prob > 0
        ln_prob = np.log(prob[mask])
        return np.sum(ln_prob * counts_bin[mask])

    def binned_chi_sq(counts_bin, bin_centers, l, bin_width, N):
        prob=distrib_Erlang(bin_centers, l) * bin_width * N
        mask = counts_bin>0
        return np.sum((counts_bin[mask] - prob[mask])**2 / counts_bin[mask])

     
    if (len(dati)) % 2 != 0:
        dati = dati[:-1]
    
    dati = dati.reshape(-1,2).sum(axis=1)
    N = len(dati)
    lamb = 2/media(dati)
    std_dev_lamb = np.sqrt(lamb**2/len(dati))

    # Distrib Erlang
    counts, bounds, _ = axs[0].hist(dati, bins=160, edgecolor='k', label='Dati')
    centers = (bounds[:-1] + bounds[1:])/2
    bin_width = bounds[1] - bounds[0]
    axs[0].plot(centers, distrib_Erlang(centers, lamb)* bin_width * N, label="Curva Aspettata")
    axs[0].errorbar(centers, distrib_Erlang(centers, lamb) * bin_width * N, yerr = np.sqrt(counts), capsize=2, elinewidth=1, color='red')

    axs[0].set_xlabel("Tempo Atteso")
    axs[0].set_ylabel("Frequenza")
    axs[0].set_title("Histogramma Dati Misurati Geiger")
    axs[0].legend()

    # Likelihood
    x = np.linspace(lamb - 3*std_dev_lamb, lamb + 3*std_dev_lamb, len(counts))
    lnL_x = np.array([ln_binned_likelihood(counts, centers, l, bin_width, N) for l in x])
    
    lamb_max_index = np.argmax(lnL_x)
    lamb_max = x[lamb_max_index]
    lnL_lamb_max = lnL_x[lamb_max_index]

    above_threshold_index = np.where(lnL_x >= (lnL_lamb_max - 0.5) )[0]
    lamb_1_index = above_threshold_index[0]
    lamb_2_index = above_threshold_index[-1]

    lamb_1 = x[lamb_1_index]
    lamb_2 = x[lamb_2_index]

    axs[1].plot(x, lnL_x)
    axs[1].axhline(lnL_lamb_max, c='m', linewidth=1.0, label=f"Lamb_max: {lamb_max}")
    axs[1].axhline(lnL_lamb_max - 0.5, c='#CA4D1F', label="Lmax-0.5")
    axs[1].axvline(lamb_1, c='#42D73D')
    axs[1].axvline(lamb_2, c='#42D73D')

    axs[1].set_xlabel("Valori di Lambda")
    axs[1].set_ylabel("ln L(Lambda)")
    axs[1].set_title("Metodo Maximum Likelihood")
    axs[1].legend()

    # chi_squared
    chisq_x = np.array([binned_chi_sq(counts, centers, l, bin_width, N) for l in x])
    global lamb_min_erlang
    chisq_min_index = np.argmin(chisq_x)
    lamb_min_erlang = x[chisq_min_index]
    chisq_min = chisq_x[chisq_min_index]

    below_threshold_index = np.where(chisq_x <= (chisq_min + 1))[0]
    lamb_3_index = below_threshold_index[0]
    lamb_4_index = below_threshold_index[-1]

    lamb_3 = x[lamb_3_index]
    lamb_4 = x[lamb_4_index]
    
    axs[2].plot(x, chisq_x)
    axs[2].axhline(chisq_min, c = 'm', label=f"Lamb_min: {lamb_min_erlang}")
    axs[2].axhline(chisq_min + 1, c="#CA4D1F", label="Lambda_min + 1")
    axs[2].axvline(lamb_3, c='#42D73D')
    axs[2].axvline(lamb_4, c='#42D73D')

    print(f"Chi Ridotto {chisq_min/(len(counts[counts>0])-2)}")
    # esercitazione 8
    nu_i = distrib_Erlang(centers, lamb_min_erlang,) * bin_width * N
    mask_pearson = (nu_i > 0) & (counts > 0)
    chi2_pearson = np.sum((counts[mask_pearson] - nu_i[mask_pearson])**2 / nu_i[mask_pearson])
    m_bins = np.sum(mask_pearson)
    ndf = m_bins - 2
    alpha = 0.05
    chi2_soglia = chi2.isf(alpha, ndf)
    if chi2_pearson > chi2_soglia:
        print("Rigettiamo")
    else:
        print("Non Rigettiamo")

    p_value = chi2.sf(chi2_pearson, ndf)
    if p_value < alpha:
        print("Rigettiamo")
    else: 
        print("Non Rigettiamo")

def Poisson(dati):
    def ln_binned_likelihood(counts_bin, bin_centri, l, bin_width, N):
        prob = (poisson.pmf(bin_centri, l)) * bin_width * N
        mask = prob>0
        ln_prob = np.log(prob[mask])
        return np.sum(ln_prob*counts_bin[mask])
    def binned_chi_sq(counts_bin, bin_centers, l, bin_width, N):
        prob= poisson.pmf(bin_centers, l) * N
        mask = counts_bin>0
        return np.sum((counts_bin[mask] - prob[mask])**2 / counts_bin[mask])

    delta_t = 30
    tcum = np.cumsum(dati)
    tmax = tcum[-1]

    w = np.arange(0, tmax, delta_t)

    if(tmax<w[-1]+delta_t):
        w = w[:-1]

    bin_edges = np.append(w, w[-1] + delta_t)
    dati, _ = np.histogram(tcum, bins=bin_edges)
    dati = dati.tolist()
    l=1/np.sum(dati)
    N = len(data)

    counts, bounds, _ = axs[3].hist(dati, bins=20, range=[0.5, 20.5], edgecolor = 'k')
    centers = (bounds[:-1] + bounds[1:])/2
    bin_width = bounds[1] - bounds[0]

    lamb_hat = np.sum(dati)/len(dati)
    std_dev_lamb = np.sqrt(lamb_hat/len(dati))
    axs[3].plot(centers, poisson.pmf(centers, lamb_hat) * len(dati), label="Curva Attesa")
    axs[3].legend()

    # Likelihood
    x = np.linspace(lamb_hat - 3*std_dev_lamb, lamb_hat + 3*std_dev_lamb, len(counts))
    lnL_x = np.array([ln_binned_likelihood(counts, centers, l, bin_width, N) for l in x])

    lamb_max_index = np.argmax(lnL_x)
    lamb_max = x[lamb_max_index]
    lnL_lamb_max = lnL_x[lamb_max_index]

    above_threshold_index = np.where(lnL_x >= (lnL_lamb_max - 0.5))[0]
    lamb_1_index = above_threshold_index[0]
    lamb_2_index = above_threshold_index[-1]

    lamb_1 = x[lamb_1_index]
    lamb_2 = x[lamb_2_index]

    axs[4].plot(x, lnL_x)
    axs[4].axhline(lnL_lamb_max, c='m', linewidth = 1.0, label=f'Lamb_max: {lamb_max}')
    axs[4].axhline(lnL_lamb_max - 0.5, c='#CA4D1F', label = "Lmax-0.5")
    axs[4].axvline(lamb_1, c='#42D73D')
    axs[4].axvline(lamb_2, c='#42D73D')

    axs[4].set_xlabel("Valori di Lambda")
    axs[4].set_ylabel("ln L(Lambda)")
    axs[4].set_title("Metodo Maximum Likelihood")
    axs[4].legend()

    # Chi sq
    chisq_x = np.array([binned_chi_sq(counts, centers, l, bin_width, len(dati)) for l in x])
    global lamb_min_poisson
    chisq_min_index = np.argmin(chisq_x)
    lamb_min_poisson = x[chisq_min_index]
    chisq_min = chisq_x[chisq_min_index]

    below_threshold_index = np.where(chisq_x <= (chisq_min + 1))[0]
    lamb_3_index = below_threshold_index[0]
    lamb_4_index = below_threshold_index[-1]

    lamb_3 = x[lamb_3_index]
    lamb_4 = x[lamb_4_index]

    axs[5].plot(x, chisq_x)
    axs[5].axhline(chisq_min, c='m', label=f"Lamb_min: {lamb_min_poisson}")
    axs[5].axhline(chisq_min + 1, c="#Ca4D1F", label="Lambda_min + 1")
    axs[5].axvline(lamb_3, c="#42D73D")
    axs[5].axvline(lamb_4, c="#42D73D")

    print(f"Chi Ridotto {chisq_min/(len(counts[counts>0]) - 2 )}")
    print(f"Rapporto: {np.sqrt(2* (chisq_min/(len(counts[counts>0])-2)) / np.sqrt(2*2-1))}")

    # Esercitazione 6
    N_poisson = len(dati)
    nu_i_poisson = poisson.pmf(centers, lamb_min_poisson) * N_poisson
    mask_pearson_p = (nu_i_poisson > 0) & (counts > 0)
    chi2_pearson_p = np.sum((counts[mask_pearson_p] - nu_i_poisson[mask_pearson_p])**2 / nu_i_poisson[mask_pearson_p])
    m_bins_p = np.sum(mask_pearson_p)
    ndf_p = m_bins_p - 2
    alpha = 0.05
    chi2_soglia_p = chi2.isf(alpha, ndf_p)
    if chi2_pearson_p > chi2_soglia_p:
        print("Rigettiamo L'ipotesi")
    else:
        print("Non Rigettiamo l'ipotesi")

    p_value_p = chi2.sf(chi2_pearson_p, ndf_p)
    if p_value_p < alpha:
        print("Rigettiamo L'ipotesi")
    else:
        print("Non Rigettiamo l'ipotesi")


if __name__ == "__main__":
    Erlang(data)
    Poisson(data)
    plot.show()
