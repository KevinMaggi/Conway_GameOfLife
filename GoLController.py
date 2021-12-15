from PyQt5.QtCore import QTimer, QEvent
from PyQt5.QtWidgets import QMessageBox

from GoLWindow import GoLWindow
from GoLModel import GoLModel


class GoLController:
    """
    [CONTROLLER]

    Controller for GoLApp
    """

    def __init__(self, view, model):
        """
        Initialize the controller
        :param view: view
        :type view: GoLWindow
        :param model: model
        :type model: GoLModel
        """
        # view
        self._view = view

        # connect to view's actions
        self._view.connect_save(self.save)
        self._view.connect_open(self.open)
        self._view.connect_exit(self.exit)
        self._view.connect_info(self.info)
        self._view.connect_help(self.help)
        self._view.connect_clear(self.ask_clear_confirm)
        self._view.connect_size(self.reset_model_board)
        self._view.connect_run(self.run)
        self._view.connect_fps(self.fps)
        self._view.connect_pause(self.pause)
        self._view.connect_next(self.next)
        self._view.board.connect_mouse(self.mouse)

        # timer
        self._timer = QTimer()
        self._timer.setInterval(1000 / self._view.fps_slider.value())
        self._timer.timeout.connect(self.next)

        # model
        self._model = model
        self._model.observe(self.refresh_view_board)

        # refresh
        self.refresh_view_board()

    """Slots"""

    def save(self):
        """
        It saves current board
        :return: None
        """
        pass  # TODO

    def open(self):
        """
        It opens saved board
        :return: None
        """
        pass  # TODO

    def exit(self):
        """
        It exits from the app
        :return: None
        """
        self._view.close()

    def info(self):
        """
        It opens info dialog
        :return: None
        """
        self._view.info_window.show()

    def help(self):
        """
        It open help dialog
        :return: None
        """
        self._view.help_window.show()

    def ask_clear_confirm(self):
        """
        It asks confirm to clear
        :return: None
        """
        ans = self._view.clear_confirm.exec_()
        if ans == QMessageBox.Ok:
            self.clear()

    def clear(self):
        """
        It clears the board
        :return: None
        """
        self._model.reset()
        self._view.set_empty()

    def reset_model_board(self):
        """
        It reset the model board
        :return: None
        """
        self._model.reset(self._view.size_slider.value())

    def refresh_view_board(self):
        """
        It refresh the view board and interface
        :return: None
        """
        self._view.board.refresh(self._model.board())

        if self._model.is_empty():
            self._view.set_empty()
            if self._timer.isActive():
                self.pause()
        else:
            self._view.set_not_empty(self._timer.isActive())

    def next(self):
        """
        It invokes the calculation of next status of model board and
        :return: None
        """
        self._model.next_status()

    def run(self):
        """
        It starts the timer to invoke periodically next status
        :return: None
        """
        self._timer.start()
        self._view.board.disconnect_mouse(self.mouse)
        self._view.running_on()

    def pause(self):
        """
        It stops the timer for simulation
        :return: None
        """
        self._timer.stop()
        self._view.board.connect_mouse(self.mouse)
        self._view.running_off()

        if self._model.is_empty():
            self._view.set_empty()
        else:
            self._view.set_not_empty(self._timer.isActive())

    def fps(self):
        """
        It change FPS of timer
        :return: None
        """
        self._timer.setInterval(1000 / self._view.fps_slider.value())

    def mouse(self, event):
        """
        It handles mouse event to activate/toggle model cells
        :return: None
        """
        cell_size = int(self._view.board.px_dim / self._model.size())
        border = (self._view.width() - cell_size * self._model.size()) / 2
        x = int((event.x() - border) / cell_size)
        y = int((event.y() - border) / cell_size)
        print(str(x) + " " + str(y))
        if 0 <= x < self._model.size() - 1 and 0 <= y < self._model.size() - 1:
            if event.type() == QEvent.MouseButtonPress:
                self._model.toggle_cell(x, y)
            elif event.type() == QEvent.MouseMove:
                self._model.activate_cell(x, y)
