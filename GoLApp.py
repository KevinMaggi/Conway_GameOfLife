from PyQt5.QtWidgets import QApplication

from GoLController import GoLController
from GoLWindow import GoLWindow


class GoLApp(QApplication):
    def __init__(self, args=None):
        if args is None:
            args = []

        QApplication.setStyle('Fusion')
        super().__init__(args)

        view = GoLWindow()
        view.show()

        controller = GoLController(view)

        self.exec_()
