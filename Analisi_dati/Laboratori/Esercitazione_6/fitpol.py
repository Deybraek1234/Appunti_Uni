import scipy as sp
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import chi2
import matplotlib.pyplot as plot

#define functions
def f_lin(x, a0, a1):
    return a0 + a1*x

def f_quad(x, b0, b1, b2):
    return b0 + b1*x + b2*x**2

def f_terza(x, c0, c1, c2, c3):
    return c0 + c1*x + c2*x**2 + c3*x**3
    
def f_sett(x, d0, d1, d2, d3, d4, d5, d6, d7):
    return d0 + d1*x + d2*x**2 + d3*x**3 + d4*x**4 + d5*x**5 + d6*x**6 + d7*x**7

# gradi di libertà n-k (k sono quantità di parametri che usiamo per stimare)
def ndf(k):
    return 12 - k

# setup fig
fig, a = plot.subplots(nrows = 2, ncols = 2)
axs = a.flatten()
#load data
x = np.array([-4., -3.3, -2.5, -1.8, -1.1, -0.4, 0.4, 1.1, 1.8, 2.5, 3.3, 4.0])
y = np.array([21., 14., 12., 11., 3., 2., 7., 5., 3., 9., 10., 15.])
sigma_y = 3
# fit
popt_lin, pcov_lin = curve_fit(f_lin, x, y, sigma=sigma_y, absolute_sigma=True)
popt_quad, pcov_quad = curve_fit(f_quad, x, y, sigma=sigma_y, absolute_sigma=True)
popt_terza, pcov_terza = curve_fit(f_terza, x, y, sigma=sigma_y, absolute_sigma=True)
popt_sett, pcov_sett = curve_fit(f_sett, x, y, sigma=sigma_y, absolute_sigma=True)

# fare i plot
for i in range(4):
    axs[i].errorbar(x, y, yerr=sigma_y, fmt='.', marker='s', elinewidth = 2)
axs[0].plot(x, f_lin(x, popt_lin[0], popt_lin[1]))
axs[1].plot(x, f_quad(x, popt_quad[0], popt_quad[1], popt_quad[2]))
axs[2].plot(x, f_terza(x, popt_terza[0], popt_terza[1], popt_terza[2], popt_terza[3]))
axs[3].plot(x, f_sett(x, popt_sett[0], popt_sett[1], popt_sett[2], popt_sett[3], popt_sett[4], popt_sett[5], popt_sett[6], popt_sett[7]))

# chi**2
residui = y - f_lin(x, popt_lin[0], popt_lin[1])
chi2_lin = np.sum((residui/sigma_y)**2)

residui = y - f_quad(x, popt_quad[0], popt_quad[1], popt_quad[2])
chi2_quad = np.sum((residui/sigma_y)**2)

residui = y - f_terza(x, popt_terza[0], popt_terza[1], popt_terza[2], popt_terza[3])
chi2_terza = np.sum((residui/sigma_y)**2)

residui = y - f_sett(x, popt_sett[0], popt_sett[1], popt_sett[2], popt_sett[3], popt_sett[4], popt_sett[5], popt_sett[6], popt_sett[7])
chi2_sett = np.sum((residui/sigma_y)**2)
## confronto con chi_s
alpha = 0.05
chi2_lin_s = chi2.isf(alpha, 12 - len(popt_lin))
chi2_quad_s = chi2.isf(alpha, 12 - len(popt_quad))
chi2_terza_s = chi2.isf(alpha, 12 - len(popt_terza))
chi2_sett_s = chi2.isf(alpha, 12 - len(popt_sett))
rigettare = []
# check per rigettare
if (chi2_lin < chi2_lin_s):
    rigettare.append("no")
else:
    rigettare.append("si")

if (chi2_quad < chi2_quad_s):
    rigettare.append("no")
else:
    rigettare.append("si")

if (chi2_terza < chi2_terza_s):
    rigettare.append("no")
else:
    rigettare.append("si")

if (chi2_sett < chi2_sett_s):
    rigettare.append("no")
else:
    rigettare.append("si")
print(rigettare)
rigettare.clear()
# p-value
p_val_lin = chi2.sf(chi2_lin, len(popt_lin))
p_val_quad = chi2.sf(chi2_quad, len(popt_quad))
p_val_terza = chi2.sf(chi2_terza, len(popt_terza))
p_val_sett = chi2.sf(chi2_sett, len(popt_sett))
# check del p-value
if (p_val_lin > alpha):
    rigettare.append("no")
else:
    rigettare.append("si")

if (p_val_quad > alpha):
    rigettare.append("no")
else:
    rigettare.append("si")

if (p_val_terza > alpha):
    rigettare.append("no")
else:
    rigettare.append("si")

if (p_val_sett > alpha):
    rigettare.append("no")
else:
    rigettare.append("si")
print(rigettare)

# test f
f = ((chi2_quad - chi2_sett)/(8 - 3))/(chi2_sett/(12-8))
print(f"Valore di f: {f}")

plot.show()