#%% 
from scipy.stats import binom
from scipy.stats import norm
from scipy.stats import zscore
import numpy as np 
import matplotlib.pyplot as plt 
import plotly.express as px 
import scipy.stats as stats
import pandas as pd 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

n,p = 2000, 0.1
n1, x1 = 10072, 974
n2, x2 = 9886, 1242
p1, p2 = x1/n1, x2/n2 

def ppool(n1, x1, n2, x2):
    return (x1+x2)/(n1+n2)

def sterror(ppool, n1, n2):
    ste = np.sqrt(ppool * (1-ppool) * ((1/n1) + (1/n2) )) 
    return ste 

def diff(x1, x2):
    return (x2-x1) 

def moe(d, ste, sig): 
    z = norm.ppf(sig, loc=0, scale=1)
    margin = z * ste
    # d = diff(p1, p2)
    return [d-margin, d , d+margin, margin] 

conf_level = 0.95 
dmin = 0.02 

pp = ppool(n1, x1, n2, x2)
st = sterror(pp, n1, n2)
d = diff(p1, p2)
m = moe(d, st, 0.975)
m

# %%
