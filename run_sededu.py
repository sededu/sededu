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


## check dependencies



## import additional packages


## initialize the GUI
thisDir = os.path.dirname(__file__)
thisPath = os.path.join(thisDir,'')
execFile = os.path.join(thisPath, "sededu", "root.py")
exec(open(execFile).read())
