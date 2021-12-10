from PyQt5.QtCore import pyqtSignal, QObject


class Observable(QObject):
    """
    Observable object
    """
    valueChanged = pyqtSignal(object)

    def __init__(self, val=None):
        super().__init__()
        self._value = val

    def observe(self, slot):
        """
        Allows to an observer to observe this object
        :param slot: function to call on status change
        """
        self.valueChanged.connect(slot)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new):
        self._value = new
        self.valueChanged.emit(self.value)

    def notify(self):
        """
        Allows to emit the signal also if the value has not changed
        :return:
        """
        self.valueChanged.emit(self.value)
