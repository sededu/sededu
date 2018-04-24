# Building distributions

This file contains information for building distributions of SedEdu for release on PyPi.

## Run commands

when ready run:

1. `python3 setup.py build --dry-run`
1. `python3 setup.py build`
1. `python3 setup.py sdist`
1. `python3 setup.py bdist_wheel`
1. see validate naming below
1. `twine upload dist/*`


`twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
`pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple sededu`



## Validate naming

Following from [PEP 425](https://www.python.org/dev/peps/pep-0425/), SedEdu wheels should be released with names following the convention:
```
{distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl
```

* `{distribution}` - should always be `sededu`
* `{version}` - should be the version number being packaged for distribution
* `{build tag}` - probably to be omitted, only include if special hot-fix for release
* `{python tag}` - should always be `py3`, well until Python 4 anyway
* `{abi tag}` - should always be `none`
* `{platform tag}` - should always be `any`

For example, version 1.0.2 was released under:

```
sededu-1.0.2-py3-none-any.whl
```
