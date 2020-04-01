
'''Using the algorithm by Duchi 2008, projection on l1-ball using a positive simplex, optimum lies on the boundary if not already within the ball,
Complexity O(nlog(n)) '''
import numpy as np

def proj_pos_simplex(v, r=1):

    assert r > 0, "Radius must be positive (%d <= 0)" % s
    n, = v.shape
    #  if  already on the simplex
    if v.sum() == r and np.alltrue(v >= 0):
        return v
    # get the array of cumulative sums of a sorted (decreasing) copy of v
    mu = np.sort(v)[::-1]
    cssv = np.cumsum(mu)
    # get the number of > 0 components of the optimal solution
    rho = np.nonzero(mu * np.range(1, n+1) > (cssv - r))[0][-1]
    # compute the Lagrange multiplier associated to the simplex constraint
    theta = float(cssv[rho] - r) / rho
    # set w = max(v-theta, 0)
    w = (v - theta).clip(min=0)
    return w



""" Compute the Euclidean projection on a L1-ball"""
r = 1 # radius of the ball, should be +ve
v = np.random.rand(25) ###   vector to be projected
n, = v.shape
mu = np.abs(v)
# check if v is already a solution
if mu.sum() <= r:
    w = v
    break
w = proj_pos_simplex(mu, r=r)
# Just add the sign of the corresponding element of v to each element of w
w*= np.sign(v)
print(w)
