import ROOT
from ctypes import c_int, c_double
from array import array
import math
import uncertainties

class Fitter:
    def __init__(self, method='MIGRAD', config_flags=[]):
        self.method = method
        self.config_flags = config_flags
        self._fit_params = []
        self._gMinuit = None
    
    def add_param(self, name, boundary, init_value=None, step=None):
        if not init_value:
            init_value = sum(boundary) / 2.
        
        if not step:
            step = (boundary[1] - boundary[0]) / 1e4
        
        idx = len(self._fit_params)
        self._fit_params.append([idx, name, boundary, init_value, step])
        return idx
    
    def clear_params(self):
        self._fit_params = []
    
    def fit(self, fcn, refine_error=True):
        ierflg = c_int(0)
        
        self._gMinuit = ROOT.TMinuit(len(self._fit_params))
        self._gMinuit.SetFCN(fcn)
        
        for idx, name, boundary, init_value, step in self._fit_params:
            self._gMinuit.mnparm(idx, name, init_value, step, *boundary, ierflg)
        
        n_config = len(self.config_flags)
        config = array('d', self.config_flags if n_config > 0 else [0.,])
        self._gMinuit.mnexcm(self.method, config, n_config, ierflg)
        
        if refine_error:
            config = array('d', [0.,])
            self._gMinuit.mnexcm('HESSE', config, 0, ierflg)
            self._gMinuit.mnexcm('MINOS', config, 0, ierflg)
    
    def get_name(self, idx):
        return self._fit_params[idx][1]
    
    def get_value(self, idx):
        value, error = c_double(0.), c_double(0.)
        self._gMinuit.GetParameter(idx, value, error)
        return uncertainties.ufloat(value.value, error.value)
    
    def print_value(self, idx, prefix_idx=False):
        temp = '{1} = {2}'
        if prefix_idx:
            temp = '#{0:2d}: ' + temp
            
        print(temp.format(idx, self.get_name(idx), self.get_value(idx)))
    
    def print_values(self):
        for i in range(len(self._fit_params)):
            self.print_value(idx=i, prefix_idx=True)

def logl(ln_f, data):
    return -sum([ln_f(x) for x in data])

def extended_logl(ln_f, n, data):
    return logl(ln_f, data) - (len(data) * math.log(n) - n)
