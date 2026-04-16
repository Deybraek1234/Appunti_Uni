import matplotlib.pyplot as plot
import numpy as np
import sys
import math

# Distributions
def distrib_uniforme(n_amount, lower_bound = 0, upper_bound = 1):
    data = np.random.uniform(lower_bound, upper_bound ,n_amount)
    return (data)

def funz_esponenziale_l(x, l = 1):
    return l*np.exp(-x*l)

def funz_esponenziale_tau(x, t = 1):
    return np.exp(-x/t)/t

def gaussian_func(x, mu = 0, std_dev = 1):
    return 1/(np.sqrt(2*np.pi)*std_dev) * np.exp(-((x-mu)**2)/(2*std_dev**2))


# Operations
def media(data):
    return np.sum(data)/len(data)

# varianza con correzione bessel
def varianza(data):
    media = np.sum(data)/len(data)
    return 1/len(data-1) * np.sum((data-media)**2)

def std_dev(data):
    return np.sqrt(varianza(data))

def covariance_xy(x,y):
    if (len(x) == len(y)):
        x_mean = np.sum(x)/len(x)
        y_mean = np.sum(y)/len(y)
        return np.sum((x-x_mean)*(y-y_mean))/(len(x)-1)
    
    elif(len(x) != len(y)):
        print(f"Arrays not the same length: lenx = {len(x)}, leny = {len(y)}")
        sys.exit(1)


# Function to plot single graphs
px = 1/plot.rcParams['figure.dpi']
def plot_graph_single_axis(axs, plot_config, is_overlay):
    # read all data data, in brackets[] obligatori, .get() optional
    plot_type = plot_config["type"].lower()
    data = plot_config["data"]
    x_data = data.get("x", [])
    y_data = data.get("y", [])
    #dynamic label
    label_name = plot_config.get("name" if is_overlay else "Base Data")

    errors = plot_config.get("errors", {})
    xerr = errors.get("xerr", None)
    yerr = errors.get("yerr", None)

    titles = plot_config.get("titles", {})
    # take plot_type and plot accordingly
    if plot_type == "graph":
        axs.errorbar(x_data, y_data, xerr=xerr, yerr=yerr, fmt='-o', capsize=5, label=label_name)
    elif plot_type == "histogram":
        hist_config = plot_config.get("config", {})
        range = hist_config.get("range", None)
        nbins = hist_config.get("nbins", 'auto')
        counts, bounds, _ = axs.hist(x_data, bins=nbins, edgecolor='black', alpha=0.8, label='Frequencies', range=range)
        centers = (bounds[:-1] + bounds[1:])/2
        bin_width = bounds[1] - bounds[0]
        axs.errorbar(centers, counts, yerr=yerr, fmt='none', elinewidth=1, capsize=2, color='red', alpha=0.6, label=label_name)
        # fit function if asked for
        fit = hist_config.get("fit", [False, None])
        # add more expected curves
        if fit[0] == True:
            fit_func = fit[1]
            match fit_func:
                case "gaussian":
                    mu = hist_config.get("mu", 0)
                    sigma = hist_config.get("sigma", 1)
                    y = gaussian_func(centers, mu, sigma)
                case "exponential_tau":
                    tau = hist_config.get("tau", 1)
                    y = funz_esponenziale_tau(centers, tau)


            y = y * bin_width * len(x_data)
            axs.plot(centers, y, label="Curva Aspettata")

    elif plot_type == "scatter":
        axs.scatter(x_data, y_data, label='Data Points', s=1)
    else:
        raise ValueError(f"Unspported plot type: '{plot_type}'")
    
    # overlay logic
    if not is_overlay:
        axs.set_title(titles.get("main", "Default Title"), fontsize = 12)
        axs.set_xlabel(titles.get("x", "X-Axis"), fontsize=10)
        axs.set_ylabel(titles.get("y", "Y-Axis"), fontsize=10)
    else:
        if "main" in titles: axs.set_title(titles["main"], fontsize=12)
        if "x" in titles: axs.set_xlabel(titles["x"], fontsize=10)
        if "y" in titles: axs.set_ylabel(titles["y"], fontsize=10)

    axs.legend(fontsize=8)
    axs.grid(True, linestyle='--', alpha=0.6)

# Function to plot graphs in multiple layers
def plot_grid(plot_configs):
    if not plot_configs:
        print("No Configurations provided")
        return

    num_subplots = 0
    for i, config in enumerate(plot_configs):
        if i == 0 or not config.get("overlay", False):
            num_subplots += 1

    ncols = int(math.ceil(math.sqrt(num_subplots)))
    nrows = int(math.ceil(num_subplots/ncols)) if ncols > 0 else 0

    fig, axs = plot.subplots(nrows=nrows, ncols=ncols, figsize=[1900*px, 1000*px], squeeze=False)
    axes_flat = axs.flatten()

    axs_index = -1
    for i, config in enumerate(plot_configs):
        is_overlay = config.get("overlay", False)
        if i == 0 or not is_overlay:
            axs_index += 1
        
        ax = axes_flat[axs_index]
        plot_graph_single_axis(ax, config, is_overlay)

    for i in range(axs_index + 1, len(axes_flat)):
        axes_flat[i].set_visible(False)
        
    plot.tight_layout()
    return fig, axs

# Example
# configs = [
#   {
#       "type": "graph", (required)
#       "data":{"x": x_vals, "y":y_vals} (required)
#       "errors":{"xerrs": x_error_bars, "yerrs": y_error_bars} (not required)
#       "titles":{"main": "Main Title", "x": "x_label", "y": "y_label"} (not, required)
#   },
#   {
#       "type": "histogram", (required)
#       "data": {"x": x_vals}, (required)
#       "errors":{"yerrs":y_errors} (not required)
#       "titles":{"main": "Histogram Title", "x": "X-Axis", "y":"Y-Axis"} (not required)
#       "config":{"nbins": number_bins, "fit":[True/false, fit_func], (for fit func input parameters, such as gaussian: "mu":mu, "sigma":sigma), and exponential_tau "tau": tau} (not required)
#   },
#   {
#       "type":"scatter",(required)
#       "data": {"x": x_vals, "y": y_vals}, (required)
#       
#   }
# ]
# !!!REQUIRES PLOT.SHOW AFTER!!!2