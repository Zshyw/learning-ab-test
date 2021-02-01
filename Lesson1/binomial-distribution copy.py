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
x = np.arange(binom.pmf(0.01, n, p), binom.ppf(0.99, n, p))
ax.plot(x, binom.pmf(x, n, p), 'bo', ms = 8, label = 'binom pmf')
ax.vlines(x,0, binom.pmf(x, n, p), colors = 'b', lw = 5, alpha = 0.5)

rv = binom(n,p)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles = '-', lw=1, label = 'frozen pmf')
ax.legend(loc = 'best', frameon = False)
plt.show()

# %%
n,p = 1000, 0.4
n2, p2 = 1000, 0.7
mean, var, skew, kurt = binom.stats(n,p, moments ='mvsk')
x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n,p)) ## ppf = percent point function
x2 = np.arange(binom.ppf(0.01, n2, p2), binom.ppf(0.99, n2,p2)) ## ppf = percent point function
y = binom.pmf(x,n,p)
y2 = binom.pmf(x2, n2,p2)
z = []
for i in zip(x,y,y2):
    z.append(i)
df = pd.DataFrame(z, columns = ['x', 'y', 'y2'])
fig = px.line(df, x = 'x', y = ['y', 'y2'])
fig.show()
# %%
