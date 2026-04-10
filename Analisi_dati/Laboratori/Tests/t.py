import functions as f
import numpy as np
import matplotlib.pyplot as plot

x = np.random.normal(size = 10000)


configs = [
    {
        "type":"histogram",
        "data":{"x": x},
        "config":{"nbins": 80, "fit": [True, "gaussian"]}
    },

]

f.plot_grid(configs)
plot.show()