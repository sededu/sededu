from setuptools import setup
import re


# borrowed from Agile Scientific bruges tools
verstr = 'unknown'
VERSIONFILE = "sededu/_version.py"
with open(VERSIONFILE, "r") as f:
    verstrline = f.read().strip()
    pattern = re.compile(r"__version__ = ['\"](.*)['\"]")
    mo = pattern.search(verstrline)
if mo:
    verstr = mo.group(1)
    print("Version "+verstr)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


setup(
    name='SedEdu',
    version='1.0.2',
    author='Andrew J. Moodie other contributors',
    author_email='amoodie@rice.edu',
    packages=['sededu'],
    url='https://github.com/amoodie/sededu',
    license='LICENSE.txt',
    description='sediment-related educational activity suite',
    long_description=open('README.md').read(),
    python_requires='>=3',
	install_requires=[
		'scipy',
        'numpy',
		'matplotlib',
        'shapely',
        'pygame'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'Topic :: Education',
        'Topic :: Education :: Computer Aided Instruction (CAI)]'],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/amoodie/sededu/issues',
        'Source': 'https://github.com/amoodie/sededu/',
    },
)
