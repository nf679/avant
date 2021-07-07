from util import findGauss, findUniform

def Gauss(name):
    prior = findGauss(name,'v_h')
    return prior

def uniform(name):
    prior = findUniform(name,'v_h')
    return prior


print(Gauss('DMPC').ppf(0.1))
print(uniform('DMPC'))