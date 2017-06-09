# encoding: utf-8
"""
The application logic is embedded here
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
import logging
import os
import sys
import traceback
from copy import deepcopy

from traitlets import Unicode, Bool, Dict, List
from traitlets.config import Application

from pensieve.model import WindowConfig, TheModel

"""
Goal: Compose a UI which permits the analysis of a video stream.
Requirements:
+ Take Command Line Arguments which define all requisite inputs
+ Package icon resources to make universal stuff available. This will create a QResource accessible binary
+ In the absence of these args, open in a state which permits the user to build the appropriate inputs graphically
+ host a traitlets based model, which will interact with appropriate controlers for the various means of invocation
+ investigate the Qt State Machine Framework, which can act as a controller for the GUI
+ Play a Video
+ While playing the video, execute a set of transformations defined by the script
+ Change the playback speed, or move a single frame at a time
+ Render the end result of the transformations in a results window.
+ Use Drawing tools to select features in the image for analysis.
References:
    * http://docs.opencv.org/3.1.0/d1/db7/tutorial_py_histogram_begins.html
    * http://docs.opencv.org/3.1.0/db/d5b/tutorial_py_mouse_handling.html
    * http://docs.opencv.org/3.1.0/d7/dfc/group__highgui.html most features are either trackbar, button or key driven.
    * http://doc.qt.io/qt-4.8/statemachine-api.html

Note:
    I believe that I can use QAbstractVideoSurface, setting the video to started, and then setting the frame to present
    will allow me to play a video in Qt

"""
class Divinator(Application):
    name = Unicode('divinator')
    description = Unicode('A tool for developing algorithms to transform and analyze imagery')
    version = Unicode('0.1')  # todo: see ipython's release.py for a more robust handling of the version question

    is_running = Bool(False, help="Is the app running?").tag(config=True)
    is_verbose = Bool(False, False, help="verbose output").tag(config=True)
    is_headless = Bool(False, False, help="execute the application headlessly").tag(config=True)
    is_testing = Bool(False, True, read_only=True, help='test the action, but do not execute').tag(config=True)
    config_file = Unicode(os.path.join(os.environ['HOMEPATH'], '.divinator', 'pensieve_config.json'),
                          help="a json formatted config file").tag(config=True)
    raise_config_file_errors = True
    aliases = Dict(dict(input="TheModel.source", destination="TheModel.destination", config="Divinator.config_file"))

    flags = Dict(dict(verbose=({'Divinator': {'is_verbose': True}}, "verbose output"),
                      v=({'Divinator': {'is_verbose': True}}, "verbose output"),
                      headless=({'Divinitor': {'is_headless': False}}, "execute the application headlessly"),
                      running=({'Divinitor': {'is_running': False}}, "determine if the application is already running"),
                      test=({'Divinitor': {'is_testing': False}}, 'test the action, but do not execute'),
                      debug=({'Application': {'log_level': logging.DEBUG}},
                             'set log level to logging.DEBUG (maximize logging output)'),
                      quit=({'Application': {'log_level': logging.CRITICAL}},
                            'set log level to logging.CRITICAL (minimize logging output)')))

    classes = List([WindowConfig, TheModel])

    def initialize(self, argv=None):
        self.parse_command_line(argv)
        self.init_crash_handler()

        # save a copy of CLI config to re-load after config files
        # so that it has highest priority
        cl_config = deepcopy(self.config)

        if self.config_file and os.path.exists(self.config_file):
            # The configurator for a divinitor, in JSON format
            # http: // traitlets.readthedocs.io / en / stable / config.html
            self.load_config_file(
                os.path.basename(self.config_file), path=os.path.dirname(self.config_file))
        self.update_config(cl_config)

        self.init_the_model()
        # before interacting further with the model, build up the appopriate interfaces
        if self.is_headless:
            print(F'running in headless mode')
        else:
            self.init_the_window()

    def start(self):
        # This is where we need to create the asyncio application and have it start up
        if self.is_headless:
            pass
        else:
            if self.is_verbose:
                print("app.config")
                print("-" * 60)
                print(self.config)
                print(self.window_config)
                print(self.model)

            try:
                # start up the opencv business
                # todo: determine the necessities for opengl support. config,
                # If any settings are passed in to the application, they must be pushed into the applications
                # the key here is to make this invocation/gui interaction seamless by actually pushing the change into
                # the system model, rather than directly into the gui

                # this is where I leave the application and move on with my life.
                sys.exit()
            except NameError:
                print("Name Error:", sys.exc_info()[1])
            except SystemExit:
                print("Closing Window ...")
            except Exception:
                print(sys.exc_info()[1])
                print("-" * 60)
                traceback.print_exc(file=sys.stdout)

    def init_the_model(self):
        self.model = TheModel(parent=self)

    def init_the_window(self):
        self.window_config = WindowConfig(parent=self)

    def init_crash_handler(self):  # todo: implement a crash handler
        pass

    @classmethod
    def launch_instance(cls, argv=None, **kwargs):
        """Launch a global instance of this Application

        If a global instance already exists, this reinitializes and starts it
        """
        app = cls.instance(**kwargs)
        app.initialize(argv)
        app.start()


launch_new_instance = Divinator.launch_instance


if __name__ == '__main__':
    launch_new_instance()