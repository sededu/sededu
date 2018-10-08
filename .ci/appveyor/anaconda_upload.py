import os
import sys
import subprocess
import traceback
import glob

print('Using python: {prefix}'.format(prefix=sys.prefix))

repo_tag = os.environ.get('APPVEYOR_REPO_TAG', '')
tag_name = os.environ.get('APPVEYOR_REPO_TAG_NAME', '')
token = os.environ.get('CONDA_TOKEN', 'NOT_A_TOKEN')
repo_branch = os.environ.get('APPVEYOR_REPO_BRANCH', '')
pull_request_num = os.environ.get('APPVEYOR_PULL_REQUEST_NUMBER', '')

print("ENVIRONMENTAL VARIABLES:")
print("\t$APPVEYOR_REPO_TAG = ", repo_tag)
print("\t$APPVEYOR_REPO_TAG_NAME = ", tag_name)
print("\t$APPVEYOR_REPO_BRANCH = ", repo_branch)
print("\t$APPVEYOR_PULL_REQUEST_NUMBER = ", pull_request_num)


if repo_tag == 'true' and tag_name.startswith('v'):
    print('Uploading to "main" channel......')
    _upload = True
    channel = 'main'
elif repo_branch == 'develop' and not pull_request_num:
    print('Uploading to "dev" channel......')
    _upload = True
    channel = 'dev'
elif pull_request_num:
    print('Build is for a PR, not deploying.....')
    _upload = False
else:
    _upload = False

if _upload:
    # try to locate the built file, 
    # if you can't find it, assume build failed
  
    expected_path = os.path.join('.ci', 'conda-build', '**',
                                 'sededu*bz2')
    binary_path = glob.glob(expected_path)
    binary_path = binary_path[0]
    if os.path.isfile(binary_path):
        print('File to upload located at:\n\t', binary_path)
    else:
        raise RuntimeError('{name}: not a file'.format(name=binary_path))

    cmd = ' '.join(['anaconda', '-t', token, 'upload', '--force',
                    '--user', 'sededu', '--channel', channel,
                    binary_path])

    try:
        subprocess.check_call(cmd, shell=True)
    except subprocess.CalledProcessError:
        traceback.print_exc()
else:
    print('No indicators made to upload:')
    print('Not uploading.......')