#%% 
from scipy.stats import binom
import numpy as np 
import matplotlib.pyplot as plt 
import plotly.express as px 
import scipy.stats as stats
import pandas as pd 

n,p = 5, 0.4 
mean, var, skew, kurt = binom.stats(n,p,moments='mvsk')
fig,ax = plt.subplots(1,1)
x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))

# binom.ppf(0.5,n,p) = 2.0 (n*p)
# binom.cdf(2.0,n,p) = 0.6825599999999997
# binom.pmf(2.0,n,p) = 0.3455999999999999

ax.plot(x, binom.pmf(x, n, p), 'bo', ms = 8, label = 'binom pmf')
ax.vlines(x,0, binom.pmf(x, n, p), colors = 'b', lw = 5, alpha = 0.5)

rv = binom(n,p)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles = '-', lw=1, label = 'frozen pmf')
ax.legend(loc = 'best', frameon = False)
plt.show()



# https://www.tutorialspoint.com/scipy/scipy_stats.htm

# %%
