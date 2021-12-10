from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSlider


class FPSSlider(QWidget):
    """
    Slider with FPS interactive label

    The FPS value can be considered not a part of the main model because it's value modify only the frequency at which
    a "next" function on the main model is called and doesn't hit the real main model (i.e. the cells population).
    Furthermore a Slider can be considered itself a small predefined MVC: the action of sliding (View) modify an
    internal value (Model) (probably thanks to an integrated controller), whose change trigger an update of the
    view (Controller).
    """
    def __init__(self):
        super().__init__()

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        """Slider"""
        self.fps = QSlider(QtCore.Qt.Horizontal)
        self.fps.setMinimum(1)
        self.fps.setMaximum(10)
        self.fps.setTickInterval(1)
        self.fps.setValue(2)
        self._layout.addWidget(self.fps)
        self.fps.valueChanged.connect(self._update_label)

        """Label"""
        self._fps_label = QLabel()
        self._fps_label.setAlignment(QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._fps_label)
        self._update_label()

    def _update_label(self):
        self._fps_label.setText("FPS: " + str(self.fps.value()))
