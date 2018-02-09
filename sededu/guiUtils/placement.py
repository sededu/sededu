# functions to place objects in GUI
import numpy as np
import collections as coll

def gridButton(n, geomObj):
    # determine the geometry of the grid based on window size
    # n objects in 2x(n/2) grid in area of size [W x H]
    Geom = coll.namedtuple('Geom', ['x', 'y', 'w', 'h']) # replace with class?
    nRows = n / 2
    bHeight = (geomObj.h / nRows) * 0.9
    bWidth = (geomObj.w / 2) * 0.9
    xOff = geomObj.x
    yOff = 0
    x = np.repeat([xOff, xOff+bWidth+(bWidth*0.1)], [nRows, nRows])
    ySep = (geomObj.h - (nRows * bHeight))/(nRows+1)
    y1 = yOff + ( ySep * np.linspace(1, nRows, nRows) ) + ( bHeight * np.linspace(0, nRows-1, nRows))
    y = np.tile(y1, 2)
    geom = Geom(x, y, bWidth, bHeight)
    return geom


def margins(dims):
    # reduce overall window dims to workable dims
    Geom = coll.namedtuple('Geom', ['x', 'y', 'w', 'h']) # replace with class?
    workWidth = dims[0] * 0.9
    xOff = dims[0] * 0.05
    workHeight = dims[1] * 0.95
    yOff = dims[1] * 0.025
    margs = Geom(xOff, yOff, workWidth, workHeight)
    return margs


def divideWindow(geomObj):
    # divide workable dims into button array and support array
    Geom = coll.namedtuple('Geom', ['x', 'y', 'w', 'h']) # replace with class?
    lowerRatio = 0.2
    upperHeight = geomObj.h * (1-lowerRatio)
    div = Geom(geomObj.x, upperHeight, geomObj.w, geomObj.h)
    return div


def quitButton(dims):
    xd = max(dims)
    yd = max(dims)
    return [xd, yd]