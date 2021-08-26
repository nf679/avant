.. refl_package documentation master file, created by
   sphinx-quickstart on Wed Aug 25 19:53:00 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Create informed priors for reflectometry analysis
=================================================

:py:mod:`refl_package` is a python package to extract values from :py:mod:`refl_database` to create informed or uniform priors to be used in reflectometry analysis.

The aim of :py:mod:`refl_package` is to improve reflectometry analysis by applying Bayesian Statistics and creating 'informed priors' which take into account literature values in the prior probability distributions of the parameters. The priors are created in a way where they can be directly implemented into `refnx`_ to perform reflectometry analysis. Plus, the package has plotting functionalities so you can see what the prior probability distirbutions look like. 

.. _refnx: https://refnx.readthedocs.io/en/latest/index.html

.. toctree::
   installation
   features
   examples.ipynb
   faq
