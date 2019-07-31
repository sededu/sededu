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

Please note that we have a code of conduct ([CODEOFCONDUCT.md](https://github.com/sededu/sededu/blob/release/CODE_OF_CONDUCT.md)), please follow it in all your interactions with the project.

__If you have any questions please don't hesitate to ask!!__
[Open an issue on SedEdu](https://github.com/sededu/sededu/issues) with your question and we'll get right to it!
We are a community seeking collaboration from anyone and everyone.
In particular, if you want to help but the "technology barrier" is scaring you, please just ask the developers.
Our goal is to make contributing easy and rewarding.


### Writing a standalone module

Contributing a module and keeping it up to date in the SedEdu has been made to be painless, thanks to `git submodule` support. 
However, for the sake of brevity in this document, a complete description of the process of getting a module into SedEdu is described in [contributing a module](https://github.com/sededu/sededu/blob/release/docs/contributing_module.md).

This type of contribution usually requires the author to have a working knowledge of Python and `git`. 
If help is needed with the SedEdu `git` workflow, open an issue in SedEdu and we can work out a way to get the module into SedEdu.


### Writing an activity for existing modules

We really need help writing the activities for SedEdu. 
If you would like to help, please just go ahead and write up an activity (using your favorite word processor).
Once you have completed it, try to get in contact with the module author and have them incorporate it into the module on GitHub so it can get pulled into SedEdu on the next update.
For a significant addition of activities, we would also consider an earlier version release to SedEdu.
Alternatively, you can pull request your activity into the module repository.


### Features and bug-fixes for existing modules

Modules maintain their own project structure and workflows, please visit the project page of the module you wish to contribute to.
A good rule-of-thumb though would be to open an issue in the repository to discuss your change with other developers. 
Then assuming you agree on a change, make the change and pull request against the modules main repository.


### Features and bug-fixes for SedEdu

We welcome any contributions to features and bug-fixes to SedEdu!
Please first [open an issue](https://github.com/sededu/sededu/issues) to discuss your idea or concern with the developers. 
This helps to ensure everyone is working together towards the same goals. 

Development should occur off of the latest `develop` branch and you should [pull request](https://github.com/sededu/sededu/blob/release/docs/pull_request_checklist.md) against this repository with your code contributions. 
See [Development Workflow](#sededu-development-workflow) below.

#### Hot-fixes

Hot-fixes fix critical issues in the production version of SedEdu (i.e., the current release).
If you detect a critical issue, please [open an issue](https://github.com/sededu/sededu/issues) immediately to alert the developers.
If you want to work on the issue yourself, you should develop your bug-fix off of the current release version, and then pull request against `release` with your patch.
Hot-fixes will be merged and released ASAP.


### Writing documentation for SedEdu

There are currently "barebones" versions of the following documents that need to worked out further.
These documents help everyone from end-users to contributors navigate through SedEdu.

* using sededu
* example module: `worksheet.md` 
* pull request checklist
* writing activities help sheet

If you want to help, you can write the documentation and pull request.
Alternatively, you can write the documentation and open an issue to share it with developers as raw text; we'll take care of the rest!



## SedEdu development workflow

SedEdu maintains three major branches in the repository: `release` and `develop`.

* `release` is the "public" repository that updates to PyPi are made from for release
* `develop` is the "internal" repository that any development should occur off, including bug-fixes
* `hotfix` is only for necessary bug fixes in the current release version

You can get the latest version of SedEdu (ready for development) from GitHub:
```
git clone https://github.com/sededu/sededu.git
```

You should do _almost_ all development work for SedEdu off the latest `develop` branch of the repository:

```
git checkout -b <name-of-working-branch> develop
```

Only if you are working on a fix for a significant bug in the release version, should you branch from the `release` branch.

If you must get the latest versions of submodules in your SedEdu branch, you can execute the following command. 
However, you should do this only in a separate branch, so that you do not muddy your topic branch with submodule updates (leave this to the SedEdu maintainers).
To get the latest versions of submodules:

```
git submodule foreach git pull
```



## Pull Request Process

1. Merge (or rebase) the latest version of the `develop` branch into your branch.
1. Add yourself to the authorship as appropriate in accordance with the SedEdu authorship policy (see [authorship](#authorship) below).
1. Increase the version numbers in the `README.md` and `setup.py` to the new version that this Pull Request would represent according to the SedEdu versioning scheme (see [versioning](#versioning) below).
1. Push your work to a new branch on your GitHub fork.
1. Check the [pull request checklist](https://github.com/sededu/sededu/blob/release/docs/pull_request_checklist.md) one more time
1. Open a new pull requests on GitHub against the `develop` branch of the main SedEdu repository.
1. You may merge the pull request into `develop` once you have the sign-off of one other developer, or if you do not have permission to do that, you may request the reviewer to merge it for you.

__Note:__ hot-fixes should pull request against the `release` version.



## Versioning

SedEdu uses a `major.minor.maint` semantic versioning scheme [semver.org](https://semver.org/), which is intended to work as follows:

* `major`: should be incremented for significant changes to the SedEdu codebase that affect the interaction of components and generally break backwards compatibility of components. Increment a major version "when you make incompatible API changes.
* `minor`: should be incremented for changes to the SedEdu codebase that do not disrupt the interaction of components (e.g., feature additions). Incorporating an _entirely new_ module into SedEdu should increment a minor version. Increment a minor version "when you add functionality in a backwards-compatible manner.
* `maint`: a.k.a., patch, should be for bug-fixes and _updating submodules_. This level will include hot-fixes to release versions. Increment a maintenance version "when you make backwards-compatible bug fixes.

And importantly, "once a versioned package has been released, the contents of that version _must not_ be modified. Any modifications _must_ be released as a new version" ([semver.org](https://semver.org/)).
Please take care to increment version number correctly when [opening a pull request](https://github.com/sededu/sededu/blob/release/docs/pull_request_checklist.md).

Finally, this semantic versioning scheme is the recommended scheme for your submodule.
Please ensure you are properly incrementing the version number in your `about.json` file when updating.
This will be checked before merging an updated module into the latest SedEdu release.



## Authorship
If you contribute to SedEdu, please add yourself to the Authors list on the main SedEdu project `README.md`, and include this change with with whatever other changes you make in your [pull request](https://github.com/sededu/sededu/blob/release/docs/pull_request_checklist.md). 
Optionally, add a terse note next to your name describing your contribution (e.g., 1 module, documentation, bug fix).
