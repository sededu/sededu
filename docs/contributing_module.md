# Contributing a module

If you want to contribute a module, this file will guide you through the necessary steps --- whether your module exists already, or you only have an idea!

Let this document serve as a roadmap to writing your module, but be patient as this roadmap will send you off on scenic tours to other documents which help provide complete information about SedEdu and contributing a module.

A "module" (the term used throughout the documentation) is a self-contained codebase that provides 1) an interactive interface, 2) demonstrates a sediment-related concept through interaction with that interface, and 3) has some worksheet/activities that accompany the interface to guide the user along. 
So, your module is actually really able to stand on its own and only gets incorporated into SedEdu later (which is really easy!).
The logical structure of this document follows that workflow of first writing the module, then incorporating it into the SedEdu suite.

A _thoroughly documented complete working module_ has been included with the SedEdu distribution to provide an example a module could be based off of.
Find the complete module in `docs/example-module/` or [on GitHub here](https://github.com/amoodie/example-module_sededu).
There is also a "template" module for your use in developing, it provides an empty shell of what could become a module; basically, the files and folders are all there, they're just empty.

Table of contents of this document:

* [File structure of module](#file-structure-of-module)
* [Writing the module](#writing-the-module)
* [Adding your module to SedEdu](#adding-your-module-to-sededu)
* [Common challenges along the way](#common-challenges-along-the-way)


Quick-links to other documentation:

* an example module with basic slider functionality ([`example-module`](https://github.com/amoodie/example-module_sededu))
* [writing the `about.json` file](https://github.com/amoodie/sededu/blob/develop/docs/writing_aboutjson.md)
* [pull request checklist](https://github.com/amoodie/sededu/blob/develop/docs/pull_request_checklist.md)



## File structure of module

As discussed above, your module is really a stand-alone application. 
To this end, the mdoule must contain a few key files and then can have many more. 
The _minimum required files for your module to be complete_ are: 

* `README.md` -- here is a template
* `LICENSE.txt` -- see [below](#licensing), and [Module Licensing](https://github.com/amoodie/sededu/blob/release/docs/contributing_module.md#module-licensing)
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


### Module philosophy

The objective of SedEdu is to offer an array of tools that educators can use throughout their curriculum, in whatever way they see fit.
To this end, it is important that SedEdu offer a __spectrum of module difficulties__, and each module __cover a single topic__.
Please bear these considerations in mind when deciding what topic you will teach through your module.


### Some technical notes

You should write your module to rely _only_ on Python3 and no other programming languages. 
This is to ensure that SedEdu remains easily deployable.
It is also crucial that you design your module to be OS agnostic by using Python's `os.path` utilities for file resources.

You are free however to use an array of Python packages within your module. 
Currently, SedEdu requires `scipy`, `matplotlib`, `pillow`, and `shapely` during installation, so you can safely use those packages.
All the packages included in the [Python Standard Library](https://docs.python.org/3/library/) are also available for use in modules (there's a ton!).

There is no hard cap on the maximum disk size allowable for your module, but in keeping with an easily deployable SedEdu please keep modules < 1.5 MB.
If including activity sheets exceeds this limit, that will be fine.
If your module requires larger data, please consider downloading it from the web in real time, _after confirming this activity from the user first_.

The biggest resource provided to you here for writing your module would be the example module.
The README of this module has a thorough description of the workflow of designing a module.
Find the complete example module in `docs/example-module/` or [on GitHub here](https://github.com/amoodie/example-module_sededu).
Furthermore, all of the modules included in SedEdu are open source, so you can view the source code for a given project for a hint on 'how-to', or inspiration for module ideas.
Finally, there are materials available form a clinic at CSDMS 2019 [available here](https://github.com/sededu/CSDMS_clinic).

### The `about.json` file
Integrating your module into SedEdu requires a special file describing the module, called `about.json`.
There are a number of required and optional fields in the file that provide information about your module to SedEdu to display to the user.
__It is really important this file is configured properly.__

A separate file about [Writing about.json](https://github.com/amoodie/sededu/blob/release/docs/writing_aboutjson.md) exists to describe the `about.json` file in detail.



### Writing activities for your module

Modules are cool on their own, but to really make them effective teaching tools, it is necessary to have some guiding documentation to make sure the user is getting the important points from your module.
Writing activities for a module can be difficult, though.

There is a separate article dedicated to Writing Activities for your module available with your distribution in `docs/writing_activities.md` or [on GitHub here](https://github.com/amoodie/sededu/blob/release/docs/writing_activities.md).
You can also look to other activities in the SedEdu suite for inspiration.


### Module Licensing

You will need to add a license to your module and GitHub repository before it will be incorporated into SedEdu.
At the very least, your module needs to be licensed to allow the module to be incorporated into larger software projects (e.g., SedEdu).

We recommend the [MIT license](https://choosealicense.com/licenses/mit/) first, and then the [GNU GPLv3 license](https://choosealicense.com/licenses/gpl-3.0/).
Simply create a file called `LICENSE.txt` and copy-paste the contents of the license into that file.

For more help choosing a license see [GitHub on licenses](https://help.github.com/articles/licensing-a-repository/) or [choosealicense.com](https://choosealicense.com/)


### Putting your module on GitHub

The [method that SedEdu uses](#adding-your-module-to-sededu) to incorporate modules requires that your project be hosted on GitHub in a repository.
This is easy and there are _tons_ of resources available to help guide you.
Therefore, the entire process isn't repeated here, but a brief description is below.

1. create an account or login to GitHub. [[link to login]](https://github.com/login).
1. create a new repository. [[link to instructions]](https://help.github.com/articles/creating-a-new-repository/)
1. install `git` on your machine. [[link to instructions]](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
1. initialize the repository locally, commit everything, push to GitHub. [[link to instructions]](https://help.github.com/articles/adding-a-file-to-a-repository-using-the-command-line/)



## Adding your module to SedEdu

Modules are incorporated into SedEdu through the use of `git submodule`s.
This allows SedEdu to easily incorporate upstream changes in your module without having to maintain project history for each module. 
This is important, because it simplifies the workflow for keeping SedEdu up to date.
However, it requires developers to have some familiarity with `git` and GitHub.
By this point your project should be on GitHub (see [Putting your module on GitHub](#putting-your-module-on-github)).
You should also have a development copy of the SedEdu project repository, for development (see [SedEdu development workflow](https://github.com/sededu/sededu/blob/release/CONTRIBUTING.md#sededu-development-workflow))

Follow the (OS agnostic) instructions below to add your module to SedEdu.

1. Using a terminal (or git bash on windows), change working directory to the root of your development SedEdu repository.
1. create a new branch from development: `git checkout -b module_<module-name> develop` where `<module-name>` is a short name of your module.
1. Visit the webpage of your repository and click on the green "Clone or download" button and copy the link to your clipboard.
1. add your new `git submodule` with: `git submodule add -b <branch-name> <the-https-link-to-github-repository-you-just-copied> sededu/modules/<category>/<module-name>` where `<the-https-link-to-github-repository-you-just-copied>` is the link you copied to your module's GitHub repository, `<category>` is the category you think your module best fits in, `<branch-name>` is the name of your __stable__ branch (see below), and `<module-name>` is some unique short name for your module. See the example below!
1. add yourself to the author list on `README.md` (see [Authorship](https://github.com/sededu/sededu/blob/release/CONTRIBUTING.md#authorship))
1. increment the minor version number in SedEdu, which is located at `sededu/_version.py`.
1. add the new module and text changes to your commit: `git add .` and `git commit -m "added new submodule <name-of-your-module> in <category>"`
1. push your changes to a branch on your GitHub SedEdu fork: `git push origin module_<module-name>`
1. ensure you have done everything on the [Pull Request Checklist](https://github.com/sededu/sededu/blob/release/docs/pull_request_checklist.md) and open a pull request to have your module addition reviewed and incorporated into SedEdu!

For an example of adding a submodule command, the "Rivers to Stratigraphy" module was added to SedEdu by issuing the command:
```
git submodule add -b master https://github.com/sededu/rivers2stratigraphy sededu/modules/stratigraphy/rivers2stratigraphy
```

__IMPORTANT NOTE FOR MODULE DEVELOPERS:__ it is really important that whatever your default GitHub repository branch is when you add the module to SedEdu remain stable. 
Periodically (every 6 months) all submodules are checked for updates and changes are automatically incorporated into the next SedEdu release version.
If the branch you maintain changes, the changes will not be incorporated into SedEdu unless you update the `.gitmodules` file.
If the module becomes broken or unstable, these changes will be incorporated into SedEdu! 
Prevent this from happening by maintaining a stable branch!
https://gist.github.com/gitaarik/8735255



## Common challenges along the way

Below are challenges that have been encountered in the past by developers trying to add modules to SedEdu.
This list is dynamic, [open an issue](https://github.com/sededu/sededu/issues) if you thing something should be added. 

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

#### README on module page is formatted as plain text

If you are getting a path formatted as a plain text (i.e., not a link), triple check the path you are giving. 
The triple check that there is actually a file there with the exact name you think it is.
The program checks if there is a file at the path and if there is, it will convert to a link to the path.
So if you have no link, then the path does not point to a file.
