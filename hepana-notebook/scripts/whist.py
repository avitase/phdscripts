from bisect import bisect
from uncertainties import ufloat
from math import sqrt

class WHist:
    def __init__(self, bin_edges):
        self.bin_edges = bin_edges
        self.data = [ufloat(0., 0.),] * (len(bin_edges) - 1)
        self.sumw2 = [0,] * (len(bin_edges) - 1)
        self.entries = 0

    def add(self, n, weight=1):
        idx = bisect(self.bin_edges, n)
        if idx > 0 and idx < len(self.bin_edges):
            self.entries += 1
            idx = idx - 1
            self.sumw2[idx] += weight**2
            n = self.data[idx].n
            u = sqrt(self.sumw2[idx])
            self.data[idx] = ufloat(n + weight, u)
