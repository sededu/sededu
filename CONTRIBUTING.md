# Contributing to SedEdu



## Ways to contribute

The SedEdu project needs contributions from the community to be successful.
However, there are __many different ways you can contribute!__
You do not even need to write code to contribute to SedEdu.
Some opportunities for contributions are listed below (in no particular order):

* write (code) a standalone interactive module
* write an activity for an existing module
* write (code) features and bug fixes for existing modules
* write (code) features and bug fixes for SedEdu
* write documentation for SedEdu

Please note that we have a code of conduct ([CODEOFCONDUCT.md](https://github.com/amoodie/sededu/blob/master/CODEOFCONDUCT.md)), please follow it in all your interactions with the project.


### Writing a standalone module
Contributing a module and keeping it up to date in the SedEdu has been made to be painless, thanks to `git submodule` support. 
However, for the sake of brevity in this document, a complete description of the process of getting a module into SedEdu is described in [contributing a module](https://github.com/amoodie/sededu/blob/develop/docs/contributing_module.md).

This type of contribution usually requires the author to have a working knowledge of Python and `git`. 
If help is needed with the SedEdu `git` workflow, open an issue in SedEdu and we can work out a way to get the module into SedEdu.


### Writing an activity for existing modules


### Features and bug-fixes for existing modules


### Features and bug-fixes for SedEdu

#### Hot-fixes


### Writing documentation for SedEdu

There are currently "barebones" versions of the following documents that need to worked out further.
These documents help everyone from end-users to contributors navigate through SedEdu.

* using sededu
* example module `readme`, `worksheet.md` 
* contributing a module
* writing the `about.json` file
* pull request checklist
* writing activities help sheet



## SedEdu `git` workflow

SedEdu maintains three major branches in the repository: `release` and `develop`.

* `release` is the "public" repository that updates to PyPi are made from for release
* `develop` is the "internal" repository that any development should occur off
* `hotfix` is only for necessary bug fixes in the current release version

You can get the latest version of SedEdu (ready for development) from GitHub:
```
git clone https://github.com/amoodie/sededu.git
```

You should do _almost_ all development work for SedEdu off the latest `develop` branch of the repository:

```
git checkout -b <name-of-working-branch> develop
```

Only if you are working on a fix for a significant bug in the release version, should you branch from the `release` branch.



## Pull Request Process

1. Merge (or rebase) the latest version of the `develop` branch into your branch.
1. Add yourself to the authorship as appropriate in accordance with the SedEdu authorship policy (see [authorship](#authorship) below).
1. Increase the version numbers in the `README.md` to the new version that this Pull Request would represent according to the SedEdu versioning scheme (see [versioning](#versioning) below).
1. Push your work to a new branch on your GitHub fork.
1. Open a new pull requests on GitHub against the `develop` branch of the main SedEdu repository.
1. You may merge the pull request into `develop` once you have the sign-off of one other developer, or if you do not have permission to do that, you may request the reviewer to merge it for you.

__Note:__ hot-fixes should pull request against the release version.



## Versioning

SedEdu uses a `major.minor.maint` semantic versioning scheme, which is intended to work as follows:

* `major`: should be incremented for significant changes to the SedEdu codebase that affect the interaction of components and generally break backwards compatibility of components. From [semver.org](https://semver.org/): increment a major version "when you make incompatible API changes."
* `minor`: should be incremented for changes to the SedEdu codebase that do not disrupt the interaction of components (e.g., feature additions). Incorporating an _entirely new_ module into SedEdu should increment a minor version. From [semver.org](https://semver.org/): increment a minor version "when you add functionality in a backwards-compatible manner."
* `maint`: a.k.a., patch, should be for bug-fixes and _updating submodules_. This level will include hot-fixes to release versions. From [semver.org](https://semver.org/): increment a maintenance version "when you make backwards-compatible bug fixes."

And importantly, "once a versioned package has been released, the contents of that version _must not_ be modified. Any modifications _must_ be released as a new version" ([semver.org](https://semver.org/)).
Please take care to increment version number correctly when [opening a pull request](https://github.com/amoodie/sededu/blob/feat_documentation/docs/pull_request_checklist.md).

Finally, this semantic versioning scheme is the recommended scheme for your submodule.
Please ensure you are properly incrementing the version number in your `about.json` file when updating.
This will be checked before merging an updated module into the latest SedEdu release.



## Authorship
If you contribute to SedEdu, please add yourself to the Authors list on the main SedEdu project `README.md`, and include this change with with whatever other changes you make in your [pull request](https://github.com/amoodie/sededu/blob/feat_documentation/docs/pull_request_checklist.md). 
Optionally, add a terse note next to your name describing your contribution (e.g., 1 module, documentation, bug fix).
