import os

import cv2
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QFont, QKeySequence, QImage, QKeyEvent
from PyQt5.QtWidgets import QWidget, QMainWindow, QToolTip, QDockWidget, QAction, QGraphicsView, QMenuBar, QLabel, \
    QProgressBar, QStatusBar, QPushButton, QMessageBox, QDesktopWidget, QHBoxLayout, QVBoxLayout, QToolBar

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QGraphicsVideoItem, QVideoWidget

from pensieve.divinator import TheModel, WindowConfig

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

class ProductDetails(QWidget):
    """Given a reference to a stage in the system pipeline, show relevant details """
    pass


class ProjectView(QWidget):
    """ This is an IDE like project view"""
    pass


class TheVideoWidget(QWidget):
    """ My video player containing a QVideoWidget, along with appropriate sliders, etc.. """

    def __init__(self, player:QMediaPlayer, parent=None):
        super(TheVideoWidget, self).__init__(parent)
        self.player = player
        self.videoWidget = QVideoWidget(self)
        self.player.setVideoOutput(self.videoWidget)

        self.playButton = QPushButton(parent=self)
        self.playButton.setIcon(QIcon(IconPath.play_video))
        self.playButton.clicked.connect(self.player.play)
        self.playButton.clicked.connect(self.changePlayButton)
        videoCtrlLayout = QHBoxLayout()
        videoCtrlLayout.addWidget(self.playButton)

        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)
        layout.addLayout(videoCtrlLayout)
        layout.addWidget(QLabel("Eat My AssHole!"))
        self.setLayout(layout)

    def changePlayButton(self):
        self.playButton.setText("foo bar baz")


class PreviewList(QWidget):
    """ A set of players showing the results at each stage of a pipeline """
    pass


class TheWindow(QMainWindow):
    def __init__(self, model: TheModel, config: WindowConfig, *args, **kwargs):
        """When implementing a widget, it is important to realize that events can be delivered very early in its
        lifetime so, in its constructor, be sure to initialize member variables early on, before there's any chance
        that it might receive an event."""
        super(TheWindow, self).__init__(*args, **kwargs)
        self.model = model
        self.config = config
        self.init_gui()  # set up the window, its layout based on the config, and the supporting widgets
        self.wire_model()  # you must wire up the model, as observable, to the window, as controller
        self.build_state_machine()  # perhaps you should investigate Qt state machines
        self.fire_init_model_state()  # after wiring the model, fire events based on the initial state

        # show yourself villain
        self.show()

    def keyPressEvent(self, e:QKeyEvent, *args, **kwargs):
        if e.key() == Qt.Key_Escape:
            self.close()

    ###################################################################################################################
    ### Initialization Support Functions
    ###################################################################################################################
    def wire_model(self):
        """ wire up the model's observers to the appropriate actions """
        self.model.observe(self.observeSource, names=['source'])

    def build_state_machine(self):
        """ look into Qt State Machine code """
        pass

    def fire_init_model_state(self):
        """examines the model, after initialization, and fires the appropriate actions based on the state of things"""
        if self.model.source:
            self.openSource()

    def init_gui(self):
        self.setWindowTitle(self.config.name)

        if self.config.fullscreen:
            self.showFullScreen()

        else:
            self.setGeometry(self.config.offsetx, self.config.offsety, self.config.width, self.config.height)
            if self.config.centered:
                self.center()

        appIcon = QIcon(IconPath.icon_app)  # fixme: include an icon
        self.setWindowIcon(appIcon)

        # set up tooltip parameters
        QToolTip.setFont(QFont("Decorative", 10, QFont.Bold))
        self.setToolTip("Foo Bar Baz")

        self.init_widgets()
        self.layout()

    def init_widgets(self):
        # status bar
        self.createStatusBar()

        # Build Actions First, then other components which may use these actions, then add actions to menus
        self.createActions()

        # Create central widget and setCentralWidget
        self.createToolbar()

        # menu bar
        self.createMenuBar()
        self.createMenus()  # wire the actions into the menus

        # dock widgets
        self.previews = PreviewList(parent=self)
        self.south_dock = QDockWidget("Preview List", parent=self)
        self.south_dock.setWidget(self.previews)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.south_dock)

        self.product_details = ProductDetails(parent=self)
        self.east_dock= QDockWidget("Details", parent=self)
        self.east_dock.setWidget(self.product_details)
        self.addDockWidget(Qt.RightDockWidgetArea, self.east_dock)

        self.project_view = ProjectView(parent=self)
        self.west_dock = QDockWidget("Project", parent=self)
        self.west_dock.setWidget(self.project_view)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.west_dock)

        # central widget
        self.player = QMediaPlayer(self)
        self.workArea = TheVideoWidget(self.player, parent=self)
        self.setCentralWidget(self.workArea);

    def createActions(self):
        """ Create actions for menus.  Make them children of the main windows """
        self.chooseSourceAction = QAction(QIcon(IconPath.choose_input), '&Open', self, shortcut=QKeySequence.Open,
                                          statusTip="Choose an Input", triggered=self.chooseSource)
        self.saveOutputAction = QAction(QIcon(IconPath.save_output_media), '&Save', self, shortcut=QKeySequence.Save,
                                        statusTip="Save Output Media", triggered=self.saveOutput)
        self.exitApplicationAction = QAction(QIcon(IconPath.exit_app), 'E&xit', self, shortcut="Ctrl+Q",
                                             statusTip="Exit the Application",
                                             triggered=self.exit)
        self.aboutAction = QAction(QIcon(IconPath.about), 'A&bout', self,
                                   statusTip="Displays info about text editor",
                                   triggered=self.showAbout)
        self.aboutQtAction = QAction(QIcon(IconPath.about_qt), 'About&Qt', self,
                                     statusTip="Displays info about Qt",
                                     triggered=self.showAboutQt)

    def createToolbar(self):
        # create toolbar
        self.theMainToolbar = self.addToolBar('Main')
        self.theMainToolbar.addAction(self.chooseSourceAction)
        self.theMainToolbar.addSeparator()
        self.theMainToolbar.addAction(self.exitApplicationAction)

    # Actual­ menu bar item creation
    def createMenus(self):
        """ Function to create actual menu bar
        """
        # file menu
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.chooseSourceAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitApplicationAction)

        # help menu
        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.aboutAction)
        self.helpMenu.addAction(self.aboutQtAction)

    def createMenuBar(self):
        self.theMenuBar = QMenuBar()
        self.setMenuBar(self.theMenuBar)

    def createStatusBar(self):
        """Create TheWindow's status bar and include a progress bar along with a status label """
        self.statusLabel = QLabel()
        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.addWidget(self.statusLabel, 1)
        self.statusLabel.setText("Loading")
        self.statusBar.addWidget(self.progressBar, 2)
        self.progressBar.setValue(100)

    def setAboutButton(self):
        self.aboutButton = QPushButton("About", self)
        self.aboutButton.move(100, 100)
        self.aboutButton.clicked.connect(self.showAbout)

    def setAboutQtButton(self):
        self.aboutQtButton = QPushButton("About Qt", self)
        self.aboutQtButton.move(200, 200)
        self.aboutQtButton.clicked.connect(self.showAboutQt)

    ####################################################################################################################
    ### observer support functions
    ####################################################################################################################
    def observeSource(self, change):
        """called as an observer to change the source """
        pass

    ####################################################################################################################
    ### action support functions
    ####################################################################################################################
    def openSource(self):
        """ handle the actual source, open it, and pass the imagery to the appropriate players """
        # self.model.cap = cv2.VideoCapture(self.model.source)
        self.player.setMedia(QMediaContent(QUrl(self.model.source)))
        self.player.play()
        print("Played Your Mother Fucking Momma")

    def chooseSource(self):
        """ Offer the user an option to open a file, url, or camera source """
        return

    def saveOutput(self):
        """ save the output, if output details are not set, then offer a settings dialog to determine how to save """
        return

    def exit(self):
        """ leave the application """
        self.close()

    def showAboutQt(self):
        """ show us the About Qt dialog """
        QMessageBox.aboutQt(self.aboutQtButton)

    def showAbout(self):
        """ show us the About this application window, include licensing, etc... """
        QMessageBox.about(self.aboutButton, "About The Window", "A tool for analyzing imagery")

    ####################################################################################################################
    ### UI utilities
    ####################################################################################################################
    def center(self):
        """ utility function used to center the screen. """
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())