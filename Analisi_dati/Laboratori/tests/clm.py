import numpy.random as np
import numpy
import matplotlib.pyplot as plot

N = 1000

medie = []
for i in range(N):
    error_normal = np.uniform(1,8,100)
    error_binomial = np.normal(10,0.5,100)
    error_exponential = np.exponential(1,100)
    error_big = np.exponential(100)

    S = numpy.sum(error_normal) + numpy.sum(error_binomial) + numpy.sum(error_exponential) + error_big
    medie.append(S)

plot.hist(medie, bins=60, edgecolor='k')
plot.show()

