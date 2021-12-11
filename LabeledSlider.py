from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSlider


class LabeledSlider(QWidget):
    """
    Slider with interactive label

    A slider is a small integrated MVC component: the action of sliding (View) modify an internal value (Model)
    (probably thanks to an integrated controller), whose change trigger an update of the view (Controller).
    Model is hidden, obviously, and view and Controller is tightly coupled
    """

    """ [VIEW] """
    def __init__(self, name, min_value, max_value, interval, value):
        super().__init__()
        self._name = name
        self.interval = interval

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        """Slider"""
        self._slider = QSlider(QtCore.Qt.Horizontal)
        self._slider.setMinimum(min_value / interval)
        self._slider.setMaximum(max_value / interval)
        self._layout.addWidget(self._slider)

        """Label"""
        self._label = QLabel()
        self._label.setAlignment(QtCore.Qt.AlignCenter)
        self._layout.addWidget(self._label)

        self.connect(self._update_label)  # [CONTROLLER]
        self._slider.setValue(value / interval)

    def connect(self, slot):
        self._slider.valueChanged.connect(slot)

    """ [CONTROLLER] """
    def _update_label(self):
        self._label.setText(self._name + ": " + str(self._slider.value() * self.interval))
