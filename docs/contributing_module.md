# Contributing a module

If you want to contirbute a module, this file will guide you through the necessary steps --  whether your module exists already, or you only have an idea!

## File structure of module

### Writing the module (supported package use)
enumerate allowed packages here, this is already in the readme?

### The `about.json` file
see the additional document for more details

## Adding your module to SedEdu
submodules?

example: git submodule add https://github.com/amoodie/rivers2stratigraphy sededu/modules/stratigraphy/rivers2stratigraphy

https://gist.github.com/gitaarik/8735255



## Common challenges

#### Cannot find files
Your module will be executed from the location of SedEdu program, so you must determine the location of your files to specify. To load a file in the same directory as your executable called `DEM.txt` try:

```
import numpy as np
import os

this_dir = os.path.dirname(__file__)
this_path = os.path.join(this_dir,'')
DEM = np.loadtxt(os.path.join(this_path, 'DEM.txt'))

```