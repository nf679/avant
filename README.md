# refl_package

**Create informed priors for reflectometry analysis**

[![Coverage Status](https://coveralls.io/repos/github/nf679/refl_package/badge.svg?)](https://coveralls.io/github/nf679/refl_package)

``refl_package`` is a python package to extract values from [``refl_database``](https://github.com/nf679/refl-database) to create informed or uniform priors to be used in reflectometry analysis.

The aim of ``refl_package`` is to improve reflectometry analysis by applying Bayesian Statistics and creating 'informed priors' which take into account literature values in the prior probability distributions of the parameters. The priors are created in a way where they can be directly implemented in [``Refnx``](https://refnx.readthedocs.io/en/latest) to perform reflectometry analysis. Plus, the package has plotting functionalities so you can see what the prior probability distributions look like. 

## Features

Currently, ``refl_package`` only contains priors for the following five parameters for DMPC: head volume, tail volume, head thickness, tail thickness and roughness. It can create an informed prior, Gauss, with the following methods:     

- **pdf** : probability distribution function
- **logpdf** : natural log of the probability distribution function
- **cdf** : cumulative distribution function
- **ppf** : percentile point function (quantile function  / inverse cdf)
- **rvs** : random variate sampling

It can also create a uniform prior which is an upper and lower bound for the prior range. The following plotting functionalities are available:

- **plotGauss(name='DMPC')**: Plot a 'Gauss' prior probability distribution. 
- **plotUniform(name='DMPC')**: Plot a uniform prior probability distribution.



## Examples

1. Plotting the informed prior for head volume for DMPC: 

       import refl_package.parameter.vh as vh
       vh.plotGauss('DMPC') 

![dmpc_vh](https://user-images.githubusercontent.com/53176345/124952482-30ed0080-e00c-11eb-80f7-f1265c9c4d6a.png)

2. Plotting the uniform prior for the head volume for DMPC:

       import refl_package.parameter.vh as vh
       vh.plotUniform('DMPC')

![dmpc_vh_u](https://user-images.githubusercontent.com/53176345/124953932-7bbb4800-e00d-11eb-8588-79e88b7f66c3.png)



3. Set a parameter equal to the Gauss object (can be used in Refnx) 

       import refl_package.parameter.vh as vh
       x = vh.Gauss('DMPC')

## Problems

If you discover any issues with ``refl_package`` feel free to either submit the issue to our issue tracker on [Github](https://github.com/nf679/refl_package), or fix the issue yourself and make a pull request to the main branch. 

## Installation 

INSERT INSTALLATION METHOD HERE ONCE IVE GOT IT ON PYPI OR YOU CAN BUILD / INSTALL WITH SETUP.PY


## Contributors


## License

The project is licensed under the MIT license.




       
