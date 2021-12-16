from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QStyleFactory, QMessageBox, QLabel

from Action import Action
from LabeledSlider import LabeledSlider
from InfoWindow import InfoWindow
from HelpWindow import HelpWindow
from GoLBoard import GoLBoard
import Parameters


class GoLWindow(QMainWindow):
    """
    [VIEW]

    Main window of GoLApp. It contains all the view elements, also secondary windows, etc.
    """

    def __init__(self):
        super().__init__()

        """Top level window configuration"""
        self.setWindowTitle("Conway's Game of Life")
        self.setWindowIcon(QtGui.QIcon('img/boat.png'))
        self.setFixedSize(Parameters.BOARD_PX_DIM + 10, Parameters.BOARD_PX_DIM + 130)
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
        self.fps_slider = LabeledSlider("FPS", 1, 15, 1, 2)
        self.size_slider = LabeledSlider("Board size", Parameters.BOARD_MIN_SIZE, Parameters.BOARD_MAX_SIZE,
                                         Parameters.BOARD_STEP_SIZE, Parameters.BOARD_INITIAL_SIZE)

        """Status bar"""
        self._status_bar = self.statusBar()
        self._running_msg = QLabel("Running...")

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
        self._toolbar.addWidget(self.size_slider)
        self._toolbar.addSeparator()
        self._toolbar.addAction(self._run_action)
        self._toolbar.addWidget(self.fps_slider)
        self._toolbar.addAction(self._pause_action)
        self._toolbar.addAction(self._next_action)

        """Secondary windows & dialog"""
        self.info_window = InfoWindow(self, self.style.standardIcon(self.style.SP_MessageBoxInformation))
        self.help_window = HelpWindow(self, self.style.standardIcon(self.style.SP_DialogHelpButton))
        self.clear_confirm = QMessageBox(QMessageBox.Question, "Are you sure?",
                                         "The board will be cleared and it will be impossible to undo the operation",
                                         QMessageBox.Cancel | QMessageBox.Ok, self)

        """Board"""
        self.board = GoLBoard(self, Parameters.BOARD_PX_DIM)
        self.setCentralWidget(self.board)

        """Initial status"""
        self.set_empty()

    """Action connection"""

    def connect_save(self, slot):
        """
        It allow to connect to save action
        :param slot: function to invoke
        :return: None
        """
        self._save_action.triggered.connect(slot)

    def connect_open(self, slot):
        """
        It allow to connect to open action
        :param slot: function to invoke
        :return: None
        """
        self._open_action.triggered.connect(slot)

    def connect_exit(self, slot):
        """
        It allow to connect to exit action
        :param slot: function to invoke
        :return: None
        """
        self._exit_action.triggered.connect(slot)

    def connect_info(self, slot):
        """
        It allow to connect to info action
        :param slot: function to invoke
        :return: None
        """
        self._info_action.triggered.connect(slot)

    def connect_help(self, slot):
        """
        It allow to connect to help action
        :param slot: function to invoke
        :return: None
        """
        self._help_action.triggered.connect(slot)

    def connect_clear(self, slot):
        """
        It allow to connect to clear action
        :param slot: function to invoke
        :return: None
        """
        self._clear_action.triggered.connect(slot)

    def connect_size(self, slot):
        """
        It allow to connect to size change action
        :param slot: function to invoke
        :return: None
        """
        self.size_slider.connect(slot)

    def connect_run(self, slot):
        """
        It allow to connect to run action
        :param slot: function to invoke
        :return: None
        """
        self._run_action.triggered.connect(slot)

    def connect_fps(self, slot):
        """
        It allow to connect to FPS change action
        :param slot: function to invoke
        :return: None
        """
        self.fps_slider.connect(slot)

    def connect_pause(self, slot):
        """
        It allow to connect to pause action
        :param slot: function to invoke
        :return: None
        """
        self._pause_action.triggered.connect(slot)

    def connect_next(self, slot):
        """
        It allow to connect to next action
        :param slot: function to invoke
        :return: None
        """
        self._next_action.triggered.connect(slot)

    """Status handling"""

    def running_on(self):
        """
        It enables/disables the right actions for simulation running status
        :return: None
        """
        self._status_bar.addPermanentWidget(self._running_msg)

        self._pause_action.setEnabled(True)

        self._save_action.setDisabled(True)
        self._open_action.setDisabled(True)
        self._clear_action.setDisabled(True)
        self.size_slider.setDisabled(True)
        self._run_action.setDisabled(True)
        self._next_action.setDisabled(True)

    def running_off(self):
        """
        It enables/disables the right actions for simulation not running status
        :return: None
        """
        self._status_bar.removeWidget(self._running_msg)
        self._running_msg = QLabel(self._running_msg.text())

        self.size_slider.setDisabled(True)
        self._pause_action.setDisabled(True)

        self._save_action.setEnabled(True)
        self._open_action.setEnabled(True)
        self._clear_action.setEnabled(True)
        self._run_action.setEnabled(True)
        self._next_action.setEnabled(True)

    def set_empty(self):
        """
        It enables/disables the right actions for empty board status
        :return: None
        """
        self.size_slider.setEnabled(True)

        self._clear_action.setDisabled(True)
        self._run_action.setDisabled(True)
        self.fps_slider.setDisabled(True)
        self._pause_action.setDisabled(True)
        self._next_action.setDisabled(True)

    def set_not_empty(self, running):
        """
        It enables/disables the right actions for not empty board status
        :return: None
        """
        self.size_slider.setDisabled(True)

        self.fps_slider.setEnabled(True)

        if running:
            self._next_action.setDisabled(True)
        else:
            self._clear_action.setEnabled(True)
            self._next_action.setEnabled(True)
            self._run_action.setEnabled(True)
