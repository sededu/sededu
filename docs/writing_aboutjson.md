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
    "projurl": "[hosted on GitHub](https://github.com/amoodie/example-module_sededu/)",
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

__NOTE:__ that each JSON entry is ended with a comma, the final _blank line_ at the end of the document and that there are _no comments_.



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

_string_, the module title. Supports UTF-8 characters.


### author

_string_, the author(s) of the module. Can be multiple people, will be printed exactly as written. Supports UTF-8 characters.


### version

_string_, the version number of the module. Will be printed exactly as written.

Examples:
```
"version": "1.0",
"version": "0.9.1",
```

### shortdesc

_string_, a short description of what the module is about and what happens with it. Keep to < 70 characters. Will be printed exactly as written.


### license

_string_, the licensing of the module. Use abbreviation if possible. Will be printed exactly as written.

Examples:
```
"license": "MIT",
"license": "GNU GPL v3",
```

### difficulty
_integer_, a measure of the difficulty of the science covered by the module. 
Should be ranked between 1 and 10 (inclusive). 
Intention is to use this number to sort the modules on the CategoryPage.

_Currently does nothing and is not used._


### longdesc
_string_, a paragraph length description of the module. Supports UTF-8 characters. Currently does nothing and is not used. Intention is to have this field mapped into a scrollable text box of specific height on the ModuleInfoPage. No support for linebreaks in the `about.json` file -- should be read from an auxiliary file?

_Currently does nothing and is not used._


### projurl
_string_, the home page of the module. Will parse out Markdown formatted link, allowing for "link shortening" behind the scenes.
<!-- If Markdown is not detected, input will be printed exactly as written as a link. -->

Examples:
```
"projurl": "[hosted on GitHub](https://github.com/amoodie/example-module_sededu/)",
"projurl": "https://github.com/amoodie/example-module_sededu/",
```

### projreadme
_list of strings_, _string_, the README for the module. If a list of strings is given, a relative path is generated with respect to the module root. 
<!-- If a string is given, it is converted to a url link. -->

Examples:
```
"projreadme": ["README.md"],
"projreadme": "https://github.com/amoodie/example-module_sededu/README.md",
``` 
    
### preview
The preview will be scaled to 250 pixels in height, and then cropped to the center of the image at a 4:3 aspect ratio (W:H).

Examples:
```
"preview": ["private", "example-module_demo.png"],
```

### exec

Examples:
```
"exec": ["src", "example-module.py"],
```

### docloc

Examples:
```
"docloc": ["docs"],
```

### doclist

Examples:
```
"doclist": {
    "theory.md": "Theory behind the model framework", 
    "worksheet.md": "Worksheet"
},
```


## Developers

If you propose to make any changes to the interaction with `about.json` files you __must__ maintain backwards compatibility.
You can use aliases to do so.

