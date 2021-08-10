import sys
sys.path.append('../')

import unittest
import numpy as np
from scipy.stats import norm
from numpy.testing import assert_equal, assert_almost_equal
from parameter.gauss_class import Gauss

test_norm1 = norm(loc=5.0, scale=1.0)
test_norm2 = norm(loc=6.0, scale=0.5)
loc_scale = np.atleast_2d([(5.0, 1.0), (6.0, 0.5)])
test_gauss = Gauss(loc_scale, 1.0, 10.0)

class TestGaussClass(unittest.TestCase):
    """
    Tests for the Gauss class.
    """

    def test_init(self):
        """
        Test initialisation function.
        """
        test_norm1 = norm(loc=5.0, scale=1.0)
        test_norm2 = norm(loc=6.0, scale=0.5)
        loc_scale = [(5.0,1.0),(6.0,0.5)]
        test_gauss = Gauss(loc_scale, 1.0, 10.0)

    def test_pdf(self):
        assert_almost_equal(test_gauss.pdf(1.0), (0.5 * test_norm1.pdf(1.0)) + (0.5 * test_norm2.pdf(1.0)))

    def test_logpdf(self):
        assert_almost_equal(test_gauss.logpdf(1.0), np.log((0.5 * test_norm1.pdf(1.0)) + (0.5 * test_norm2.pdf(1.0))))

    def test_cdf(self):
        assert_almost_equal(test_gauss.cdf(1.0), (0.5 * test_norm1.cdf(1.0)) + (0.5 * test_norm2.cdf(1.0)))

    def test_ppf(self):
        cdf_value = test_gauss.cdf(5.0)
        assert_almost_equal(test_gauss.ppf(cdf_value), 5.0)
