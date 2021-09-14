import numpy as np
from scipy.optimize import brentq
from scipy.stats import norm, truncnorm


class Gauss:
    """
    Creates an informed prior probability distribution through a weighted sum of Gaussian distributions
    for literature values of a parameter. Can return statistical properties of this distribution and has
    an rvs method to return random variates from the distribution.
    """

    def __init__(self, loc_scale, lb, ub):
        """
        Parameters
        ----------
        loc_scale: array-like
            An array of the loc and scale values used to create each Gaussian.
        lb: float
            Lower bound to clip distribution to
        ub: float
            Upper bound to clip distribution to
        """
        self.data = np.atleast_2d(loc_scale)
        # The xrange to use for the distribution.
        self.lb = lb
        self.ub = ub
        self.xrange = np.linspace(self.lb, self.ub, 100)
        # The weight each Gaussian has in the sum: currently equally weighted.
        self.weight = 1.0 / len(self.data)
        self._pdf_ = []

        def l_s(mean, std):
            # convert bounds to scaled distribution
            return (lb - mean) / std, (ub - mean) / std

        # Create arrays from the data
        # truncnorm takes care of each gaussian contribution integrating
        # to unity, etc.
        self.distros = [truncnorm(*l_s(d[0], d[1]), loc=d[0], scale=d[1])
                        for d in self.data]

    def pdf(self, x):
        """
        Loops over the values in the data array to find the gaussian for each value. The Gaussians
        are then added, taking the weight into consideration. The value of the pdf at the x value
        given is then returned.
        """
        x = np.atleast_1d(x)

        arrs = [d.pdf(x) for d in self.distros]
        return np.sum(arrs, axis=0) / len(self.data)

    def logpdf(self, x):
        """
        Returns the log of the pdf at x.
        """
        return np.log(self.pdf(x))

    def cdf(self, x):
        """
        Returns the cumulative distribution function at x.
        """
        arrs = [d.cdf(x) for d in self.distros]
        return np.sum(arrs, axis=0) / len(self.data)

    def _ppf_single(self, q):
        factor = 10.
        left, right = self.lb, self.ub

        # obtain brackets
        if np.isinf(left):
            left = min(-factor, right)
            while self._ppf_root(left, q) > 0.:
                left, right = left * factor, left
            # left is now such that cdf(left) <= q
            # if right has changed, then cdf(right) > q

        if np.isinf(right):
            right = max(factor, left)
            while self._ppf_root(right, q) < 0.:
                left, right = right, right * factor
            # right is now such that cdf(right) >= q

        return brentq(self._ppf_root, left, right, args=(q,))

    def ppf(self, q):
        """
        Returns the percent point function (quantile function / inverse cdf) at q.
        """
        vfun = np.vectorize(self._ppf_single, otypes='d')
        _ppf = vfun(np.atleast_1d(q))

        if len(_ppf) == 1:
            return _ppf[0]
        return _ppf

    def _ppf_root(self, x, q):
        return self.cdf(x) - q

    def rvs(self, n):
        """
        Return n number of random numbers from the pdf.
        """
        # TODO consider using scipy.stats.NumericalInversePolynomial, it might
        # be able to generate random variates more efficiently for this kind of
        # distribution.
        # Alternatively consider inheriting scipy.stats.rv_continuous.
        # This would mean you wouldn't have to implement ppf, rvs, etc.
        gauss = self.pdf(self.xrange)
        prob = gauss / sum(gauss)  # normalise the pdf so the values sum to 1
        _rvs = np.random.choice(self.xrange, p=prob, size=n)
        return _rvs
