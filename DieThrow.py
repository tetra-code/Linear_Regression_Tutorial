import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import uniform

die = [1, 2, 3, 4, 5, 6]
die2 = ["red", "blue", "green", "yellow", "purple"]
# Assign a probability to each single outcome
probabilities = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]
probabilities2 = [0.3, 0.15, 0.1, 0.2, 0.25]


def die_throw_rvs(n):
    """
    Second method for random die throw. Function returns 'size' number of
    random variables that simulate die-throws. In other words, the values
    {1,2,3,4,5,6} are taken with probability 1/6
    """
    random_variables = np.zeros(n)
    for i in range(n):
        # returns a uniform variable from 0 to 1
        random_variables[i] = np.ceil(uniform.rvs() * 6)
    return random_variables


def die_throw_rvs2(n):
    # return an array of size n, along with the corresponding probabilities
    return np.random.choice(die, size=n, p=probabilities)


def die_throw_avg(n):
    # return the average of array from above method
    return np.mean(die_throw_rvs2(n))


def plot_averages(n):
    # array of averages from total number of outcomes ranging from 1 to 1000
    outcomes = die_throw_rvs2(n)
    averages = [np.mean(outcomes[range(0, i)]) for i in range(1, 1001)]
    plt.plot(averages)
    plt.xlabel("n")
    plt.ylabel("Average after n throws")
    plt.show()


def weird_die_probability(n, value):
    outcome = die_throw_rvs2(n)
    count = 0
    for i in range(n):
        if outcome[i] == value:
            count = count + 1
    return count / n


print(die_throw_rvs(100))
print("Average outcome after 10 throws: ", die_throw_avg(10))
print("Average outcome after 100 throws: ", die_throw_avg(100))
print("Average outcome after 1000 throws: ", die_throw_avg(1000))
print(weird_die_probability(1000, 'purple'))
# plot_averages(1000)
