from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QStyleFactory

from Action import Action
from FPSSlider import FPSSlider
from InfoWindow import InfoWindow
from HelpWindow import HelpWindow


class GoLWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        """Top level window configuration"""
        self.setWindowTitle("Conway's Game of Life")
        self.setWindowIcon(QtGui.QIcon('img/boat.png'))
        self.setFixedSize(500, 500)
        self.style = QStyleFactory.create("Fusion")
        self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)

        """Actions"""
        self._save_action = Action(self, "&Save", "Save current configuration", ["Ctrl+S"], self.style.standardIcon(self.style.SP_DialogSaveButton))
        self._open_action = Action(self, "&Open", "Open a configuration", ["Ctrl+O"], self.style.standardIcon(self.style.SP_DialogOpenButton))
        self._exit_action = Action(self, "&Exit", "Exit the program", ["Ctrl+Q", "Ctrl+F4"])
        self._info_action = Action(self, "&Info", "Read more about the program", ["Ctrl+I"], self.style.standardIcon(self.style.SP_MessageBoxInformation))
        self._help_action = Action(self, "&Help", "Read user guide", ["Ctrl+H"], self.style.standardIcon(self.style.SP_DialogHelpButton))

        self._play_action = Action(self, "&Play", "Start the running", ["Ctrl+P"], self.style.standardIcon(self.style.SP_MediaPlay))
        self._stop_action = Action(self, "S&top", "Stop the running", ["Ctrl+T"], self.style.standardIcon(self.style.SP_MediaStop))
        self._clear_action = Action(self, "&Clear", "Clear the configuration", ["Ctrl+C"], self.style.standardIcon(self.style.SP_LineEditClearButton))

        """Status bar"""
        self._status_bar = self.statusBar()

        """Menu bar"""
        self._menu_bar = self.menuBar()

        self._file_menu = self._menu_bar.addMenu("&File")
        self._file_menu.addAction(self._save_action)
        self._file_menu.addAction(self._open_action)
        self._file_menu.addSeparator()
        self._file_menu.addAction(self._exit_action)

        self._run_menu = self._menu_bar.addMenu("&Run")
        self._run_menu.addAction(self._clear_action)
        self._run_menu.addSeparator()
        self._run_menu.addAction(self._play_action)
        self._run_menu.addAction(self._stop_action)

        self._about_menu = self._menu_bar.addMenu("&About")
        self._about_menu.addAction(self._help_action)
        self._about_menu.addAction(self._info_action)

        """Toolbar"""
        self._toolbar = self.addToolBar("Controls")
        self._toolbar.setMovable(False)
        self._toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self._toolbar.addAction(self._clear_action)
        self._toolbar.addSeparator()
        self._toolbar.addAction(self._play_action)
        self._toolbar.addAction(self._stop_action)

        self._slider = FPSSlider()
        self._toolbar.addWidget(self._slider)

        """Secondary windows"""
        self._info_window = InfoWindow(self, self.style.standardIcon(self.style.SP_MessageBoxInformation))
        self._help_window = HelpWindow(self.style.standardIcon(self.style.SP_DialogHelpButton))

        """Slots binding"""
        self._exit_action.triggered.connect(self.close)
        self._info_action.triggered.connect(self._info_window.show)
        self._help_action.triggered.connect(self._help_window.show)
