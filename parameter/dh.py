from util import findGauss, findUniform
import matplotlib.pyplot as plt
import numpy as np


def Gauss(name):
    """"
    Calls the findGauss function from util.py to return the Gauss prior for the given molecule.
    Input:      name of molecule
    Output:     Gauss prior object containing pdf, logpdf, cdf, ppf and rvs methods
    """
    prior = findGauss(name, 'd_h')
    return prior


def uniform(name):
    """
    Calls the findUniform function from util.py to return the uniform bounds for the given molecule.
    Input:      name of molecule
    Output:     array of length [2] with the upper and lower bounds for the uniform prior
    """
    prior = findUniform(name, 'd_h')
    return prior


def plot(name, type):
    """
    Plots the prior probability distribution for the given molecule.
    Input:      name of molecule, type of prior (should either be 'Gauss' or 'uniform')
    Output:     matplotlib.pyplot graph of the given prior
    """
    # set the xrange, upper bound and lower bound for the prior
    xrange = uniform(name)
    lb = xrange[0,0]
    ub = xrange[0,1]
    xrange = np.linspace(lb, ub, 100)

    # plot the Gauss prior
    if (type == 'Gauss'):
        prior = Gauss(name)
        plt.xlabel('Head Thickness [Å]')
        plt.ylabel('pdf')
        plt.title(name)
        plt.plot(xrange, prior.pdf(xrange))
        plt.show()

    # plot the uniform prior
    if (type == 'uniform'):
        y = np.zeros_like(xrange)
        xrange = np.linspace(0.5 * lb, 1.3 * ub, 100)
        for i, j in enumerate(xrange):
            if (lb <= j <= ub):
                y[i] = 1.0
            else:
                y[i] = 0.0
        plt.xlabel('Head Thickness [Å]')
        plt.ylabel('pdf')
        plt.title(name)
        plt.plot(xrange, y)
        plt.show()


# Test out the package
plot('DMPC', 'Gauss')
plot('DMPC', 'uniform')