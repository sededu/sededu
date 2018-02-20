# SedEdu -- sediment-related educational activity suite
# Copyright (C) <year>  <name of author>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ###



import os

## setup script
# setup()

## check dependencies
# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "techSurfers.settings")
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError:
#         # The above import may fail for some other reason. Ensure that the
#         # issue is really that Django is missing to avoid masking other
#         # exceptions on Python 2.
#         try:
#             import django
#         except ImportError:
#             raise ImportError(
#                 "Couldn't import Django. Are you sure it's installed and "
#                 "available on your PYTHONPATH environment variable? Did you "
#                 "forget to activate a virtual environment?"
#             )
#         raise
#     execute_from_command_line(sys.argv)


## import additional packages



## initialize the GUI
thisDir = os.path.dirname(__file__)
thisPath = os.path.join(thisDir,'')
execFile = os.path.join(thisPath, "sededu", "sededuGUI.py")
exec(open(execFile).read())

# from sededu import sededuGUI
# sededuGUI()