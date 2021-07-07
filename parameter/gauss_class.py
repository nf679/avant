import numpy as np
from scipy.optimize import root_scalar
from scipy.stats import norm


class Gauss:

    def __init__(self, loc_scale, lb, ub):

        self.data = loc_scale
        # Set the range for the priors
        self.lb = lb
        self.ub = ub
        self.xrange = np.linspace(self.lb, self.ub, 100)
        self.weight = 1.0 / len(self.data)
        self._pdf_ = []

        # Create arrays from the data
        self.distros = []
        for d in self.data:
            self.distros.append(norm(loc=d[0], scale=d[1]))


    def pdf(self, x):
        """
        Loops over the values in the data array to find the gaussian for
        each value. The gaussians are then added, taking the weight into
        consideration. If no weight is given in the file the gaussians
        are summed with equal weighting (i.e. if weight=0.0). The value
        of the pdf at the x value given is then returned.
        """
        x = np.atleast_1d(x)
        _pdf = np.zeros_like(x)
        for i, d in enumerate(self.distros):
            for j, k in enumerate(x):
                if k < self.lb:
                    _pdf[j] = 0
                elif k >= self.ub:
                    _pdf[j] = 0
                else:
                    _pdf[j] += d.pdf(x[j]) * self.weight

        return _pdf

    def logpdf(self, x):
        """
        Returns the log of the pdf at x.
        """
        return np.log(self.pdf(x))

    def cdf(self, x):
        """
        Returns the cumulative distribution function at x.
        """
        _cdf = np.zeros_like(x)
        for i, d in enumerate(self.distros):
            _cdf += d.cdf(x) * self.weight
        return _cdf

    def ppf(self, x):
        """
        Returns the percent point function (quantile function / inverse cdf) at x.
        """
        brack_min = np.mean(self.data[:, 0]) - np.mean(self.data[:, 0]) * 10
        brack_max = np.mean(self.data[:, 0]) + np.mean(self.data[:, 0]) * 10
        x = np.atleast_1d(x)
        _ppf = np.zeros_like(x)
        for i, v in enumerate(x):
            if v < 1e-7:
                _ppf[i] = self.lb
            elif v > (1.0 - 1e-7):
                _ppf[i] = self.ub
            else:
                _ppf[i] = root_scalar(self._ppf_root,
                                      bracket=[brack_min, brack_max],
                                      args=[v]).root
        if len(_ppf) == 1:
            return _ppf[0]
        return _ppf

    def _ppf_root(self, y, x):
        return self.cdf(y) - x

    def rvs(self, n):
        """
        Return n number of random numbers from the pdf.
        """
        gauss = self.pdf(self.xrange)
        prob = gauss / sum(gauss)  # normalise the pdf so the values sum to 1
        _rvs = np.random.choice(self.xrange, p=prob, size=n)
        return _rvs