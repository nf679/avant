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
       
