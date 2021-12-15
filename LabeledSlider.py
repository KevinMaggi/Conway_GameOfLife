from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSlider


class LabeledSlider(QWidget):
    """
    Slider with interactive label

    A slider is a small integrated MVC component: the action of sliding (View) modify an internal value (Model)
    (probably thanks to an integrated controller), whose change trigger an update of the view (Controller).
    Model is hidden, obviously, and view and Controller is tightly coupled.

    Talking about the whole app it belongs to View/Controller, from the moment that its data (like FPS) are
    substantially a View/Controller parameter and not part of the status (Model)
    """

    """ [VIEW] """

    def __init__(self, name, min_value, max_value, interval, value):
        """
        It initializes both the slider and the label allowing to handle a conversion between slider value (1-stepped)
        and extern value with customizable step
        :param name: text to show in the label
        :type name: string
        :param min_value: external minimum value
        :type min_value: int
        :param max_value: external maximum value
        :type max_value: int
        :param interval: external step
        :type interval: int
        :param value: external initial value
        :type value: int
        """
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
        """
        It allows to connect with the change of slider value
        :param slot: function to invoke
        :return: None
        """
        self._slider.valueChanged.connect(slot)

    def value(self):
        """
        It returns the external value
        :return: int
        """
        return self._slider.value() * self.interval

    def set_value(self, new):
        """
        It allows to set the external value
        :param new: new value
        :type new: int
        :return: None
        """
        self._slider.setValue(new)

    """ [CONTROLLER] """

    def _update_label(self):
        """
        Update the label with the current value
        :return: None
        """
        self._label.setText(self._name + ": " + str(self._slider.value() * self.interval))
