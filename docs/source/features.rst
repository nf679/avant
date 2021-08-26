.. _features_chapter:

=============================
Features
=============================

Currently, :py:mod:`refl_package` only contains priors for the following five parameters for DMPC: head volume, tail volume, head thickness, tail thickness and roughness. It can create an informed prior, *Gauss*, with the following methods:

* **pdf**: probability distribution function
* **logpdf**: natural log of the probability distribution function
* **cdf**: cumulative distribution function
* **ppf**: percentile point function (also known as quantile function or inverse cdf)
* **rvs**: random variate sampling

It can also create a uniform prior which is an upper and lower bound for the prior range. 

The following plotting functionalities are available:

* **plotGauss(name)**: Plot an informed *Gauss* prior probability distribution.
* **plotUniform(name)**: Plot a uniform prior probability distribution. 


