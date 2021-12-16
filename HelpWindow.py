from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QWidget, QHBoxLayout, QStyleFactory, QFrame, QSizePolicy

STYLE = QStyleFactory.create("Fusion")


class HelpWindow(QDialog):
    """
    Info dialog
    """

    def __init__(self, parent, icon):
        super().__init__(parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)

        """Top level window configurations"""
        self.setWindowTitle("Info")
        self._style = parent.style
        self.setWindowIcon(icon)
        self.setFixedSize(500, 500)

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        self._layout.addWidget(QLabel("<h3>Session</h3>"))
        self._layout.addWidget(IconLabel(STYLE.SP_DialogSaveButton,
                                         "<p><b>Save</b>: save the current board population for future reuse</p>"))
        self._layout.addWidget(IconLabel(STYLE.SP_DialogOpenButton,
                                         "<p><b>Open</b>: open a previously saved board population or an example</p>"))
        self._layout.addWidget(QHSeparationLine())
        self._layout.addWidget(QLabel("<h3>Simulation</h3>"))
        self._layout.addWidget(IconLabel(STYLE.SP_MediaPlay,
                                         "<p><b>Run</b>: start the simulation of the game of life from the current population at the setted FPS (can be changed at any time)</p>"))
        self._layout.addWidget(IconLabel(STYLE.SP_MediaPause, "<p><b>Pause</b>: interrupt the running simulation</p>"))
        self._layout.addWidget(IconLabel(STYLE.SP_MediaSkipForward,
                                         "<p><b>Next</b>: update the board to the population at next time step without starting the simulation</p>"))
        self._layout.addWidget(QHSeparationLine())
        self._layout.addWidget(QLabel("<h3>Board</h3>"))
        self._layout.addWidget(IconLabel(STYLE.SP_LineEditClearButton,
                                         "<p><b>Clear</b>: Clear the board. After having cleared it, you can change board size</p>"))


class IconLabel(QWidget):
    HorizontalSpacing = 2

    def __init__(self, icon, text):
        super().__init__()
        self.setFixedSize(450, 50)

        self._layout = QHBoxLayout()
        self.setLayout(self._layout)

        self._icon = QLabel()
        self._icon.setPixmap(STYLE.standardIcon(icon).pixmap(25, 25))
        self._icon.setFixedSize(50, 50)
        self._layout.addWidget(self._icon)

        self._layout.addSpacing(self.HorizontalSpacing)

        self._text = QLabel(text)
        self._text.setFixedSize(375, 50)
        self._text.setWordWrap(True)
        self._layout.addWidget(self._text)


class QHSeparationLine(QFrame):
    """
    a horizontal separation line [from py4u.net]
    """

    def __init__(self):
        super().__init__()
        self.setMinimumWidth(1)
        self.setFixedHeight(10)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setSizePolicy(QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
