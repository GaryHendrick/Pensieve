# encoding: utf-8
"""
Models : traitlets Configurables and HasTraits used as models for object notification
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

# -----------------------------------------------------------------------------
#   Imports
# -----------------------------------------------------------------------------
import numbers
import os
# -----------------------------------------------------------------------------
#   Imports
# -----------------------------------------------------------------------------
import urllib.parse
import urllib.parse

import numpy as np
from traitlets import Bool, Unicode, List, Integer, validate, TraitError, Instance
from traitlets.config.configurable import Configurable

from pensieve.cvtools import CaptureProperties


class TheModel(Configurable):
    """ A model derived from the Traitlets API and built to support an observable pattern.
     The Configurable superclass permits theModel to be used
    """
    source = Unicode("", True, False, help='input filename to be initially loaded').tag(config=True)

    @validate('source')
    def _valid_source(self, proposal):
        if isinstance(proposal['value'], numbers.Integral):
            return str(proposal['value'])
        elif not urllib.parse.urlparse(proposal['value']).scheme == "":
            return proposal['value']
        elif os.path.exists(proposal['value']) and not os.path.isdir(proposal['value']):
            return proposal['value']
        else:
            raise TraitError('Illegal Source specfied: {}'.format(proposal['value']))

    destination = Unicode(os.getcwd(), True, False, help='the output directory to be used to store data snapshots').tag(
        config=True)

    @validate('destination')
    def _valid_destination(selfself, proposal):
        if os.path.exists(proposal['value']) and os.path.isdir(proposal['value']) and os.access(proposal['value'], os.W_OK):
            return proposal['value']
        else:
            raise TraitError('Illegal Destination specfied: {}'.format(proposal['value']))

    cap_props = Instance(klass=CaptureProperties)
    sourcemat = Instance(klass=np.ndarray)

    piped_outputs = List(Instance(klass=np.ndarray))

    def __repr__(self) -> str:
        return super().__repr__()


class WindowConfig(Configurable):
    fullscreen = Bool(False, False, help='set the application to a fullscreen mode').tag(config=True)
    centered = Bool(True, False, help='open the window centered').tag(config=True)
    offsetx = Integer(200).tag(config=True)
    offsety = Integer(200).tag(config=True)
    width = Integer(600).tag(config=True)
    height = Integer(400).tag(config=True)
    style = Unicode('windows').tag(config=True)

    name = Unicode(u'The Window')

    def __repr__(self) -> str:
        return super().__repr__()