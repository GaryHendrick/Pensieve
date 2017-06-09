# encoding: utf-8
"""
Pensieve: a tool for interacting with and modifying media through openCV and
other python tools
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

#-----------------------------------------------------------------------------
#   Imports
#-----------------------------------------------------------------------------
import sys

#-----------------------------------------------------------------------------
# setup
#-----------------------------------------------------------------------------
if sys.version_info < (3,3): # fixme: check against requirements
    raise ImportError(
        """
        Pensieve uses such and such requirements
        """
    )
#-----------------------------------------------------------------------------
# setup the top level names
#-----------------------------------------------------------------------------
from .core import release
import pensieve.core.application as application
from .core.application import Divinator
from .testing import test
from .utils.sysinfo import sys_info

# Release data
__author__ = f'{release.author}, {release.author_email}'
__license__ = release.license
__version__ = release.version
version_info = release.version_info


def start_pensieve(argv=None, **kwargs):
    """Launch a pensieve instance (as opposed to embedded)

    `start_pensieve()` loads startup files, configuration, etc.

    This is a public API method, and will survive implementation changes.

    Parameters
    ----------

    argv : list or None, optional
        If unspecified or None, pensieve will parse command-line options from sys.argv.
        To prevent any command-line parsing, pass an empty list: `argv=[]`.
    user_ns : dict, optional
        specify this dictionary to initialize the pensieve user namespace with particular values.
    kwargs : various, optional
        Any other kwargs will be passed to the Application constructor,
        such as `config`.
    """
    return application.launch_new_instance(argv=argv, **kwargs)