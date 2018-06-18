from scipy.stats import chi2
import numpy as np
import os

def poisson_interval(k, alpha=2.*0.159):
    high = chi2.ppf(1.-alpha/2., 2*k + 2) / 2.
    low = chi2.ppf(alpha/2., 2*k) / 2. if k > 0 else 0.
    return low, high

def make_hist_file(data, bin_edges, file_name, error_fct=poisson_interval):
    file_name = os.path.join('img', file_name)

    hist, bin_edges = np.histogram(data, bin_edges)

    columns = ['lower bin edge', 'bin center', 'upper bin edge',
               'lower error', 'bin content', 'upper error']
    with open(file_name, 'w') as f:
        f.write(','.join(['\"{}\"'.format(x) for x in columns]) + '\n')

        i = 0 
        row_temp = ','.join(['{:.5g}',] * len(columns))
        for n in hist:
            bin_edge = bin_edges[i], bin_edges[i+1]
            bin_center = np.mean(bin_edge)
            i = i + 1

            error_low, error_up = error_fct(n)

            values = bin_edge[0], bin_center, bin_edge[1], error_low, n, error_up
            f.write(row_temp.format(*values) + '\n')

