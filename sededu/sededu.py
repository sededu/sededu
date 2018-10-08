import os

# class sededu(object):
def sededu():
    ## setup script


    ## check dependencies


    ## import additional packages


    ## initialize the GUI
    thisDir = os.path.dirname(__file__)
    thisPath = os.path.join(thisDir,'')
    execFile = os.path.join(thisPath, "root.py")
    exec(open(execFile).read())