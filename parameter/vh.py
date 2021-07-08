from util import findGauss, findUniform
import matplotlib.pyplot as plt
import numpy as np

def Gauss(name):

    prior = findGauss(name,'v_h')
    return prior


def uniform(name):

    prior = findUniform(name,'v_h')
    return prior


def plot(name,type):

    xrange = uniform(name)
    lb = xrange[0]
    ub = xrange [1]
    xrange = np.linspace(lb, ub, 100)

    if (type == 'Gauss'):
        #plot the gauss prior
        prior = Gauss(name)
        plt.xlabel('Head Volume [Å]')
        plt.ylabel('pdf')
        plt.title(name)
        plt.plot(xrange,prior.pdf(xrange))
        plt.show()

    if (type =='uniform'):
        #plot the uniform prior
        y = np.zeros_like(xrange)
        xrange = np.linspace(0.5*lb,1.3*ub,100)
        for i,j in enumerate(xrange):
            if (lb<=j<=ub):
                y[i] = 1.0
            else:
                y[i] = 0.0

        plt.xlabel('Head volume [Å]')
        plt.ylabel('pdf')
        plt.title(name)
        plt.plot(xrange,y)
        plt.show()





#print(Gauss('DMPC').ppf(0.1))
#print(uniform('DMPC'))
plot('DMPC','Gauss')
plot('DMPC','uniform')