# rain_table
Interactive rain table model written by Jeffrey Kwang at UIUC.

This repository contains 3 files. In order to run the model ('rain_table.py'), python 2.7 needs to be installed along with the library pygame (https://www.pygame.org).

For example, Python 2.7 can be installed with the anaconda pacakge (https://www.anaconda.com/download/) or Python(x,y) (https://python-xy.github.io/downloads.html). 

After python is installed, pygame can be installed via the cmd prompt or linux terminal. Use 'pip install pygame'.

The list of the files

(1) rain_table.py: This file contains the source code to run the rain table simulation. Simply run the model in python, and click the screen to drop rain on the screen. The rain will be routed on the landscape in accordance to the d8, steepest decent algorithm (see O’Callaghan and Mark, 1984).

(2) dem.txt: this file contains the digital elevaiton model that is rendered on the screen. This DEM's source is the 1/3 arcsecond USGS DEM product. The name of this particular watershed is Baisman Run in Baltimore Country, MD (LOC: Lat 39°28'46.1", long 76°40'40.9"). File is a ersi formatted ascii.

(3) dir.txt: this file contains the d8 flow direction data. File is a ersi formatted ascii.

Current user defined parameters in rain_table.py:
scale -> this parameter scales the original dem grid (pixel length by pixel width) to window that is [(pixel length x scale) by (pixel width x scale)]

rad -> this parameter controls the pixel radius of the rain cloud

f_rate -> this parameter controls the frame rate of the simulation. It is set to 60 as the default because most computer screens' refresh rates are 60 Hz.

References

O’Callaghan, J. F. and Mark, D. M.: The extraction of drainage networks from digital elevation data, Computer Vision, Graphics, and Image Processing, 28(3), 323–344, doi:10.1016/S0734-189X(84)80011-0, 1984.
