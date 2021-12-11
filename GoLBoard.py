from PyQt5 import QtCore
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene


class GoLBoard(QGraphicsView):
    def __init__(self, parent, cell_per_side=500, size_px=500):
        super().__init__(parent)

        self._cell_per_side = cell_per_side
        self._cell_size = int(size_px / self._cell_per_side)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, size_px, size_px)
        self.scene.setBackgroundBrush(QBrush(QtCore.Qt.black))

        self.setScene(self.scene)

        for i in range(self._cell_per_side):
            for j in range(self._cell_per_side):
                self.scene.addRect(i * self._cell_size, j * self._cell_size, self._cell_size, self._cell_size,
                                   QPen(QtCore.Qt.black), QBrush(QtCore.Qt.white))
