from distutils.core import setup

setup(
    name='SedEdu',
    version='0.1.0',
    author='Andrew J. Moodie other contributors',
    author_email='amoodie@rice.edu',
    packages=['sededu', 'sededu.test'],
    url='https://github.com/amoodie/sededu',
    license='LICENSE.txt',
    description='',
    long_description=open('README.md').read(),
	# install_requires=[
		# "scipy",
		# "python3-tk", <-- requires an apt install on ubuntu
		# "matplotlib"
#    ],
)
