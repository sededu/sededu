# Contributing a module

If you want to contribute a module, this file will guide you through the necessary steps --  whether your module exists already, or you only have an idea!



## File structure of module



## Writing the module (supported package use)
enumerate allowed packages here, this is already in the readme?


### The `about.json` file
see the additional document for more details


### Writing activities for your module


### Module Licensing


## Adding your module to SedEdu
submodules?

cd into the git repository and use git submodule add to add your module to the SedEdu repository:
```
git submodule add https://github.com/amoodie/rivers2stratigraphy sededu/modules/stratigraphy/rivers2stratigraphy
```

IT IS REALLY IMPORTANT TO KEEP YOUR DEFAULT BRANCH STABLE!!!!

https://gist.github.com/gitaarik/8735255

how to update the submodules periodically:
```
git submodule foreach git pull
```



## Updating SedEdu metadata
https://semver.org/



## Open a pull request
TEST TEST TEST! Please make sure you have stable module.
Open PR to stable
http://nvie.com/posts/a-successful-git-branching-model/
http://nvie.com/files/Git-branching-model.pdf



## Common challenges

Below are challenges that have been encountered in the past by developers trying to add modules to SedEdu.
This list is dynamic, [open an issue](https://github.com/amoodie/sededu/issues) if you thing something should be added. 

#### Cannot find program files

Your module will be executed from the location of SedEdu program, so you must determine the location of your files to specify. To load a file in the same directory as your executable called `DEM.txt` try:

```
import numpy as np
import os

this_dir = os.path.dirname(__file__)
this_path = os.path.join(this_dir,'')
DEM = np.loadtxt(os.path.join(this_path, 'DEM.txt'))
```

#### Cannot find activity/worksheet files

Make sure the path specified in `about.json` is correct. I have made the mistake of specifying 

```
"docloc": ["docs"],
```

when I should have been specifying 

```
"docloc": ["doc"],
```

