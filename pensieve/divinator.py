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
import logging
import numbers
import os
import sys
import traceback
import urllib.parse
from copy import deepcopy

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QStyleFactory
from traitlets import Bool, Unicode, Dict, List, Integer, validate, TraitError
from traitlets.config.configurable import Configurable

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


from traitlets.config.application import Application


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
    aliases = Dict(dict(
        input="TheModel.source", destination="TheModel.destination", config="Divinator.config_file"))

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
                QCoreApplication.processEvents()

                self.gui_app.exec_()

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
        from pensieve.gui import TheWindow
        self.window_config = WindowConfig(parent=self)
        self.gui_app = QApplication(sys.argv)
        # style it ['Windows', 'WindowsXP', 'WindowsVista', 'Motif', 'CDE', 'Plastique', 'Cleanlooks']
        if self.window_config.style in QStyleFactory.keys():
            print(f"applying style {self.window_config.style}")
            self.gui_app.setStyle(QStyleFactory.create(self.window_config.style))
        self.win = TheWindow(model=self.model, config=self.window_config)

    def init_crash_handler(self):  # todo: implement a crash handler
        pass


# main function
def main():
    # Create an Application which will be a shared between cli and gui invocations of the system
    app = Divinator()
    app.initialize()
    app.start()

# Module Invocation
if __name__ == '__main__':
    main()
