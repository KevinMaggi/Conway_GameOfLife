from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene


class GoLBoard(QGraphicsView):
    mouse = pyqtSignal(object)

    def __init__(self, parent, px_dim=500):
        super().__init__(parent)

        self.px_dim = px_dim

        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(QBrush(QtCore.Qt.black))

        self.setScene(self.scene)

    def refresh(self, board):
        cell_dim = board.shape[0]
        cell_size = int(self.px_dim / cell_dim)

        self.scene.clear()
        self.scene.setSceneRect(0, 0, cell_size * cell_dim, cell_size * cell_dim)

        for i in range(cell_dim):
            for j in range(cell_dim):
                if board[i, j] == 0:
                    brush = QBrush(QtCore.Qt.white)
                else:
                    brush = QBrush(QtCore.Qt.green)
                self.scene.addRect(i * cell_size, j * cell_size, cell_size, cell_size, QPen(QtCore.Qt.black), brush)

    def mousePressEvent(self, event):
        self.mouse.emit(event)

    def mouseMoveEvent(self, event):
        self.mouse.emit(event)

    def connect_mouse(self, slot):
        self.mouse.connect(slot)

    def disconnect_mouse(self, slot):
        self.mouse.disconnect(slot)
