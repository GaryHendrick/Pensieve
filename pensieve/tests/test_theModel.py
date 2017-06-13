# encoding: utf-8
"""
 TheModle tests : tests for the application's model
"""
# -----------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#   Imports
# -----------------------------------------------------------------------------
from unittest import TestCase
from unittest.mock import patch

from traitlets import observe, Instance, TraitError

from pensieve.model import TheModel
# -----------------------------------------------------------------------------
#   Imports
# -----------------------------------------------------------------------------
from unittest import TestCase
from unittest.mock import patch

from traitlets import observe, Instance, TraitError

from pensieve.model import TheModel


class TestTheModel(TestCase):
    """ In truth, limited testing is really required for TheModel, as it is simply
    a HasTraits object.  I am testing it in order to develop my understanding of how
    HasTraits works more than anything else, really"""

    def setUp(self):
        self.model = TheModel()

    def observer(change):
        return

    def test__invalid_destination(self):
        with self.assertRaises(TraitError):
            self.model.destination = ''

    def test__observe_source(self):
        with patch.object(self, 'observer') as mock_observer:
            self.model.observe(self.observer, names=['source'])
            self.model.source = "samples/video.h264"
        mock_observer.assert_called_once_with(
            dict(name='source', new='samples/video.h264', owner=self.model, type='change', old=''))

    def test_chain__observe_destination(self):
        from traitlets import HasTraits, Unicode

        class Foo(HasTraits):
            self._delegate = Instance(HasTraits)
            destination = Unicode()

            @observe('destination')
            def _observe_destination(self, change):
                self._delegate.destination = change['new']

            def __init__(self, delegate: HasTraits):
                super(Foo, self).__init__()
                self._delegate = delegate
                self._delegate.add_traits(**self.traits())

        myfoo = Foo(self.model)
        myfoo.destination = 'samples'
        self.assertEqual(myfoo.destination, self.model.destination)
