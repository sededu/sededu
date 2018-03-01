# Writing the about.json file

This document provides support for writing the modules "documentation" file in the format that SedEdu requires: the `about.json` file.

A sample `about.json` file can be found in the `sample_module` folder [(link to folder)](https://github.com/amoodie/sededu/docs/sample_module)

## what is the about.json file
 describe json briefly

 Required vs optional fields, note that leaving out req fields won't cause failure, but will result in default strings.

 Note that the order of the fields in your `about.json` file does not matter. 


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