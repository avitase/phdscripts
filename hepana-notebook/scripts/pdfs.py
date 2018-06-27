from math import sqrt, pi, erf, exp

class Linear:
    def __init__(self, boundaries):
        self.boundaries = boundaries
    
    def __call__(self, x, a):
        l, r = self.boundaries
        norm = a / 2. * (r*r - l*l) + r - l
        return (1. + a * x) / norm

class Gaussian:
    SQRT2 = sqrt(2.)
    SQRTPI = sqrt(pi)
    
    def __init__(self, boundaries):
        self.boundaries = boundaries
    
    def __call__(self, x, mean, width):
        t = lambda x: (x - mean) / self.SQRT2 / width
        
        l, r = self.boundaries
        norm = self.SQRTPI / self.SQRT2 * width
        norm *= erf(t(r)) - erf(t(l))
        
        tx = t(x)
        return exp(-tx * tx) / norm
