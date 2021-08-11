import sys
sys.path.append('../')

import unittest
import numpy as np
from scipy.stats import norm
from numpy.testing import assert_equal, assert_almost_equal, assert_
from parameter.gauss_class import Gauss
import parameter.vh as vh

class TestDh(unittest.TestCase):

    def test_Gauss(self):
        a = vh.Gauss('DMPC')
        loc_scale = np.atleast_2d([(320.9, 20.1), (339.5, 14.5), (319.0, 6.0)])
        b = Gauss(loc_scale, 250.0, 450.0)
        assert_almost_equal(a.pdf(0.5),b.pdf(0.5))

    def test_uniform(self):
        b = vh.uniform('DMPC')
        assert_almost_equal(b,np.array([[250.0,450.0]]))

    def test_plot(self):






