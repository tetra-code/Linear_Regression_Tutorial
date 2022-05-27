import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm

# use kernel density estimate to approximate density function of X values


# plots the kernel density based on the value array specifics of minimum and maximum values
# note that depending on the value distribution, plot may not be centered or most balanced looking
def plot_kernel_density_estimate(n, bin, array, x_space):
    min_axis = np.round(np.min(array)) - 50
    max_axis = np.round(np.max(array)) + 50
    x_axis = np.linspace(min_axis, max_axis, 1000)
    density = 1/n * sum(norm.pdf(x_axis, xi, bin) for xi in array)
    plt.fill_between(x_space, density, alpha=1)
    plt.axis([min_axis, max_axis, 0.00, max(density) * 2])
    plt.show()


df_X = pd.read_csv("resource/X.csv")
X = np.array(df_X.vals)
x_d = np.linspace(0, 200, 1000)


plot_kernel_density_estimate(len(X), 3, X, x_d)
