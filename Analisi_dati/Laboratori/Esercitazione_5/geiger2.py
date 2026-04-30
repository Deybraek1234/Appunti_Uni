import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plot
import math

px = 1/plot.rcParams['figure.dpi']
fig, a = plot.subplots(nrows = 1, ncols = 3, figsize=[1900*px, 1000*px])
axs = a.flatten()
dati = np.loadtxt("gruppo2.txt")/1000

def Erlang(data_import):
    global media, dati
    def media(data):
        return np.sum(data)/len(data)

    def distrib_Erlang(t, l, k=2):
        return t**(k-1) * 1/math.factorial(k-1) * l**k * np.exp(-l*t)

    def ln_binned_likelihood(counts_bin, bin_centri, l, bin_width, N):
        ln_prob = np.log(distrib_Erlang(bin_centri, l) * bin_width * N)
        return np.sum(ln_prob * counts_bin)

    def binned_chi_sq(counts_bin, bin_centers, l, bin_width, N):
        prob = distrib_Erlang(bin_centers, l) * bin_width * N
        mask = counts > 0

        return np.sum((counts_bin[mask] - prob[mask])**2 / counts_bin[mask])


    if len(data_import) % 2 != 0:
        dati = data_import[:-1]
    else:
        dati = data_import

    # Distribuzione di Erlang
    erlang_dati = dati.reshape(-1,2).sum(axis=1)
    N = len(erlang_dati)
    lamb = 1/media(erlang_dati)

    counts, bounds, _ = axs[0].hist(erlang_dati, bins=160, edgecolor='k', label="Dati")
    errs = np.sqrt(counts)
    centers = (bounds[:-1] + bounds[1:])/2
    bin_width = bounds[1] - bounds[0]
    expected_centers = distrib_Erlang(centers,  lamb) * bin_width * N
    axs[0].plot(centers, expected_centers, label="Curva Aspettata")
    axs[0].errorbar(centers, expected_centers, yerr=errs, capsize=2, elinewidth=1, color='red')

    axs[0].set_xlabel("Tempo Atteso")
    axs[0].set_ylabel("Frequenza")
    axs[0].set_title("Histogramma Dati Misurati Geiger")
    axs[0].legend()


    # Binned Likelihood
    std_dev_lamb = np.sqrt(lamb**2/len(erlang_dati))
    x = np.linspace(lamb - 3*std_dev_lamb, lamb + 3*std_dev_lamb, N)
    ln_xL = np.array([ln_binned_likelihood(counts, centers, l, bin_width, N) for l in x])

    for i in range(len(x)-1):
        slope = ln_xL[i+1] - ln_xL[i]
        if (slope <= 0):
            lamb_max = x[i]
            ln_lamb_max = ln_xL[i]
            lamb_max_index = i
            break

    lamb_target = ln_latmb_max - 0.5
    saved_diff_1 = float("inf")
    saved_diff_2 = float("inf")
    lamb_1 = 0.0
    lamb_2 = 0.0
    for i in range(len(x)):
        temp_difference = np.abs(lamb_target - ln_xL[i])

        if (i<lamb_max_index): 
            if(temp_difference<saved_diff_1):
                saved_diff_1 = temp_difference
                lamb_1 = x[i]
        if(i>lamb_max_index):
            if (temp_difference < saved_diff_2):
                saved_diff_2 = temp_difference
                lamb_2 = x[i]

    axs[1].axhline(ln_lamb_max - 0.5, c='#CA4D1F', label="Lmax-0.5")
    axs[1].axvline(lamb_1, c="#42D73D")
    axs[1].axvline(lamb_2, c="#42D73D")
    axs[1].axvline(x=lamb_max, c='m', linewidth=1.0, label=f'Lamb_max: {lamb_max:.5f} \u00B1 {lamb - lamb_1}')
    axs[1].plot(x, ln_xL)

    axs[1].set_xlabel("Valori di Lambda")
    axs[1].set_ylabel("ln L(lambda)")
    axs[1].set_title("Metodo Maximum Likelihood")
    axs[1].legend()

    # chi_squared
    chi_sq_x = np.array([binned_chi_sq(counts, centers, l, bin_width, N) for l in x])

    lambda_min_index = np.argmin(chi_sq_x)
    lambda_min = x[lambda_min_index]
    chi_lamb_min = chi_sq_x[lambda_min_index]

    lamb_target = chi_lamb_min + 1

    for i in range(lambda_min_index, 0, -1):
        if chi_sq_x[i] > lamb_target:
            lambda_3 = x[i]
            break
    for i in range(lambda_min_index, len(x)):
        if chi_sq_x[i] > lamb_target:
            lambda_4 = x[i]
            break

    axs[2].axvline(lambda_min, c = "m", label="Lamb_min")
    axs[2].axhline(chi_lamb_min + 1, c = "#CA4D1F", label = "Lambda_min + 1")
    axs[2].axvline(lambda_3, c='#42D73D')
    axs[2].axvline(lambda_4, c='#42D73D')
    axs[2].plot(x, chi_sq_x)

    axs[2].set_xlabel("Valori di Chi Lamabd")
    axs[2].set_ylabel("Chi^2(Lambda)")
    axs[2].set_title ("Chi Quadro")
    axs[2].legend()

    mask = counts > 0
    chi_ridotto = chi_lamb_min/(len(counts[mask]) - 2)
    print(f"Chi Ridotto: {chi_ridotto}")

def Poisson(dati):
    delta_t = 30
    tcum = np.cumsum(dati)
    tmin = 0
    tmax = tcum[-1]

    w = np.arange(tmin, tmax, delta_t)

    if(tmax<w[-1]+delta_t):
        w = w[:-1]
    
    Poisson_counts = []
    for i in w:
        ind = np.where((tcum>i) & (tcum<=(i+delta_t)))
        Poisson_counts.append(len(tcum[ind]))

    counts, bounds, _ = axs[0].hist(Poisson_counts, bins=20, range=[0.5, 20.5], edgecolor='k')
    centers = (bounds[:-1] + bounds[1:])/2
    bin_width = bounds[1] - bounds[0]
    errors = np.sqrt(counts)

if __name__ == "__main__":
    #Erlang(dati)
    #plot.show()
    Poisson(dati)
    plot.show()