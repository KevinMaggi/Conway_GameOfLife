from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QBrush, QPen, QColor
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QWidget, QHBoxLayout, QStyleFactory, QFrame, QSizePolicy, \
    QGraphicsView, QGraphicsScene

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
        self.setFixedSize(500, 750)

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        self._layout.addWidget(QLabel("<h3>Session</h3>"))
        self._layout.addWidget(IconLabel(STYLE.SP_DialogSaveButton,
                                         "<p><b>Save</b>: save the current board population for future reuse</p>"))
        self._layout.addWidget(IconLabel(STYLE.SP_DialogOpenButton,
                                         "<p><b>Open</b>: open a previously saved board population or an example</p>"))
        self._layout.addWidget(QHSeparationLine())
        self._layout.addWidget(QLabel("<h3>Simulation</h3>"))
        self._layout.addWidget(QLabel(
            "<p>Lighter cells are newly born, darker ones are old cells still alive; grayed spots indicates just died cells</p>").setWordWrap(
            True))
        self._layout.addWidget(IconLabel(STYLE.SP_MediaPlay,
                                         "<p><b>Run</b>: start the simulation of the game of life from the current population at the setted FPS (can be changed at any time)</p>"))
        self._layout.addWidget(IconLabel(STYLE.SP_MediaPause, "<p><b>Pause</b>: interrupt the running simulation</p>"))
        self._layout.addWidget(IconLabel(STYLE.SP_MediaSkipForward,
                                         "<p><b>Next</b>: update the board to the population at next time step without starting the simulation</p>"))
        self._layout.addWidget(QHSeparationLine())
        self._layout.addWidget(QLabel("<h3>Board</h3>"))
        self._layout.addWidget(IconLabel(STYLE.SP_LineEditClearButton,
                                         "<p><b>Clear</b>: Clear the board. After having cleared it, you can change board size</p>"))
        self._layout.addWidget(QHSeparationLine())
        self._layout.addWidget(QLabel("<h3>Color Legend</h3>"))
        self._colors = QHBoxLayout()
        self._layout.addLayout(self._colors)
        self._colors.addWidget(ColorLabel(0, 150, 0, "<p>Newly born cell</p>"))
        self._colors.addWidget(ColorLabel(0, 215, 0, "<p>Old cell still alive</p>"))
        self._colors.addWidget(ColorLabel(215, 215, 215, "<p>Just died cell</p>"))
        self._colors.addWidget(ColorLabel(255, 255, 255, "<p>Free spot</p>"))


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


class ColorLabel(QWidget):
    HorizontalSpacing = 2

    def __init__(self, r, g, b, text):
        super().__init__()
        self.setFixedSize(115, 100)

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        self._color = QGraphicsView()
        self._color.setFixedSize(25, 25)
        self._color.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self._color.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self._color_scene = QGraphicsScene()
        self._color_scene.setBackgroundBrush(QBrush(QtCore.Qt.black))
        self._color.setScene(self._color_scene)
        self._color_scene.addRect(0, 0, 22, 22, QPen(QtCore.Qt.black), QBrush(QColor(r, g, b)))
        self._layout.addWidget(self._color)

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
