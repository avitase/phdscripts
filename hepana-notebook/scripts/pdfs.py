from math import sqrt, pi, erf, exp

class Linear:
    def __init__(self, boundaries):
        self.boundaries = boundaries

    def _norm(self, a):
        l, r = self.boundaries
        return a / 2. * (r**2 - l**2) + r - l
    
    def __call__(self, x, a):
        return (1. + a * x) / self._norm(a)

    def integral(self, x):
        return (x + a / 2. * x**2) / self._norm(a)


class Gaussian:
    SQRT2 = sqrt(2.)
    SQRTPI = sqrt(pi)
    
    def __init__(self, boundaries):
        self.boundaries = boundaries

    def _t(self, x):
        return (x - mean) / self.SQRT2 / width
    
    def __call__(self, x, mean, width):
        l, r = self.boundaries
        tx, tr, rl = [self.t(y) for y in [x, r, l]]

        norm = self.SQRTPI / self.SQRT2 * width
        norm *= erf(tr) - erf(tl)
        
        return exp(-tx * tx) / norm

    def integral(self, x):
        l, r = self.boundaries
        tx, tr, rl = [self.t(y) for y in [x, r, l]]
        return erf(tx) / (erf(tr) - erf(tl))
