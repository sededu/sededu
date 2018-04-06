# Contributing a module

If you want to contribute a module, this file will guide you through the necessary steps --- whether your module exists already, or you only have an idea!

Let this document serve as a roadmap to writing your module, but be patient as this roadmap will send you off on scenic tours to other documents which help provide complete information about SedEdu and contributing a module.

A "module" (the term used throughout the documentation) is a self-contained codebase that provides 1) an interactive interface, 2) demonstrates a sediment-related concept through interaction with that interface, and 3) has some worksheet/activities that accompany the interface to guide the user along. 
So, your module is actually really able to stand on its own and only gets incorporated into SedEdu later (which is really easy!).
The logical structure of this document follows that workflow of first writing the module, then incorporating it into the SedEdu suite.


A _thoroughly documented complete working module_ has been included with the SedEdu distribution to provide an example a module could be based off of.
Find the complete module in `docs/example-module/` or [on GitHub here](https://github.com/amoodie/example-module_sededu)
Some of the text below is borrowed from there.

There is also a "template" module for your use in developing, it provides an empty shell of what could become a module.
Basically, the files and folders are all there, they're just empty.

Links to other documentation:

* 
* 
* 
* 

Table of contents of this document:

* [File structure of module](#file-structure-of-module)
* 
* 
* 


## File structure of module

You can view a [literal tree of an example module here](https://github.com/amoodie/example-module_sededu#folder-and-file-organization), but the purpose of this section is to describe more conceptually how a module needs to be structured internally, and then how exactly this module gets incorporated into the structure of SedEdu.





To make your module "SedEdu ready" really all you need is 1) a specific `about.json` file which documents your module and 2) a licen


The `about.json` file just contains some simple information which gets displayed/used within SedEdu; see [Contributing a Module](https://github.com/amoodie/sededu/blob/feat_documentation/docs/contributing_module.md) and [Writing about.json](https://github.com/amoodie/sededu/blob/feat_documentation/docs/writing_aboutjson.md) for more information about this file's contents.
The `.gitignore` file is a GitHub related file that tells your local repository which files to sync with the remote GitHub repository (you don't need to worry about this right now)


## Writing the module (supported package use)
enumerate allowed packages here, this is already in the readme?


### The `about.json` file
see the additional document for more details


### Writing activities for your module


### Module Licensing

You will need to add a license to your module and GitHub repository before it will be incorporated into SedEdu.
At the very least, your module needs to be licensed to allow the module to be incorporated into larger software projects (e.g., SedEdu).

We recommend the [MIT license](https://choosealicense.com/licenses/mit/) first, and then the [GNU GPLv3 license](https://choosealicense.com/licenses/gpl-3.0/).
Simply create a file called `LICENSE.txt` and copy-paste the contents of the license into that file.

For more help choosing a license see [GitHub on licenses](https://help.github.com/articles/licensing-a-repository/) or [choosealicense.com](https://choosealicense.com/)


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

