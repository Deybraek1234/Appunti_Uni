import numpy as np

data = np.random.uniform(0,1,1000)
n, data = np.histogram(data, bins=10)

print(f"{n}")