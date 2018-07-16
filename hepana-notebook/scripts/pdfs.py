from math import sqrt, pi, erf, exp

class Linear:
    def __init__(self, boundaries):
        self.boundaries = boundaries

    def _norm(a):
        l, r = self.boundaries
        return a / 2. * (r**2 - l**2) + r - l
    
    def __call__(self, x, a):
        return (1. + a * x) / _norm(a)

    def integral(x):
        return (x + a / 2. * x**2) / _norm(a)


class Gaussian:
    SQRT2 = sqrt(2.)
    SQRTPI = sqrt(pi)
    
    def __init__(self, boundaries):
        self.boundaries = boundaries

    def _t(x):
        return (x - mean) / self.SQRT2 / width
    
    def __call__(self, x, mean, width):
        l, r = self.boundaries
        norm = self.SQRTPI / self.SQRT2 * width
        norm *= erf(_t(r)) - erf(_t(l))
        
        tx = _t(x)
        return exp(-tx * tx) / norm

    def integral(x):
        l, r = self.boundaries
        return erf(_t(x)) / (erf(_t(r)) - erf(_t(l)))
