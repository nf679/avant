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
        plt.xlabel('Head Volume')
        plt.ylabel('pdf')
        plt.plot(xrange,prior.pdf(xrange))
        plt.show()

    if (type =='uniform'):
        #plot the uniform prior
        print("uniform")




print(Gauss('DMPC').ppf(0.1))
print(uniform('DMPC'))
plot('DMPC','Gauss')