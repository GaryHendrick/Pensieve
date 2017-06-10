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
from unittest import TestCase


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
    def test_initialize(self):
        self.fail("unimplemented")

    def test_start(self):
        self.fail("unimplemented")

    def test_init_the_model(self):
        self.fail("unimplemented")

    def test_init_the_config(self):
        self.fail("unimplemented")

    def test_init_crash_handler(self):
        self.fail("unimplemented")

    def test_launch_instance(self):
        self.fail("unimplemented")
