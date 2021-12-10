from PyQt5.QtWidgets import QApplication

from GoLWindow import GoLWindow


class GoLApp(QApplication):
    def __init__(self, args=None):
        if args is None:
            args = []

        QApplication.setStyle('Fusion')  # Windows, WindowsXP, WindowsVista, Fusion
        super().__init__(args)

        window = GoLWindow()
        window.show()

        self.exec_()
