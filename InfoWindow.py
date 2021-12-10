from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel


class InfoWindow(QDialog):
    """
    Info dialog
    """
    def __init__(self, parent, icon):
        super().__init__(parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)

        """Top level window configurations"""
        self.setWindowTitle("Info")
        self._style = parent.style
        self.setWindowIcon(icon)
        self.setFixedSize(400, 200)

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        self._credits = QLabel("<h1>Powered by Kevin Maggi</h1>", self)
        self._credits.setAlignment(QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._credits)

        self._more_text = """<p>This work is part of the exam of <b>Human Computer Interaction</b> by Prof. <i>Andrew D. Bagdanov</i> in Laurea Magistrale in Ingegneria Informatica at University of Florence.</p>"""
        self._more = QLabel(self._more_text, self)
        self._more.setWordWrap(True)
        self._more.setAlignment(QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._more)

        self._link = QLabel("<a href='https://github.com/KevinMaggi/Conway_GameOfLife'>https://github.com/KevinMaggi/Conway_GameOfLife</a>", self)
        self._link.setOpenExternalLinks(True)
        self._link.setAlignment(QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._link)
