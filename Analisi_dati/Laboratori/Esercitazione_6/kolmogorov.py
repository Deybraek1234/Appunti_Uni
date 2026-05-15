import numpy as np
import matplotlib.pyplot as plot
from scipy.stats import ks_2samp


fig, a = plot.subplots(nrows = 1, ncols = 2)
axs = a.flatten()

n=1000
da1= np.loadtxt("dati/gruppo1.txt", max_rows = n)
da2 = np.loadtxt("dati/gruppo2.txt", max_rows = n)

dati1 = np.sort(da1)
dati2 = np.sort(da2)

y_fc_1 = np.arange(1, n+1) / n
y_fc_2 = np.arange(1, n+1) / n

axs[0].step(dati1, y_fc_1, where='post', label='Frequenza cumulativa empirica')
axs[0].step(dati2, y_fc_2, where='post', label='Frequenza cumulativa empirica')

D, pvalue = ks_2samp(dati1,dati2)

if (pvalue < 0.05):
    print("Non sono compatibili")
else:
    print("Sono compatibili")

plot.show()