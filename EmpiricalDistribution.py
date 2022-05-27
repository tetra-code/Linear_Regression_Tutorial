import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.distributions.empirical_distribution import ECDF
from scipy import stats


# return array of exponential distribution x and y values, with
# x values derived from array of interest
def calculate_exp_dist(array, lam):
    min_axis = np.min(array)
    max_axis = np.max(array) * 2
    exp_dist_x = np.arange(min_axis, max_axis, 0.01)
    exp_dist_y = 1 - np.exp(-lam * exp_dist_x)
    return [exp_dist_x, exp_dist_y]


def plot_ecdf_of_exp_distribution(array, lam):
    ecdf = ECDF(array)
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    plt.plot(ecdf.x, ecdf.y)
    exp_dist = calculate_exp_dist(array, lam)
    ax.plot(exp_dist[0], exp_dist[1])
    plt.show()


def ks_distance(lam, y):
    return stats.kstest(y, stats.expon(scale=1/lam).cdf)[0]


df = pd.read_csv("resource/Y.csv")
Y = np.array(df.vals)


print(ks_distance(3, Y))
