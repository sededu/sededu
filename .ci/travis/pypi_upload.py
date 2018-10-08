import os
import sys
import subprocess
import traceback
import glob

print('Using python: {prefix}'.format(prefix=sys.prefix))

tag_name = os.environ.get('TRAVIS_TAG', 'false')
repo_branch = os.environ.get('TRAVIS_BRANCH', '')
is_pull_request = os.environ.get('TRAVIS_PULL_REQUEST', 'false')
pypi_pass = os.environ.get('PYPI_PASS', 'NOT_A_PASS')

if is_pull_request == 'false':
    is_pull_request = False
elif is_pull_request.isdigit():
    is_pull_request = True
else:
    raise RuntimeError('{val} defined for "is_pull_request"'.format(val=is_pull_request))
    sys.exit(1)

if tag_name and tag_name.startswith('v'):
    print('Tag made for release:')
    print('Uploading to Pypi')
    _upload = True
    channel = 'main'
elif repo_branch == 'develop' and not is_pull_request:
    print('Commit made to "develop", and not PR:')
    print('Not uploading to Pypi.')
    _upload = False
elif is_pull_request:
    print('Build is for a PR, not uploading to Pypi.')
    _upload = False
else:
    _upload = False

if _upload:
    try:
        cmd = 'twine upload -u amoodie -p{0} dist/*'.format(pypi_pass)
        response = subprocess.check_output(cmd, shell=True)
        print('Deploy to Pypi succeeded.')
    except subprocess.CalledProcessError:
        print('\n\tDeploy to PyPi failed.\n\n')
        # traceback.print_exc()
        sys.exit(1)
else:
    print('No indicators made to deploy to Pypi:')
    print('Not Deploying.......')
