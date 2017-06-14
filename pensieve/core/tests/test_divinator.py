# encoding: utf-8
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


"""
Testing for the Application Divinator resides here.  As this is the Application itself, there are both unit tests
and end-to-end tests included here.
"""
import time
import unittest
from unittest import TestCase

from traitlets import HasTraits

from pensieve import Divinator


class TestDivinatorEndToEnd(TestCase):
    """ The TestCase for Divinator's end to end tests """

    def test_launch_and_click(self):
        """ an end to end test fullfilled by launching the application in its graphical mode and then watching for
        an update to TheModel via closing a view window perhaps """
        # todo: confirm the details of this test before commiting totally to the implications
        from pensieve.core.application import Divinator
        app = Divinator.instance()
        app.initialize()
        app.start()
        self.assertTrue(app._model.is_displayed)

        # The app is launched and the gui is displayed
        # app._gui_context.close_window()
        time.sleep(10)
        self.assertFalse(app._model.is_displayed,
                         'The Ui is Still Opened, any change that there is no thread handler ?')


class TestDivinatorUnit(TestCase):
    """ Unit tests for the Divinator application """

    def setUp(self):
        self.app = Divinator()
        self.app.initialize()

    def test_initialize(self):
        self.assertIsInstance(self.app._model, HasTraits)
        # todo: add a greater degree of initialization testing, i.e. how about ensuring that the config system is ok

    def test_start(self):
        # I should be testing an event loop here
        self.app.start()
        self.fail("unimplemented")

    @unittest.skip('skipping until we get into worrying about a crash handler')
    def test_init_crash_handler(self):
        self.fail("unimplemented")

    def test_open_video(self):
        self.app.open_input()

    def test_iterate_video(self):
        self.app.scan_input()

    def test_watch_iteration(self):
        self.fail("unimplemented")

    def test_pipleine_builder(self):
        # todo: likely too course grained a test.  Instead of this, consider adding methods such as add/remove layer
        self.fail("unimpmented")

    def test_pipeline_transport(self):
        """ assert that the data moves through the pipeline effectively """
        self.fail("unimplemented")

    def test_pipeline_product(self):
        """ assert the results of a pipeline of transformations """
        self.fail("unimplemented")
