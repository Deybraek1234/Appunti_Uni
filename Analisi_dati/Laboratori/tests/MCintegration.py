import numpy.linalg
import numpy as np
import matplotlib.pyplot as plot
from matplotlib.animation import FuncAnimation

fig, ax = plot.subplots()

def f(x):
    if(numpy.linalg.norm(x) < 1):
        result = 1
    else:
        result = 0
    return result

n=100
results = []

x=[]
y=[]
scatter, = ax.plot([], [], 'bo', label="Dati Generati")
ax.set_xlim=(-1,1)
ax.set_ylim=(-1,1)


def update(frame):
    x.append(numpy.random.uniform(-1,1,1))
    y.append(numpy.random.uniform(-1,1,1))

    scatter.set_data(x,y)
    return x, y


area = 4/n*np.sum(results)
print(area)

animation = FuncAnimation(fig, update, interval=1)
plot.show()