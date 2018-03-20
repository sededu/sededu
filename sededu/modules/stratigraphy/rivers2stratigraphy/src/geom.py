# geometry calculations
# TODO:
#  - swap to x^(0.5) instead of sqrt for speed?

import numpy as np
from scipy.spatial import distance


def Qhatfun(Qwf, D50, g):
    # dimensionless Qw, Wilkerson and Parker, 2011
    return Qwf / (np.sqrt(g * D50) * D50**2)


def Repfun(D50, R, g, nu):
    # particle Reynolds num, Wilkerson and Parker, 2011
    return (np.sqrt(R * g * D50) * D50) / nu 


def Bbarfun(Qhat, Rep):
    # dimensionless width, Wilkerson and Parker, 2011
    return (0.00398 * Qhat**0.269) * (Rep**0.494) 


def Hbarfun(Qhat, Rep):
    # dimensionless depth, Wilkerson and Parker, 2011
    return (22.9 * Qhat**(-0.124)) * (Rep**(-0.310))


def Sbarfun(Qhat, Rep):
    # dimensionless slope, Wilkerson and Parker, 2011
    return (19.1 * Qhat**(-0.394)) * (Rep**(-0.196)) 


def dimless2dimfun(X, Qbf, g):
    # make dimensional, Wilkerson and Parker, 2011
    return (X * Qbf**(2 / 5)) / (g**(1 / 5))


def Fafun(qs, Beta):
    # parameterized avulsion frequency, e.g., Bryant et al., 1995
    return qs**Beta


def Ccc2coordsfun(Ccc, Bc, Hnbf):
    xs = np.array([[Ccc[0]-(Bc/2)], [Ccc[0]+(Bc/2)],
        [Ccc[0]+(Bc/2)], [Ccc[0]-(Bc/2)]])
    ys = np.array([[Ccc[1]-(Hnbf/2)], [Ccc[1]-(Hnbf/2)],
        [Ccc[1]+(Hnbf/2)], [Ccc[1]+(Hnbf/2)]])
    return np.hstack((xs, ys))


def outdatedIndex(chanList0, stratMax):
    chanListIdx = [ all( x['coords'][0][:,1] < stratMax ) 
                   for x in chanList0 ]
    return np.array(chanListIdx)