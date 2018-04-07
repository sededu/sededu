from setuptools import setup

setup(
    name='SedEdu',
    version='0.9.2',
    author='Andrew J. Moodie other contributors',
    author_email='amoodie@rice.edu',
    packages=['sededu'],
    url='https://github.com/amoodie/sededu',
    license='LICENSE.md',
    description='sediment-related educational activity suite',
    long_description=open('README.md').read(),
	# install_requires=[
		# "scipy",
		# "python3-tk", <-- requires an apt install on ubuntu
		# "matplotlib"
#    ],
)
