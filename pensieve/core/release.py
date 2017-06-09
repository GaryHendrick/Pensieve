# encoding: utf-8
"""
Pensieve Release Data
"""
#-----------------------------------------------------------------------------
#  Copyright (c) 2017, Gary Hendrick.
#
#  This file is part of Pensieve.
#
#    Pensieve is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Pensieve is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
#  The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------


# Name of the package for release purposes.  This is the name which labels
# the tarballs and RPMs made by distutils, so it's best to lowercase it.
name = 'pensieve'

# Pensieve version information.  See semanitic versioning guidelines.
# An empty _version_extra corresponds to a full
# release.  'dev' as a _version_extra string means this is a development
# version
_version_major = 0
_version_minor = 1
_version_patch = 0
_version_extra = '.dev'
# _version_extra = 'rc2'
_version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor, _version_patch]

__version__ = '.'.join(map(str, _ver))
if _version_extra:
    __version__ = __version__  + _version_extra

version = __version__  # backwards compatibility name
version_info = (_version_major, _version_minor, _version_patch, _version_extra)

description = "Pensieve: An interactive algorithm development tool"

long_description = \
"""
Pensieve Video Analyzer and OpenCV algorithm development tool
"""

license = 'GPLv3'

authors = {'Gary' : ('Gary Hendrick','gary.hendrick@gmail.com'),
           }

author = 'Gary Hendrick'

author_email = 'gary.hendrick@gmail.org'

url = 'https://github.com/GaryHendrick/Pensieve'

platforms = ['Linux','Mac OSX','Windows']

keywords = ['Interactive','Analysis']

classifiers = [
    'Framework :: Traitlets',
    'Intended Audience :: Engineers',
    'Intended Audience :: Engineering/Science/Research',
    'License :: OSI Approved :: GPLv3',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Analysis'
    ]
