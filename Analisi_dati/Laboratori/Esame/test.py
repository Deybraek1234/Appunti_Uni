import numpy as np

# 1. Read the data from the text file
# Make sure the text file is in the same directory or provide the correct path
dati_ms = np.loadtxt("conteggi_geiger_terraEtna_notte.txt")

# 2. Convert the data from milliseconds to seconds
dati_s = dati_ms / 1000.0

# 3. Get the number of events (N)
N = len(dati_s)

# 4. Calculate Expected Value (tau_hat) using Maximum Likelihood
tau_hat = np.mean(dati_s)

# 5. Calculate Variance and Standard Deviation
var_tau = (tau_hat ** 2) / N
sigma_tau = np.sqrt(var_tau)

# 6. Print the results formatted properly
print(f"Number of events (N): {N}")
print(f"Expected Value (\u03C4\u0302): {tau_hat:.4f} seconds")
print(f"Variance: {var_tau:.6f} seconds\u00B2")
print(f"Result: {tau_hat:.4f} \u00B1 {sigma_tau:.4f} seconds")