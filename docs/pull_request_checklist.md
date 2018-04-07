# Pull Request checklist



## Bug-fixes and features in SedEdu

1. 
1. authorship list
1. increment version numbers
1. check branch to pull against (should be develop, unless a hot-fix)



## Adding a submodule to SedEdu

1. determine stability of submodule and [assign a version number](https://github.com/amoodie/sededu/blob/develop/CONTRIBUTING.md#versioning)
1. license file
1. increment version number (minor if new)
1. check branch to pull against (should be develop, unless a hot-fix)



## Contributions to submodules

1. Should be made in the respective repository of the submodule.
1. 
1. Will be incorporated into new SedEdu releases scheduled for every 6 months, January and June. These submodule changes will result in `maint` level version increments to SedEdu, if nothing else has changed in that release cycle. If you wish to update the submodule into SedEdu sooner that the 6 month cycle, open a pull request against the latest `develop` branch.