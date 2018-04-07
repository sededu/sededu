# Writing the about.json file

This document provides support for writing the modules "documentation" file in the format that SedEdu requires: the `about.json` file.

A sample `about.json` file can be found in the `example-module` folder in `docs/example-module/about.json` or [on GitHub](https://github.com/amoodie/example-module_sededu/blob/master/about.json), and is also listed in the next section.
A blank template `about.json` file is available in the `template-module` folder in `docs/template-module/about.json` or [on GitHub](https://github.com/amoodie/template-module_sededu/blob/master/about.json).



## What is the about.json file

From [JSON.org](https://www.JSON.org):

> JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. ... JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language.

In SedEdu we use JSON because it is easy to write for a module contributor. 
There are several required fields, and some optional fields, in the `about.json` file. 
Unrecognized fields will be ignored.
Note that leaving out a required field won't cause SedEdu to fail to load your module, but will result in defaults being inserted instead.
Also note that the order of the fields in your `about.json` file does not matter. 

The `about.json` from the complete example module is listed below:

```
{
    "title": "An example module for SedEdu",
    "author": "Andrew J. Moodie",
    "version": "1.0",
    "shortdesc": "A simple model implementation to demonstrate a module in SedEdu",
    "license": "MIT",
    "difficulty": 1,
    "projurl": "https://github.com/amoodie/example-module_sededu.git",
    "projreadme": ["README.md"],
    "preview": ["private", "example-module_demo.png"],
    "exec": ["src", "example-module.py"],
    "docloc": ["docs"],
    "doclist": {
        "theory.md": "Theory behind the model framework", 
        "worksheet.md": "Worksheet"
    }
}

```

__NOTE:__ the _blank line_ at the end of the document and that there are _no comments_!



## Where to put the about.json file
The `about.json` __must__ be located in the root of the module repository. See the [example module](https://github.com/amoodie/example-module_sededu/) and [template module](https://github.com/amoodie/template-module_sededu/).



## Supported fields

Available fields are listed below, fields listed in __bold__ are mandatory. More information about each field is enumerated below. 

* __title__
* __author__
* __version__
* __shortdesc__
* __license__
* __difficulty__
* longdesc
* projurl
* projreadme
* preview
* exec
* docloc
* doclist

### title
will be trimmed to ?? length

### author


### longdesc


### preview


### title

### author

A string, the author(s) of the module. Can be multiple people, will be printed exactly as written. UTF support?

### version

### shortdesc

### license

### difficulty
An integer, a measure of the difficulty of the science covered by the module. 
Should be ranked between 1 and 10 (inclusive). 
Intention is to use this number to sort the modules on the CategoryPage.

_Currently does nothing and is not used._

### longdesc
A string, a paragraph length description of the module. Currently does nothing and is not used. Intention is to have this field mapped into a scrollable text box of specific height on the ModuleInfoPage. No support for linebreaks in the `about.json` file -- should be read from an auxiliary file?

_Currently does nothing and is not used._

### projurl

### projreadme

### preview
The preview will be scaled to 250 pixels in height, and then cropped to the center of the image at a 4:3 aspect ratio (W:H).

### exec

### docloc

### doclist
