<img src="https://raw.githubusercontent.com/sededu/sededu/develop/private/sededuicon_hires.png" width="250">

[![Build Status](https://github.com/sededu/sededu/actions/workflows/build.yaml/badge.svg?branch=develop)](https://github.com/sededu/sededu/actions/workflows/build.yaml)

[![Anaconda-Server Badge](https://anaconda.org/sededu/sededu/badges/version.svg)](https://anaconda.org/sededu/sededu)
[![PyPI version](https://badge.fury.io/py/sededu.svg)](https://badge.fury.io/py/sededu)

<!-- [![Anaconda-Server Badge](https://anaconda.org/sededu/sededu/badges/platforms.svg)](https://anaconda.org/sededu/sededu) -->

<!-- # SedEdu -->
SedEdu is a suite of educational activities related to geomorphology and sedimentology. 
The suite is targeted at educators who want to bring engaging, interactive, and scientifically relevant activities into their classroom. 
SedEdu is built __entirely in Python and is free and open source__ software. 
Modules included in SedEdu are built by researchers at the cutting edge of their fields and are designed to showcase their research in a digestible manner.

<img src="https://raw.githubusercontent.com/sededu/sededu/develop/private/sededu_demo.png" width="600" align="center">
    


# Getting Started

These instructions will get you a copy of the project up and running on your local machine for use in the classroom. 
See [Contributing to SedEdu](#contributing-to-sededu) for information on becoming a part of the SedEdu project.


## Installing dependencies

SedEdu runs in Python 3 and utilizes PyQt5 for rendering the graphical user interface. 
Modules included in SedEdu rely on `scipy`, `matplotlib`, `pillow`, and `shapely`. 

You can check your Python version by running: `python3 -V` in a terminal. 
Note that you may need to specify the path to your Python executable on some systems.
If you do not have Python 3 installed, you will need to do so to use SedEdu. 
This will not disrupt an existing Python 2.x installation, if you rely on that for other uses.

If you are new to Python, __it is strongly recommended that you install Anaconda Python__, which is an open source distribution of Python which includes many basic scientific libraries, some of which are used in the module. 
Anaconda can be downloaded at https://www.anaconda.com/download/ for Windows, macOS, and Linux. 
If you do not have storage space on your machine for Anaconda or wish to install a smaller version of Python for another reason, see below on options for Miniconda or vanilla Python.

1. Visit the website for Anaconda https://www.anaconda.com/download/ and select the installer for your operating system.
__Be sure to select the Python 3.x installation.__
2. Start the installer.
3. If prompted, select to "install just for me", unless you know what you are doing.
4. When prompted to add Anaconda to the path during installation, select _yes_ if you __know__ you do not have any other Python installed on your computer; otherwise select _no_.
5. If you received no errors, proceed to installing below.


If you want a more flexible and lightweight Python distribution, you can use whatever your favorite package manager is distributing (e.g., `homebrew` or `apt`), check the [Windows downloads here](https://www.python.org/downloads/windows/), or compile [from source](https://www.python.org/downloads/source/). 
If you go this route, you will need to also install `pip3`, PyQt5 (`python3-pyqt5`), and the dependency python packages listed below. 

Note that on Linux, users may need to specify an installation of `pyqt` and/or `tkinter` directly from `apt`:
Install PyQt5:

```
sudo apt install python3-pyqt5 python3-tk
```


## Installing SedEdu

If you installed Anaconda Python or Miniconda, you can follow the instructions below for your operating system. 
Otherwise see the instructions for PyPi installation below.

__Please__ [open an issue](https://github.com/sededu/rivers2stratigraphy/issues) if you encounter any troubles installing or any error messages along the way! 
Please include 1) operating system, 2) installation method, and 3) copy-paste the error.

### Windows users

1. Open your "start menu" and search for the "Anaconda prompt"; start this application.

2. Install with the module type the following command and hit "enter":
```
conda install -c sededu sededu
```
If asked to proceed at either step, type `Y` and press "enter" to continue installation. 
3. This process may take a few minutes as the necessary source code is downloaded.
If the installation succeeds, proceed below to the "Run the module" section.

__Note on permissions:__ you may need to run the Anaconda prompy "as administrator" on Windows.


### Mac OSX and Linux users

1. Install the module by opening a terminal and typing the following command.
```
conda install -c sededu sededu
```
If asked to proceed at either step, type `Y` and press enter to continue installation.
2. This process may take a few minutes as the necessary source code is downloaded.
If the installation succeeds, proceed below to the "Run the module" section.

__Note on permissions:__ you may need to use `sudo` on OSX and Linux.


### Advanced user installations

__Install with pip__
To install with `pip` from Pypi use (not recommended for entry-level users):
```
pip3 install pyqt sededu
```
or in the event of a failed install, try:
```
pip3 install pyqt5 sededu
```

See below instructions for downloading the source code if you wish to be able to modify the source code for development or for exploration.


__Install by cloning the repository__

_Developers see below:_
You can clone the git repository to get the latest release version with:
```
git clone --recurse-submodules -b release https://git@github.com/sededu/sededu.git
```
and SedEdu is then run with:
```
python3 sededu/run_sededu.py
```

Note that if you have no modules: run `git submodule update --init --recursive`.

### Running SedEdu

1. Open a Python shell by typing `python` (or `python3`) at the terminal (OSX and Linux users) or at the Anaconda / Command Prompt (Windows users).
2. Run the module from the Python shell with:
```
import sededu
```
Instructions will indicate to use the following command to then run the module:
```
sededu.run()
```

Alternatively, you can do this in one line from the standard terminal with:
```
python -c "import sededu; sededu.run()"
```



Alternatively, run the module with provided script:
```
python3 <path-to-installation>run_sededu.py
```

Please [open an issue](https://github.com/sededu/sededu/issues) if you encounter any additional error messages! 
Please include 1) operating system, 2) installation method, and 3) copy-paste the error.


### Troubleshooting

* __SedEdu won't launch:__ you're probably missing some Python or PyQt dependencies. If you `pip install`ed, did you install `pyqt`? Linuz users: try `sudo apt install python3-pyqt5`.

* __There are no modules in SedEdu:__ you probably didn't get the submodules when you `git clone`d. Try `git submodule update --init --recursive` inside the cloned repository.



# Contributing to SedEdu

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

The SedEdu project needs contributions from the community to be successful.
However, there are __many different ways you can contribute!__
You do not even need to write code to contribute to SedEdu.
Some opportunities for contributions are listed below (in no particular order):

* write (code) a standalone interactive module
* write an activity for an existing module
* write (code) features and bug fixes for existing modules
* write (code) features and bug fixes for SedEdu
* write documentation for SedEdu

Please read [CONTRIBUTING.md](https://github.com/sededu/sededu/blob/release/CONTRIBUTING.md) for details on our code of conduct, and the process for contributing to SedEdu (which includes any pull request).



### Developer installation

Dev channel stats:
[![Build Status](https://github.com/sededu/sededu/actions/workflows/build.yaml/badge.svg?branch=develop)](https://github.com/sededu/sededu/actions/workflows/build.yaml)
[![Coverage Status](https://coveralls.io/repos/github/sededu/sededu/badge.svg?branch=tests)](https://coveralls.io/github/sededu/sededu?branch=tests)

You should get the entire repository and work off of the `develop` branch:

```
git clone --recurse-submodules https://github.com/sededu/sededu.git
git checkout -b <name-of-working-branch> develop
```

If you have already `git clone`d and need to pull the submodules now try:

```
git submodule update --init --recursive
```

See [CONTRIBUTING.md](https://github.com/sededu/sededu/blob/release/CONTRIBUTING.md) for more information on the preferred `git` workflow for SedEdu, including a note on hot-fixes.



# Authors

* **Andrew J. Moodie** - *3 modules* - [github.com/amoodie](https://github.com/amoodie)
* **Kensuke Naito** - *1 module* - [github.com/kensukename2](https://github.com/kensukename2)
* **Jeffrey Kwang** - *1 module* - [github.com/jeffskwang](https://github.com/jeffskwang)

See also the list of [contributors](https://github.com/sededu/sededu/graphs/contributors) who have participated in this project in other ways.



# License

This project is licensed under the GNU GPL License - see the [full license](https://github.com/sededu/sededu/blob/release/LICENSE.txt) file for details.
It is provided without warranty or guaranteed support.
Each submodule may be licensed under a different license, please see the relevant module's license file, README, or project homepage for more information.



# Acknowledgments

The SedEdu framework was created by Andrew J. Moodie but has been built through the efforts of many authors (see Authors above).
The authors have been supported by:
* The US National Science Foundation under Grant Nos. 1427262 and 1450681.



# Disclaimer

Any opinion, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of any funding agency.
