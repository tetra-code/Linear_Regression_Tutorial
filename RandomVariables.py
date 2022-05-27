import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
from scipy.stats import expon


def exponential_rvs(n, theta):
    """
    function returns 'size' number of
    exponential random variable with parameter theta > 0
    """
    random_variables = np.zeros(n)
    # transform the uniform_variables into exponential random variables that are saved in the array 'random_variables'
    for i in range(n):
        random_variables[i] = (-1 / theta) * np.log(uniform.rvs())

    return random_variables


def rand_var_greater_than_prob(n, greater_than_val, rand_theta):
    # random_variables = expon.rvs(n, scale=1/rand_theta)
    random_variables = exponential_rvs(n, rand_theta)
    indicators = np.linspace(greater_than_val, greater_than_val, n)
    # those greater than the indicators will have 1 as true, 0 as false
    proportion = np.count_nonzero(np.greater(random_variables, indicators))
    print(proportion)
    return proportion / n


def plot_histogram(n, rand_theta, density_theta):
    # we use expon.rvs for safety
    # between 0.5 and 10
    random_variables = expon.rvs(n, scale=1/rand_theta)
    theoretical_scale = 1/density_theta
    fig, ax = plt.subplots(1, 1)
    ax.hist(random_variables, density=True, bins='auto')
    x = np.linspace(expon.ppf(0.01, scale=theoretical_scale), expon.ppf(0.99, scale=theoretical_scale), 100)
    ax.plot(x, expon.pdf(x, scale=theoretical_scale), 'r-', lw=5, alpha=0.6, label='pdf')
    ax.plot()
    plt.show()
    return


# plot_histogram(1000, 3, 1)
print("the probability is given by {}".format(rand_var_greater_than_prob(1000, 1, 3)))

