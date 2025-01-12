from PyQt5.QtWidgets import QApplication

from GoLController import GoLController
from GoLModel import GoLModel
from GoLWindow import GoLWindow
import Parameters


class GoLApp(QApplication):
    def __init__(self, args=None):
        if args is None:
            args = []

        QApplication.setStyle('Fusion')
        super().__init__(args)

        # [MODEL]
        model = GoLModel(Parameters.BOARD_INITIAL_SIZE)

        # [VIEW]
        view = GoLWindow()
        view.show()

        # [CONTROLLER]
        controller = GoLController(view, model)

        self.exec_()
