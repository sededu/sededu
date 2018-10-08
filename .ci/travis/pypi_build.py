import os
import sys
import subprocess
import traceback
import glob

print('Using python: {prefix}'.format(prefix=sys.prefix))

tag_name = os.environ.get('TRAVIS_TAG', 'false')
repo_branch = os.environ.get('TRAVIS_BRANCH', '')
is_pull_request = os.environ.get('TRAVIS_PULL_REQUEST', 'false')

if is_pull_request == 'false':
    is_pull_request = False
elif is_pull_request == 'true':
    is_pull_request = True
else:
    raise RuntimeError('{val} defined for "is_pull_request"'.format(name=val))

if tag_name and tag_name.startswith('v') and repo_branch == 'release':
    print('Tag made for release:')
    print('Building for Pypi release')
    _build = True
elif repo_branch == 'develop' and not is_pull_request:
    print('Commit made to develop, and not PR:')
    print('Not building......')
    _build = False
elif is_pull_request:
    print('Build is for a PR, not building.....')
    _build = False
else:
    _build = False

if _build:
    try:
        cmd = 'python setup.py sdist bdist_wheel'
        response = subprocess.check_output(cmd, shell=True)
        print('Build succeeded.')
    except subprocess.CalledProcessError:
        print('\n\nBuild failed.\n\n')
        traceback.print_exc()
else:
    print('No indicators made to build:')
    print('Not building.......')
