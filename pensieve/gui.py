# encoding: utf-8
"""
gui module : controlers and views for use in the pensieve gui
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
import os

import cv2
from traitlets.config import Application, HasTraits, Bool, observe

from pensieve.model import TheModel
# -----------------------------------------------------------------------------
#   Imports
# -----------------------------------------------------------------------------
import os

import cv2
from traitlets.config import Application, HasTraits, Bool, observe

from pensieve.model import TheModel


class IconPath(object):
    """ A simple means of encapsulating the locations of icons """
    # constants
    RES_ROOT = "resource"
    RES_TYPE = os.path.join("svg", "production")
    RES_ACTION = os.path.join(RES_ROOT, "action", RES_TYPE)
    RES_ALERT = os.path.join(RES_ROOT, "alert", RES_TYPE)
    RES_AV = os.path.join(RES_ROOT, "av", RES_TYPE)
    RES_COMMUNICATIONS = os.path.join(RES_ROOT, "communications", RES_TYPE)
    RES_CONTENT = os.path.join(RES_ROOT, "content", RES_TYPE)
    RES_DEVICE = os.path.join(RES_ROOT, "device", RES_TYPE)
    RES_EDITOR = os.path.join(RES_ROOT, "editor", RES_TYPE)
    RES_FILE = os.path.join(RES_ROOT, "file", RES_TYPE)
    RES_HARDWARE = os.path.join(RES_ROOT, "hardware", RES_TYPE)
    RES_ICOFONT = os.path.join(RES_ROOT, "icofont", RES_TYPE)
    RES_IMAGE = os.path.join(RES_ROOT, "image", RES_TYPE)
    RES_MAPS = os.path.join(RES_ROOT, "maps", RES_TYPE)
    RES_NAVIGATION = os.path.join(RES_ROOT, "navigation", RES_TYPE)
    RES_NOTIFICATION = os.path.join(RES_ROOT, "notification", RES_TYPE)
    RES_PLACES = os.path.join(RES_ROOT, "places", RES_TYPE)
    RES_TOGGLE = os.path.join(RES_ROOT, "toggle", RES_TYPE)

    icon_app = os.path.join(RES_PLACES, "ic_ac_unit_24px.svg")
    choose_input = os.path.join(RES_ACTION, "ic_input_48px.svg")
    exit_app = os.path.join(RES_NAVIGATION, "ic_close_48px.svg")
    save_output_media = os.path.join(RES_ACTION, "ic_save_48px.svg")
    fast_forward_video = os.path.join(RES_AV, "ic_fast_forward_48px.svg")
    fast_rewind_video = os.path.join(RES_AV,"ic_fast_rewind_48px.svg")
    forward_05_video = os.path.join(RES_AV, "ic_forward_5_48px.svg")
    forward_10_video = os.path.join(RES_AV, "ic_forward_10_48px.svg")
    forward_30_video = os.path.join(RES_AV, "ic_forward_30_48px.svg")
    loop_video = os.path.join(RES_AV, "ic_loop_48px.svg")
    movie = os.path.join(RES_AV, "ic_movie_48px.svg")
    pause_video = os.path.join(RES_AV, "ic_pause_48px.svg")
    play_video = os.path.join(RES_AV, "ic_play_48px.svg")
    replay_video = os.path.join(RES_AV, "ic_replay_48px.svg")
    replay_05_video = os.path.join(RES_AV, "ic_replay_5_48px.svg")
    replay_10_video = os.path.join(RES_AV, "ic_replay_5_48px.svg")
    replay_30_video = os.path.join(RES_AV, "ic_replay_5_48px.svg")
    slow_motion_video = os.path.join(RES_AV, "ic_slow_motion_video_48px.svg")
    stop_video = os.path.join(RES_AV, "ic_stop_video_48px.svg")
    about = os.path.join(RES_ACTION, "ic_help_24px.svg")
    about_qt = os.path.join(RES_ACTION, "ic_help_outline_24px.svg")

class WindowHandle(object):
    """ an object used to keep track of the windows in the manager """

    def __init__(self, id) -> None:
        super(WindowHandle, self).__init__()
        self.id = id


WHANDLE_ALL = WindowHandle(-1)

class WindowController(object):
    """ The controller has to handle the gui related callbacks, forwarding those requests back down stream via the
    model, or simply updating the ui appropriately, and also, monitor the model for appropriate changes coming up
    from the application to the gui.
    """
    def __init__(self, window_name:str, model:TheModel) -> None:
        super(WindowController, self).__init__()
        self.wname = window_name

        #todo: button, mouse, etc.... callbacks


class ControlPanel(object):
    def __init__(self, context, *args, **kwargs) -> None:
        super().__init__()
        self.context = context
        self._wname = "control_panel"
        self._wname_foo = "foo"

    def show(self):
        cv2.namedWindow(self._wname)
        cv2.createTrackbar(self._wname_foo, self._wname, 1, 1, self.on_foo_change)

    def on_foo_change(self, state, userdata):
        print(f"on_foo_change clicked with {state} and {userdata}")
        self.context.close_window()


class GuiContext(Application):
    """ The manager contains information relevant to each window in the application. It is also responsible
     for registering model callbacks to the controllers that it creates, and managing the relationship of controllers to
     views.

     Use the GuiMangager to configure the gui.
     """
    is_displayed = Bool(False)

    @observe('is_displayed')
    def _observe_is_displayed(self, change: dict):
        self._model.is_displayed = change['new']

    def __init__(self, model: TheModel, *args, **kwargs) -> None:
        super(GuiContext, self).__init__(*args, **kwargs)
        self._model = model if model is not None else HasTraits()
        self.init_model()
        self.build_components()

    def init_model(self):
        """ called during initialization.  The traits of this object will be added to the traits of the __init__
        supplied model """
        self._model.add_traits(**self.traits())

    def init_source_window(self):
        pass

    def add_child_window(self):
        handle = WindowHandle(id())
        return handle

    def start(self):
        # todo: pass opencv's ui into either asyncio or another thread
        cv2.namedWindow(self._wname, cv2.WINDOW_GUI_EXPANDED)
        self._control_panel.show()
        self.is_displayed = True

    def add_window(self) -> WindowHandle:
        pass

    def close(self):
        cv2.destroyAllWindows()

    def build_control_panel(self):
        self._control_panel = ControlPanel(context=self)

    def build_components(self):
        self._wname = "guicontext"
        self.build_control_panel()

    def close_window(self, handle=WHANDLE_ALL):
        if handle == WHANDLE_ALL:
            cv2.destroyAllWindows()
            self.is_displayed = False
        else:
            cv2.destroyWindow(self.opened_windows[handle])
