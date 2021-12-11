from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QStyleFactory

from Action import Action
from LabeledSlider import LabeledSlider
from InfoWindow import InfoWindow
from HelpWindow import HelpWindow
from GoLBoard import GoLBoard


class GoLWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        """Top level window configuration"""
        self.setWindowTitle("Conway's Game of Life")
        self.setWindowIcon(QtGui.QIcon('img/boat.png'))
        self.setFixedSize(760, 880)
        self.style = QStyleFactory.create("Fusion")
        self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)

        """Actions"""
        self._save_action = Action(self, "&Save", "Save current configuration", ["Ctrl+S"],
                                   self.style.standardIcon(self.style.SP_DialogSaveButton))
        self._open_action = Action(self, "&Open", "Open a configuration", ["Ctrl+O"],
                                   self.style.standardIcon(self.style.SP_DialogOpenButton))
        self._exit_action = Action(self, "&Exit", "Exit the program", ["Ctrl+Q", "Ctrl+F4"])
        self._info_action = Action(self, "&Info", "Read more about the program", ["Ctrl+I"],
                                   self.style.standardIcon(self.style.SP_MessageBoxInformation))
        self._help_action = Action(self, "&Help", "Read user guide", ["Ctrl+H"],
                                   self.style.standardIcon(self.style.SP_DialogHelpButton))

        self._run_action = Action(self, "&Run", "Start the running", ["Ctrl+R"],
                                  self.style.standardIcon(self.style.SP_MediaPlay))
        self._pause_action = Action(self, "&Pause", "Pause the running", ["Ctrl+P"],
                                    self.style.standardIcon(self.style.SP_MediaPause))
        self._next_action = Action(self, "&Next", "Next status of the run", ["Ctrl+N"],
                                   self.style.standardIcon(self.style.SP_MediaSkipForward))
        self._clear_action = Action(self, "&Clear", "Clear the configuration", ["Ctrl+C"],
                                    self.style.standardIcon(self.style.SP_LineEditClearButton))

        """Controls"""
        self._fps_slider = LabeledSlider("FPS", 1, 15, 1, 2)
        self._size_slider = LabeledSlider("Board size", 25, 100, 5, 75)

        """Status bar"""
        self._status_bar = self.statusBar()

        """Menu bar"""
        self._menu_bar = self.menuBar()

        self._file_menu = self._menu_bar.addMenu("&File")
        self._file_menu.addAction(self._save_action)
        self._file_menu.addAction(self._open_action)
        self._file_menu.addSeparator()
        self._file_menu.addAction(self._exit_action)

        self._run_menu = self._menu_bar.addMenu("&Tools")
        self._run_menu.addAction(self._clear_action)
        self._run_menu.addSeparator()
        self._run_menu.addAction(self._run_action)
        self._run_menu.addAction(self._pause_action)
        self._run_menu.addAction(self._next_action)

        self._about_menu = self._menu_bar.addMenu("&About")
        self._about_menu.addAction(self._help_action)
        self._about_menu.addAction(self._info_action)

        """Toolbar"""
        self._toolbar = self.addToolBar("Controls")
        self._toolbar.setMovable(False)
        self._toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self._toolbar.addAction(self._clear_action)
        self._toolbar.addWidget(self._size_slider)
        self._toolbar.addSeparator()
        self._toolbar.addAction(self._run_action)
        self._toolbar.addWidget(self._fps_slider)
        self._toolbar.addAction(self._pause_action)
        self._toolbar.addAction(self._next_action)

        """Secondary windows"""
        self.info_window = InfoWindow(self, self.style.standardIcon(self.style.SP_MessageBoxInformation))
        self.help_window = HelpWindow(self.style.standardIcon(self.style.SP_DialogHelpButton))

        """Board"""
        self._board = GoLBoard(self, 50, 750)
        self.setCentralWidget(self._board)

    def connect_exit(self, slot):
        self._exit_action.triggered.connect(slot)

    def connect_info(self, slot):
        self._info_action.triggered.connect(slot)

    def connect_help(self, slot):
        self._help_action.triggered.connect(slot)
