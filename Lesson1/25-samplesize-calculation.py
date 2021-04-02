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

def zscore(conf_level, tailtest):
    if tailtest == 1:
        z = norm.ppf(conf_level, loc=0, scale = 1)
    elif tailtest == 2:
        z = norm.ppf(1-((1-conf_level)/2), loc=0, scale = 1)
    return z 


conf_level = 0.95
statpower = 0.8
beta = 1 - statpower 
base_rate = 0.5
min_effect = 0.03
test_rate = base_rate+min_effect

z_alpha = zscore(conf_level,2)
z_power = zscore(statpower, 1)

def sample_needed(za, zb, ca, cb):
    z_sq = ((z_alpha) + (z_power))**2 
    c_ = (ca*(1-ca)) + (cb*(1-cb))
    denom = (ca-cb)**2 
    return (z_sq*c_) / denom

### this formula aligns with sample size calculator in below link
### https://stats.stackexchange.com/questions/392979/ab-test-sample-size-calculation-by-hand
### https://www.evanmiller.org/ab-testing/sample-size.html
def sample_needed2(za, zb, ca, cb):
    z1 = za*np.sqrt(2*ca*(1-ca))
    z2 = zb*np.sqrt(ca*(1-ca) + cb*(1-cb))
    nom = (z1+z2)**2
    denom = (ca-cb)**2 
    return nom / denom

s = sample_needed2(z_alpha, z_power, base_rate, test_rate)

print(f'sample size needed: {s}')
print(f'Confidence Level: {conf_level}, Z Alpha: {z_alpha}')
print(f'Statistical Power: {statpower}, Z Power: {z_power}')
print(f'Base Rate: {base_rate}')
print(f'test_rate: {test_rate}')
print(f'Min detectable effect: {min_effect}')


# %%
# https://splitmetrics.com/blog/mobile-a-b-testing-sample-size/#:~:text=Here%E2%80%99s%20an%20A%2FB%20test%20sample%20size%20formula%20for,and%20%D0%92%20in%20case%20of%20a%20two-tailed%20test%3B
# https://towardsdatascience.com/required-sample-size-for-a-b-testing-6f6608dd330a
# http://hansheng.gsm.pku.edu.cn/pdf/2007/prop.pdf
# https://select-statistics.co.uk/calculators/sample-size-calculator-two-proportions/

# n = (Zα/2+Zβ)2 * (p1(1-p1)+p2(1-p2)) / (p1-p2)2