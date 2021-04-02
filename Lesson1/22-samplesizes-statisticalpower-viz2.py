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

n,p = 2000, 0.1
n1, p1 = 10200, 0.1
n2, p2 = 10800, 0.105
mean, var, skew, kurt = binom.stats(n,p, moments ='mvsk')
x = np.arange(binom.ppf(0.001, n, p), binom.ppf(0.999, n,p))
z_x = zscore(x)
y = binom.pmf(x,n,p)

x1 = np.arange(binom.ppf(0.001, n1, p1), binom.ppf(0.999, n1,p1)) 
z_x1 = zscore(x1)
y1 = binom.pmf(x1,n1,p1)

x2 = np.arange(binom.ppf(0.001, n2, p2), binom.ppf(0.999, n2,p2)) 
z_x2 = zscore(x2)
y2 = binom.pmf(x2,n2,p2)

x_tail1 = np.arange(binom.ppf(0.01, n1, p1), binom.ppf(0.025, n1, p1))
y_tail1 = binom.pmf(x_tail1, n1, p1)

fig = go.Figure()
fig.add_vline(x=binom.ppf(0.025, n1,p1))
fig.add_vline(x=binom.ppf(0.975, n1,p1))
fig.add_trace(go.Scatter(x = x1, y = y1, name = 'n=10,000, p = 0.1', fill = 'tozeroy'))
# fig.add_trace(go.Scatter(x = x2, y = y2, name = 'n=10,000, p = 0.2', fill = 'tonexty'))
fig.add_trace(go.Scatter(x = x2, y = y2, name = 'n=10,000, p = 0.2', fill = 'tozeroy'))

fig.add_trace(go.Scatter(x = x_tail1, y = y_tail1, name = 'n=10,000, p = 0.2', fill = 'tozeroy'))
fig.show()

# %%
