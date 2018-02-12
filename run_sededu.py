import os
# from sededu import sededuGUI

## check dependencies?



## import packages?



## initialize the GUI
thisDir = os.path.dirname(__file__)
thisPath = os.path.join(thisDir,'')
exec(open(thisPath + "sededu/sededuGUI.py").read())