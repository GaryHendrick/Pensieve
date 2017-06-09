import os

import cv2
from pensieve.model import TheModel, WindowConfig

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


class WindowController(object):
    """ The controller has to handle the gui related callbacks, forwarding those requests back down stream via the
    model, or simply updating the ui appropriately, and also, monitor the model for appropriate changes coming up
    from the application to the gui.
    """
    def __init__(self, window_name:str, model:TheModel) -> None:
        super(WindowController, self).__init__()
        self.wname = window_name

        #todo: button, mouse, etc.... callbacks 

class GuiManager(object):
    """ The manager contains information relevant to each window in the application. It is also responsible
     for registering model callbacks to the controllers that it creates, and managing the relationship of controllers to
     views.

     Use the GuiMangager to configure the gui.
     """
    def __init__(self, model:TheModel, config:WindowConfig) -> None:
        super(GuiManager, self).__init__()

    def init_source_window(self):
        pass

    def add_child_window(self):
        handle = WindowHandle(id())
        return handle

    def launch(self):
        pass

    def add_window(self) -> WindowHandle:
        pass

    def close(self):
        cv2.destroyAllWindows()
