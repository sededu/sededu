# Writing the about.json file

This document provides support for writing the modules "documentation" file in the format that SedEdu requires: the `about.json` file.

A sample `about.json` file can be found in the `sample_module` folder [(link to folder)](https://github.com/amoodie/sededu/docs/sample_module)

## what is the about.json file
 describe json briefly

 Required vs optional fields, note that leaving out req fields won't cause failure, but will result in default strings.

 Note that the order of the fields in your `about.json` file does not matter. 

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

## where to put the about.json file
in the root of the module. see sample_module.

## Supported fields

Available fields are listed below, fields listed in __bold__ are mandatory. More information about each field is enumerated below. 

* __title__
* __author__
* __version__
* __shortdesc__
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
Can be multiple people, will be printed exactly as written. UTF support?

### longdesc
No support for linebreaking!

### preview
The preview will be scaled to 250 pixels in height, and then cropped to the center of the image at a 4:3 aspect ratio (W:H).