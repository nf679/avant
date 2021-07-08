# refl_package

A python package to extract values from [refl_database](https://github.com/nf679/refl-database) to create informed or uniform priors to be used in reflectometry analysis.

## refl_package.\<parameter\>

The following parameters are available in this format:

- dh:          head thickness
- dt:          tail thickness
- roughness:   roughness of the layer
- vh:          head volume 
- vt:          tail volume 

### Methods

- **Gauss(name='DMPC')**: Return an informed prior probability object as an object with the following statistical methods:
    - **pdf** : probability distribution function
    - **logpdf** : natural log of the probability distribution function
    - **cdf** : cumulative distribution function
    - **ppf** : percentile point function (quantile function  / inverse cdf)
    - **rvs** : random variate sampling

- **uniform(name='DMPC')**: Return an array with a lower and upper bound which can be used for a uniform probability distribution.
- **plot(name='DMPC',type='uniform')**: Plot either a (type=) 'uniform' or 'Gauss' prior probability distribution. 


## Examples



