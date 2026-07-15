import numpy.random
import numpy as np
import matplotlib.pyplot as plot
from matplotlib.animation import FuncAnimation

fig, ax = plot.subplots()

line_normal, = ax.plot([], [], label="Normal Mean(Converges to 0)", linewidth=2)
line_cauchy, = ax.plot([], [], label="Cauchy Mean", linewidth=2, alpha=0.8)

plot.axhline(0, color="forestgreen")

n_samples=[]
normal_data=[]
cauchy_data=[]
normal_means=[]
cauchy_means=[]

def init():
    ax.set_xlim(0,50)
    ax.set_ylim(-5,5)
    return line_normal, line_cauchy

def update(frame):
    n = frame+1
    n_samples.append(n)

    normal_data.append(np.random.standard_normal())
    cauchy_data.append(np.random.standard_cauchy())

    normal_means.append(np.mean(normal_data))
    cauchy_means.append(np.mean(cauchy_data))

    line_normal.set_data(n_samples, normal_means)
    line_cauchy.set_data(n_samples, cauchy_means)

    if n > 45:
        ax.set_xlim(0, n+10)
    
    current_max = max(max(cauchy_means), max(normal_means))
    current_min = min(min(cauchy_means), min(normal_means))

    y_upper = max(5, current_max + 2)
    y_lower = min(-5, current_min - 2)
    ax.set_ylim(y_lower, y_upper)
    return line_normal, line_cauchy

ani=FuncAnimation(fig, update, init_func = init, blit=False, interval=1, repeat=False)

plot.legend()
plot.tight_layout()
plot.show()