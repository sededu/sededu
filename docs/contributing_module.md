# Contributing a module

If you want to contribute a module, this file will guide you through the necessary steps --- whether your module exists already, or you only have an idea!

Let this document serve as a roadmap to writing your module, but be patient as this roadmap will send you off on scenic tours to other documents which help provide complete information about SedEdu and contributing a module.

A "module" (the term used throughout the documentation) is a self-contained codebase that provides 1) an interactive interface, 2) demonstrates a sediment-related concept through interaction with that interface, and 3) has some worksheet/activities that accompany the interface to guide the user along. 
So, your module is actually really able to stand on its own and only gets incorporated into SedEdu later (which is really easy!).
The logical structure of this document follows that workflow of first writing the module, then incorporating it into the SedEdu suite.

A _thoroughly documented complete working module_ has been included with the SedEdu distribution to provide an example a module could be based off of.
Find the complete module in `docs/example-module/` or [on GitHub here](https://github.com/amoodie/example-module_sededu).
There is also a "template" module for your use in developing, it provides an empty shell of what could become a module; basically, the files and folders are all there, they're just empty.

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

As discussed above, your module is really a stand-alone application. 
To this end, the mdoule must contain a few key files and then can have many more. 
The _minimum required files for your module to be complete_ are: 

* `README.md` -- here is a template
* `LICENSE.txt` -- see [below](#licensing), and [Module Licensing](https://github.com/amoodie/sededu/blob/develop/docs/contributing_module.md#module-licensing)
* executable python script

Then, to incorporate into SedEdu, all you are required to add is an `about.json` file that provides SedEdu with some documentation about your module.
A potential folder structure for your module, which separates components logically, is below: 

```
module/
├── docs
│   ├── activity
│   └── activity
├── private
│   ├── image1
│   ├── image2
│   └── data1
├── src
│   ├── executable-code.py
│   └── helper-functions.py
├── about.json
├── LICENSE.txt
└── README.md
```

The module root is the `module` folder. 
In the root, we have three folders to separate the source code (`src`), from the supporting data (`private`), from the activities that go along with the module (`docs`).
This root folder is also where the `README.md`, a `LICENSE.txt` file, and the `about.json` files should be.



## Writing the module

You should write your module to rely _only_ on Python3 and no other programming languages. 
This is to ensure that SedEdu remains easily deployable.

You are free however to use an array of Python packages within your module. 
Currently, SedEdu requires `scipy`, `matplotlib`, `pygame`, and `shapely` during installation, so you can safely use those packages.
All the packages included in the [Python Standard Library]](https://docs.python.org/3/library/) are also available for use in modules (there's a ton!).

There is no hard cap on the maximum disk size allowable for your module, but in keeping with an easily deployable SedEdu please keep modules < 1.5 MB.
If including activity sheets exceeds this limit, that will be fine.
If your module requires larger data, please consider downloading it from the web in real time, _after confirming this activity from the user first_.

The biggest resource provided to you here for writing your module would be the example module.
The README of this module has a thorough description of the workflow of designing a module.
Find the complete example module in `docs/example-module/` or [on GitHub here](https://github.com/amoodie/example-module_sededu).
Furthermore, all of the modules included in SedEdu are open source, so you can view the source code for a given project for a hint on 'how-to', or inspiration for module ideas.


### The `about.json` file
Integrating your module into SedEdu requires a special file describing the module, called `about.json`.



### Writing activities for your module

Modules are cool on their own, but to really make them effective teaching tools, it is necessary to have some guiding documentation to make sure the user is getting the important points from your module.
Writing activities for a module can be difficult, though.

There is a separate article dedicated to Writing Activities for your module available with your distribution in `docs/writing_activities.md` or [on GitHub here](https://github.com/amoodie/sededu/blob/develop/docs/writing_activities.md).
You can also look to other activities in the SedEdu suite for inspiration.


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

