'''Naman Deep Singh 01.04.2020'''
'''Using the algorithm by Duchi 2008, projection on l1-ball using a positive simplex, optimum lies on the boundary if not already within the ball,
Complexity O(nlog(n)) '''

import numpy as np

def proj_pos_simplex(v, r=1):

    assert r > 0, "Radius must be positive (%d <= 0)" % s
    n, = v.shape
    #  if  already on the simplex
    if v.sum() == r and np.alltrue(v >= 0):
        return v
    mu = np.sort(v)[::-1]
    ss = np.cumsum(mu)

    rho = np.nonzero(mu * np.arange(1, n+1) > ( ss - r))[0][-1]
    theta = float(ss[rho] - r) / rho
    w = (v - theta).clip(min=0)
    return w

""" Compute the Euclidean projection on a L1-ball"""
r = 1 # radius of the ball, should be +ve
v = np.random.rand(150) ###   vector to be projected
n, = v.shape
mu = np.abs(v)
# check if v is already a solution
if mu.sum() <= r:
    w = v
    print("Projected vector is :", w)
    exit(1)
    
w = proj_pos_simplex(mu, r=r)

# Just add the sign of the corresponding element of v to each element of w
w*= np.sign(v)
print("Projected vector is :", w)
