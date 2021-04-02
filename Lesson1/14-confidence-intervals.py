#%% 
from scipy.stats import binom
from scipy.stats import norm
import numpy as np 
import matplotlib.pyplot as plt 
import plotly.express as px 
import scipy.stats as stats
import pandas as pd 

# %%
n,p = 2000, 300/2000
n1, p1 = 1000, 100/1000
mean, var, skew, kurt = binom.stats(n,p, moments ='mvsk')
x = np.arange(binom.ppf(0.001, n, p), binom.ppf(0.999, n,p)) ## ppf = percent point function
y = binom.pmf(x,n,p)
z = []
for i in zip(x,y):
    z.append(i)
df = pd.DataFrame(z, columns = ['x', 'y'])
fig = px.line(df, x = 'x', y = ['y']) 
fig.show()

z = norm.ppf(0.995, loc=0, scale=1)
sterror = np.sqrt((p*(1-p)/n))

z1 = norm.ppf(0.975, loc=0, scale=1)

print(f'Z score: {z}')
#### calculates the z score of confidence interval 95% (for 2 tailed tests)
#### with mean = 0, std = 1
#### used for multiplying with Standard Error to obtain Margin of Error

moe = z * sterror
print(f'Margin of Error: {moe}')
print(f'Lower interval: {(p-moe)*n}, {p-moe}')
print(f'Upper interval: {(moe+p)*n}, {p+moe}')

np_up = norm.ppf(0.995, loc = binom.mean(n,p), scale = binom.std(n,p))
np_down =norm.ppf(0.005, loc = binom.mean(n,p), scale = binom.std(n,p))
print(f'norm.ppf CI calculation: {np_down}, {np_up}')
#### directly gives you where the value lies at both the higher/lower end of the normal distribution
#### using normal distribution because we pass the checks for using this


print(f'binom.interval CI calculation: {stats.binom.interval(alpha = 0.99, n = n, p = p)}')

#### calculates the 
# %%
