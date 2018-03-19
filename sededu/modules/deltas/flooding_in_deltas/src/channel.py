# channel functions
import numpy as np
import hydro, utils
import os, csv

def set_B(B0, mou, thet, nx, dx):
    # set B for channel width
    B = np.zeros(nx + 1)
    chanLen = int(mou * nx)
    B[:chanLen] = B0
    B[chanLen:] = B0 + 2 * ((np.arange(1, (nx - chanLen+2))) \
        * (1600e3 / 400) * np.tan(np.radians(2)))
    # print(B)
    return B

def get_slope(eta, nx, dx):
    # return slope of input bed (eta)
    S = np.zeros(nx + 1)
    S[0] = (eta[0] - eta[1]) / dx
    S[1:nx] = (eta[0:nx-1] - eta[2:nx+1]) / (2 * dx)
    S[nx:] = (eta[nx-1] - eta[nx]) / dx
    return S

def load_nitt():
    this_dir = os.path.dirname(__file__)
    this_path = os.path.join(this_dir,'')
    par_path = os.path.normpath(this_path + os.pardir)
    data_path = os.path.join(par_path, 'private', 'data')
    nitt_bed = NittData()
    nitt_water = NittData()
    nitt_bed.data = np.genfromtxt(os.path.join(data_path, 'nitt_bed.csv'), 
                             delimiter=',', skip_header=1)
    nitt_water.data = np.genfromtxt(os.path.join(data_path, 'nitt_water.csv'), 
                             delimiter=',', skip_header=1)
    # nitt_bed.RK = [ nitt_bed.data[:,0] ]
    nitt_water.RK = [ nitt_water.data[:,1] ]
    with open(os.path.join(data_path, 'nitt_bed.csv')) as csvfile:
        nitt_bed_rdr = csv.reader(csvfile, delimiter=',', quotechar="'")
        nitt_bed.hdr = next(nitt_bed_rdr)
    with open(os.path.join(data_path, 'nitt_water.csv')) as csvfile:
        nitt_water_rdr = csv.reader(csvfile, delimiter=',', quotechar="'")
        nitt_water.hdr = next(nitt_water_rdr)
    return nitt_bed, nitt_water

class NittData():
    data = []
    hdr = []

def get_path():
    
    return thisPath