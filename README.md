# SedEdu

SedEdu is a suite of educational activities related to geomorphology and sedimentology. The suite is targeted at grade school educators who want to bring enagaging, interactive, and scientifically relevant activities into their classroom. SedEdu is built entirely in Python and is *free and open source* software. Modules included in SedEdu are built by reseachers at the cutting edge of their fields and are designed to showcase their research in a digestable manner.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for use in the classroom. See "Contributing" for information on becoming a part of the SedEdu project.

SedEdu runs in Python (v3) and utilizes PyQt5 for rendering the interface. Modules rely on scipy, matplotlib, Tkinter, Pygame, and Shapely. You can check your python version by running: 

```
python3 -V
```

in a terminal. It is recommended you install the needed dependencies through `pip3`.

### Installing dependencies
push to separate `installation.md` file?

#### Windows instructions

#### MacOSX instructions

#### Linux instructions

Install the needed python3 system libraries:

```
sudo apt install python3 python3-pip python3-tk
```

Install the needed python3 packages:
```
pip3 install pyqt5 scipy numpy matplotlib pygame shapely
```

### Installing SedEdu

instructions for installing through pip, using either PyPI or from GitHub are forthcoming (see milestones).

For now, you can clone the git repository to get the lastest version

```
git clone https://github.com/amoodie/sededu.git
```

and run SedEdu with:

```
python3 sededu/run_sededu.py
```

### Running the program

A step by step series of examples

```
python3 <your-path-to-sededu>/run_sededu.py
```

installation through pip to give an executable?


## Contributing

Please read [CONTRIBUTING.md](https://github.com/amoodie/sededu/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.


## Authors

* **Andrew J. Moodie** - *2 modules* - [github.com/amoodie](https://github.com/amoodie)
* **Kensuke Naito** - *1 module* - [github.com/kensukename2](https://github.com/kensukename2)
* **Jeffrey Kwang** - *1 module* - [github.com/jeffskwang](https://github.com/jeffskwang)

See also the list of [contributors](https://github.com/amoodie/sededu/graphs/contributors) who have participated in this project in other ways.


## License

This project is licensed under the GNU GPL License - see the [full license](https://github.com/amoodie/sededu/blob/master/LICENSE.md) file for details. It is provided without warranty or guaranteed support.


## Acknowledgments

The SedEdu framework was created by Andrew J. Moodie but has been built through the efforts of many authors (see Authors above). The authors have been supported by: 
* The National Science Foundation under Grant Nos. 1427262 and 1450681. 

### Disclaimer

Any opinion, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of any funding agency.