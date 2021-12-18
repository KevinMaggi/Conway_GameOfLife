import numpy

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QBrush, QPen, QColor
from PyQt5.QtWidgets import QWidget, QGraphicsView, QGraphicsScene


class GoLBoard(QGraphicsView):
    """
    [VIEW]
    Interactive board with mouse events
    """

    """
    Signal for mouse events
    """
    mouse = pyqtSignal(object)

    def __init__(self, parent, px_dim=500):
        """
        Initialize the board (square)
        :param parent: parent widget
        :type parent: QWidget
        :param px_dim: board dimension in pixel
        :type px_dim: int
        """
        super().__init__(parent)

        self.px_dim = px_dim

        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(QBrush(QtCore.Qt.black))
        self.setScene(self.scene)

    def refresh(self, board):
        """
        It refresh the board. Alive cells are green, free spots are white
        :param board: board status
        :type board: ndarray
        :return: None
        """
        cell_dim = board.shape[0]
        cell_size = int(self.px_dim / cell_dim)

        self.scene.clear()
        self.scene.setSceneRect(0, 0, cell_size * cell_dim, cell_size * cell_dim)

        for i in range(cell_dim):
            for j in range(cell_dim):
                if board[i, j] == 0:  # free spot that was already free
                    brush = QBrush(QtCore.Qt.white)
                elif board[i, j] == 1:  # still alive cell
                    brush = QBrush(QColor(0, 150, 0))
                elif board[i, j] == -1:  # just dead cell
                    brush = QBrush(QColor(215, 215, 215))
                elif board[i, j] == 2:  # newly born cell
                    brush = QBrush(QColor(0, 215, 0))
                self.scene.addRect(i * cell_size, j * cell_size, cell_size, cell_size, QPen(QtCore.Qt.black), brush)

    def mousePressEvent(self, event):
        self.mouse.emit(event)

    def mouseMoveEvent(self, event):
        self.mouse.emit(event)

    def connect_mouse(self, slot):
        """
        It allows to connect to mouse events (press or move)
        :param slot: function to invoke
        :return: None
        """
        self.mouse.connect(slot)

    def disconnect_mouse(self, slot):
        """
        It allows to disconnect from mouse events
        :param slot: function to not invoke anymore
        :return: None
        """
        self.mouse.disconnect(slot)
