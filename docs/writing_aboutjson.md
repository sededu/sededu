# Writing the about.json file

This document provides support for writing the modules "documentation" file in the format that SedEdu requires: the `about.json` file.

A sample `about.json` file can be found in the `example-module` folder in `docs/example-module/about.json` or [on GitHub](https://github.com/amoodie/example-module_sededu/blob/release/about.json), and is also listed in the next section.
A blank template `about.json` file is available in the `template-module` folder in `docs/template-module/about.json` or [on GitHub](https://github.com/amoodie/template-module_sededu/blob/release/about.json).



## What is the about.json file

From [JSON.org](https://www.JSON.org):

> JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. ... JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language.

In SedEdu we use JSON because it is easy to write for a module contributor. 
There are several required fields, and some optional fields, in the `about.json` file. 
Unrecognized fields will be ignored.
Note that leaving out a required field won't cause SedEdu to fail to load your module, but will result in defaults being inserted instead, and the module probably won't work correctly.
Also note that the order of the fields in your `about.json` file does not matter. 

The `about.json` from the complete example module is listed below:

```json
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

__NOTE:__
* each JSON entry is ended with a comma, 
* use of double quotation marks
* a final _blank line_ at the end of the document 
* there are _no comments_

If you do not have something to fill in an optional key field, __remove the field completely__. 
If you leave a blank pair of double-quotes, the field may be printed in SedEdu, but simply be blank.

## Where to put the about.json file
The `about.json` __must__ be located in the root of the module repository. See the [example module](https://github.com/sededu/example-module_sededu/) and [template module](https://github.com/sededu/template-module_sededu/).



## Supported fields

Available fields are listed below, fields listed in __bold__ are mandatory.
More information about each field is enumerated below. 

* __title__
* __author__
* __version__
* __shortdesc__
* __license__
* __difficulty__
* __exec__
* longdesc
* projurl
* projreadme
* preview
* docloc
* doclist

JSON calls "objects" what syntactically look like Python "dictionaries", and JSON calls "arrays" what syntactically looks like Python "lists".
JSON also defines string and numbers.
The [JSON nomenclature](http://www.json.org/) is used below.


### title

_string_, the module title. Supports UTF-8 characters.


### author

_string_, the author(s) of the module. 
Can be multiple people, will be printed exactly as written. 
Supports UTF-8 characters.


### version

_string_, the version number of the module. 
Will be printed exactly as written.

Examples:
```
"version": "1.0",
"version": "0.9.1",
```


### shortdesc

_string_, a short description of what the module is about and what happens with it. 
Keep to < 80 characters. 
Will be printed exactly as written.


### license

_string_, the licensing of the module. 
Use abbreviation if possible. 
Will be printed exactly as written.

Examples:
```
"license": "MIT",
"license": "GNU GPL v3",
```


### difficulty

_number_, a measure of the difficulty of the science covered by the module. 
Should be ranked between 1 and 10 (inclusive). 
Intention is to use this number to sort the modules on the CategoryPage.

_Currently does nothing and is not used._


### exec

_array of strings_, the executable "main module file" that is run from SedEdu.
A relative path is generated with respect to the module root from the given list of strings, where each string in the list is a folder along the path to the file (the last item in list).

Examples:
```
"exec": ["src", "example-module.py"],
"exec": ["source", "main", "executable-file.py"],
```


### longdesc

_string_, a paragraph length description of the module.
Supports UTF-8 characters. 
Intention is to have this field mapped into a scrollable text box of specific height on the ModuleInformationPage. 
No support for linebreaks in the `about.json` file.

_Currently does nothing and is not used._


### projurl

_string_, the home page of the module. 
Will parse out Markdown formatted link, allowing for "link shortening" behind the scenes.
<!-- If Markdown is not detected, input will be printed exactly as written as a link. -->

Examples:
```
"projurl": "[hosted on GitHub](https://github.com/amoodie/example-module_sededu/)",
"projurl": "https://github.com/amoodie/example-module_sededu/",
```


### projreadme

_array of strings_, the README for the module. 
If an array of strings is given, a relative path is generated with respect to the module root, where each string in the array is the folder along the path to the file (last item in array). 
<!-- If a string is given, it is converted to a url link. **ADD STRING TO INPUTS ABOVE!!** -->

Examples:
```
"projreadme": ["README.md"],
```
<!-- "projreadme": "https://github.com/amoodie/example-module_sededu/README.md", --> 


### preview

_array of strings_, the image preview shown on the ModuleInformationPage.
Will be scaled to 250 pixels in height, and then cropped from the left edge of the image to 334 pixels in width (i.e., at a 4:3 aspect ratio, W:H). 
Should work with most image formats (`.png`, `.jpeg`), but does not support movie `.gif`s. 
A relative path is generated with respect to the module root from the given array of strings, where each string in the array is a folder along the path to the file (the last item in array).

Examples:
```
"preview": ["private", "example-module_demo.png"],
```


### docloc

_array of strings_, the folder which contains activities/worksheets that go along with executable "main module file" that is run from SedEdu.
A relative path is generated with respect to the module root from the given array of strings, where each string in the array is a folder along the path to the documents folder (the last item in array).

Examples:
```
"docloc": ["docs"],
```


### doclist

_object_, key-value pairs defining the filename in "docloc" folder as key and the document title to display in SedEdu as the value. Only documents explicitly included in this list will be displayed in SedEdu.

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

