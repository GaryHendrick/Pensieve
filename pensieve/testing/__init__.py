# encoding: utf-8
"""Testing support (tools to test Pensieve itself).
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
# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# User-level entry point for testing
def test(**kwargs):
    """Run the entire pensieve test suite.
    """
    pass


# So nose doesn't try to run this as a test itself and we end up with an
# infinite test loop
test.__test__ = False