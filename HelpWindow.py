from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow


class HelpWindow(QMainWindow):
    """
    Info dialog
    """
    def __init__(self, icon):
        super().__init__()

        """Top level window configuration"""
        self.setWindowTitle("Help")
        self.setWindowIcon(icon)
        self.setFixedSize(500, 300)
        self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
