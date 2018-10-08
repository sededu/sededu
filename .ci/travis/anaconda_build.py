import os
import sys
import subprocess
import traceback
import glob

print('Using python: {prefix}'.format(prefix=sys.prefix))

tag_name = os.environ.get('TRAVIS_TAG', 'false')
token = os.environ.get('CONDA_TOKEN', 'NOT_A_TOKEN')
repo_branch = os.environ.get('TRAVIS_BRANCH', '')
repo_slug = os.environ.get('TRAVIS_REPO_SLUG', '')
is_pull_request = os.environ.get('TRAVIS_PULL_REQUEST', 'false')

if is_pull_request == 'false':
    is_pull_request = False
elif is_pull_request.isdigit():
    is_pull_request = True
else:
    raise RuntimeError('{val} defined for "is_pull_request"'.format(val=is_pull_request))
    sys.exit(1)

print("ENVIRONMENTAL VARIABLES:")
print("\t$TRAVIS_TAG = ", tag_name)
print("\t$TRAVIS_BRANCH = ", repo_branch)
print("\t$TRAVIS_REPO_SLUG = ", repo_slug)
print("\t$TRAVIS_PULL_REQUEST = ", is_pull_request)


if tag_name and tag_name.startswith('v'):
    print('Tag made for release:')
    print('Building for "main" channel......')
    _build = True
    channel = 'main'
    # os.environ['BUILD_STR'] = ''
elif repo_branch == 'develop' and not is_pull_request:
    print('Commit made to "develop", and not PR:')
    print('Building for "dev" channel......')
    _build = True
    channel = 'dev'
elif is_pull_request:
    print('Build is for a PR, not building.....')
    _build = False
else:
    _build = False

if _build:
    try:
        cmd = ' '.join(['conda', 'build', os.path.join('.ci', 'conda-recipe'),
                        '--output-folder', os.path.join('.ci', 'conda-build'),
                        '--no-test'])
        response = subprocess.check_output(cmd, shell=True)
        print('Build succeeded.')
    except subprocess.CalledProcessError:
        print('\n\nBuild failed.\n\n')
        traceback.print_exc()
        sys.exit(1)
else:
    print('No indicators made to build:')
    print('Not building.......')
