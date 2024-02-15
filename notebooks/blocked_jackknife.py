import numpy as np
from time import time

mu, sigma = 100, 15
datapoints = 10000
x = mu + sigma*np.random.randn(datapoints)

def jackknife(data, stat=None):
    n = len(data)
    t = np.zeros(n)
    inds = np.arange(n)
    for i in range(n):
        t[i] = stat(np.delete(data,i) )

    print("original           bias      std. error")
    print("%8g %14g %15g" % (stat(data),(n-1)*np.mean(t)/n, (n*np.var(t))**.5))

    return (stat(data),(n-1)*np.mean(t)/n, (n*np.var(t))**.5)

def blocked_jackknife(data, stat=None, nr_blocks=None):
    n = len(data) // nr_blocks
    t = np.zeros(n)
    inds = np.arange(n)
    for i in range(n):
        t[i] = stat(np.delete(data,list(range(i*nr_blocks,i*nr_blocks+nr_blocks))) )

    print("original           bias      std. error")
    print("%8g %14g %15g" % (stat(data),(n-1)*np.mean(t)/n, (n*np.var(t))**.5))

    return (stat(data),(n-1)*np.mean(t)/n, (n*np.var(t))**.5)

# Returns mean of data samples                                                                                                                                                     
def jackknife_stat(data):
    return np.nanmean(data)



# t = jackknife(x, stat)
# print()
# t = blocked_jackknife(x, stat, 10)

import functools
j = functools.partial(jackknife, stat=jackknife_stat)
print(j(x))

bj = functools.partial(blocked_jackknife, stat=jackknife_stat, nr_blocks=10)
print(bj(x))