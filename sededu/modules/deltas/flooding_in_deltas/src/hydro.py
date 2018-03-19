# hydro functions
import numpy as np


def get_backwater_dBdx(eta, S, B, H0, Cf, Qw, nx, dx):
    # backwater formulated for changing width
    H = np.zeros(nx + 1) # preallocate depth 
    H[-1] = abs(H0 - eta[-1]) # water depth at downstream boundary
    dBdx = (B[1:] - B[0:nx]) / dx
    iterVect = np.int_( np.linspace(nx, 1, nx+1) )
    for i in iterVect:
        # predictor step: computation of a first estimation of the water depth Hp
        Frsqp = get_froude(Qw, H[i], B[i-1]) # calculate froude from conditions at i+1
        dHdxp = get_dHdx_dBdx(S[i], Cf, Frsqp, H[i], B[i-1], dBdx[i-1]) # get dHdx width changing form
        Hp = H[i] - dHdxp * dx # solve for H prediction
        # corrector step: computation of H
        Frsqc = get_froude(Qw, Hp, B[i-1]) # calculate froude at i with prediction depth
        dHdxc = get_dHdx_dBdx(S[i-1], Cf, Frsqc, Hp, B[i-1], dBdx[i-1]) # doaa
        # convolution of prediction and correction, trapezoidal rule
        H[i-1] = H[i] - ( (0.5) * (dHdxp + dHdxc) * dx )
    return H


def get_dHdx_dBdx(S_loc, Cf, Frsq, H_loc, B_loc, dBdx):
    # formulation to get dHdX for a changing width backwater formulation
    dHdx = ((S_loc-(Cf*Frsq))/(1-Frsq)) + (Frsq/(1-Frsq)) * (H_loc/B_loc) * (dBdx)
    return dHdx

def get_froude(Qw, H, B):
    g = 9.81 # gravitational acceleration constant
    Frsq = ( Qw**2 / (g * B**2 * H**3) )
    return Frsq

def find_backwaterregion(H, dx):
    dHdx = (H[1:] - H[:-1]) / dx
    dHdxdx = (dHdx[1:] - dHdx[:-1]) / dx
    t = dHdxdx*1e9 < 0.080 # threshold
    cps = t[:-1] != t[1:] # changepoints
    Xs = ( np.nonzero(cps)[0][:2] ) * dx
    return Xs