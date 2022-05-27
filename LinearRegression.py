import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.regression as smreg


# first item is beta_0, second item is beta_1
def simple_regression_betas(X, Y):
    design_matrix = np.c_[np.ones(len(X)), X]
    model = smreg.linear_model.OLS(Y, design_matrix)
    results = model.fit()
    return results


# equation y=β0+β1x+β2x2+β3x3y=β0+β1x+β2x2+β3x3.
# first item is beta_0, second item is beta_1, third item is beta_2, fourth item is beta_3
def multi_regression_betas(X, Y):
    design_matrix = np.c_[np.ones(len(X)), X, X**2, X**3]
    model = smreg.linear_model.OLS(Y, design_matrix)
    results = model.fit()
    return results


def create_scatter_plot(X, Y, isSimple):
    fig, ax = plt.subplots(1,1, figsize = (10,5))
    ax.scatter(X, Y)
    # projections
    x = np.linspace(np.min(X), np.max(X), 200)
    if isSimple:
        parameters = simple_regression_betas(X, Y).params
        y = parameters[0] + parameters[1] * x
    else:
        parameters = multi_regression_betas(X, Y).params
        y = parameters[0] + parameters[1] * x + parameters[2] * x**2 + parameters[3] * x**3
    ax.plot(x, y, 'orange')
    plt.show()


def scatter_residuals(X, Y, isSimple):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    if isSimple:
        parameters = simple_regression_betas(X, Y).params
        y_hat = parameters[0] + parameters[1] * X
    else:
        parameters = multi_regression_betas(X, Y).params
        y_hat = parameters[0] + parameters[1] * X + parameters[2] * X**2 + parameters[3] * X**3
    residuals = Y - y_hat
    ax.scatter(X, residuals)
    plt.show()


def compute_R_squared(X, Y, isSimple):
    if isSimple:
        results = simple_regression_betas(X, Y)
    else:
        results = multi_regression_betas(X, Y)
    return results.rsquared


bivariate_1 = pd.read_csv("resource/bivariate_1.csv")
bivariate_2 = pd.read_csv("resource/bivariate_2.csv")
bivariate_3 = pd.read_csv("resource/bivariate_3.csv")
X1 = bivariate_1.X
Y1 = bivariate_1.Y
X2 = bivariate_2.X
Y2 = bivariate_2.Y
X3 = bivariate_3.X
Y3 = bivariate_3.Y


create_scatter_plot(X3, Y3, False)
# scatter_residuals(X1, Y1, true)
