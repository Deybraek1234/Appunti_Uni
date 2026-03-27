import matplotlib.pyplot as plot
import numpy as np

from matplotlib import cm
from matplotlib.widgets import Slider
from matplotlib.colors import LightSource

fig, axs = plot.subplots(subplot_kw=dict(projection='3d'))
def Main():
    x = np.linspace(-4,4,1000)
    y = np.linspace(-4,4,1000)
    x_points, y_points = np.meshgrid(x,y)

    z = gauss(x_points, y_points)

    ls = LightSource(270, 45)

    rgb = ls.shade(z, cmap = cm.gist_earth, blend_mode='soft')
    axs.plot_surface(x_points, y_points, z, facecolors = rgb, shade = False)
    fig.subplots_adjust(bottom = 0.25)
    axheight = fig.add_axes([0.025, 0.1, 0.65, 0.03])
    height_slider = Slider(ax=axheight, label = "Height" , valmin = 0.1, valmax = 20, valinit=1)
    
    height_slider.on_changed(update(x_points, y_points))

    plot.show()

def gauss(x,y, height = 1):
    return (np.exp(-x**2 -y**2)/(2*np.pi*height))

def update(x_points, y_points):
    axs.plot_surface(x_points, y_points, gauss(x_points, y_points))
    fig.canvas.draw_idle()

if __name__ == "__main__":
    Main()