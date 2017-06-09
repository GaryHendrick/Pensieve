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
import os
import platform
import pprint

import sys

from pensieve.core import release


def pkg_info(pkg_path):
    """Return dict describing the context of this package

        Parameters
        ----------
        pkg_path : str
           path containing __init__.py for package

        Returns
        -------
        context : dict
           with named parameters of interest
        """
    return dict(
        ipython_version=release.version,
        ipython_path=pkg_path,
        sys_version=sys.version,
        sys_executable=sys.executable,
        sys_platform=sys.platform,
        platform=platform.platform(),
        os_name=os.name,
    )


def get_sys_info():
    """Return useful information about IPython and the system, as a dict."""
    p = os.path
    path = p.realpath(p.dirname(p.abspath(p.join(__file__, '..'))))
    return pkg_info(path)


def sys_info():
    """Return useful information about IPython and the system, as a string.

    Examples
    --------
    ::

        In [2]: print sys_info()
        {'commit_hash': '144fdae',      # random
         'commit_source': 'repository',
         'ipython_path': '/home/fperez/usr/lib/python2.6/site-packages/IPython',
         'ipython_version': '0.11.dev',
         'os_name': 'posix',
         'platform': 'Linux-2.6.35-22-generic-i686-with-Ubuntu-10.10-maverick',
         'sys_executable': '/usr/bin/python',
         'sys_platform': 'linux2',
         'sys_version': '2.6.6 (r266:84292, Sep 15 2010, 15:52:39) \\n[GCC 4.4.5]'}
    """
    return pprint.pformat(get_sys_info())