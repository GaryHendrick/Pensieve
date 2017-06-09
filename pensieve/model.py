
import numbers
import os
import urllib.parse

import numpy as np
from traitlets import Bool, Unicode, List, Integer, validate, TraitError, Instance
from traitlets.config.configurable import Configurable

from pensieve import Divinator


class release():
    pass

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

    sourcemat = Instance(klass=np.ndarray)
    piped_outputs = List(Instance)

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