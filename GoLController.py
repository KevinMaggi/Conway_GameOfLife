from PyQt5.QtCore import QTimer, QEvent
from PyQt5.QtWidgets import QMessageBox


class GoLController:
    def __init__(self, view, model):
        self._view = view

        self._view.connect_exit(self.exit)
        self._view.connect_info(self.info)
        self._view.connect_help(self.help)
        self._view.connect_size(self.reset_model_board)
        self._view.connect_clear(self.ask_clear_confirm)
        self._view.connect_next(self.next)
        self._view.board.connect_mouse(self.mouse)
        self._view.connect_run(self.run)
        self._view.connect_pause(self.pause)
        self._view.connect_fps(self.fps)

        self._timer = QTimer()
        self._timer.setInterval(1000 / self._view.fps_slider.value())
        self._timer.timeout.connect(self.next)

        self._model = model
        self._model.observe(self.refresh_view_board)

        self.refresh_view_board()

    def exit(self):
        self._view.close()

    def info(self):
        self._view.info_window.show()

    def help(self):
        self._view.help_window.show()

    def reset_model_board(self):
        self._model.reset(self._view.size_slider.value())

    def refresh_view_board(self):
        self._view.board.refresh(self._model.board())

    def ask_clear_confirm(self):
        ans = self._view.clear_confirm.exec_()
        if ans == QMessageBox.Ok:
            self.clear()

    def clear(self):
        self._model.reset()
        self._view.set_empty()

    def next(self):
        self._model.next_status()

        if self._model.is_empty():
            self._view.set_empty()
            if self._timer.isActive():
                self.pause()
        else:
            self._view.set_not_empty(self._timer.isActive())

    def run(self):
        self._timer.start()
        self._view.board.disconnect_mouse(self.mouse)
        self._view.running_on()

    def pause(self):
        self._timer.stop()
        self._view.board.connect_mouse(self.mouse)
        self._view.running_off()

        if self._model.is_empty():
            self._view.set_empty()
        else:
            self._view.set_not_empty(self._timer.isActive())

    def fps(self):
        self._timer.setInterval(1000 / self._view.fps_slider.value())

    def mouse(self, event):
        cell_size = int(self._view.board.px_dim / self._model.size())
        border = (self._view.width() - cell_size * self._model.size()) / 2
        x = int((event.x() - border) / cell_size)
        y = int((event.y() - border) / cell_size)

        if event.type() == QEvent.MouseButtonPress:
            self._model.toggle_cell(x, y)
        elif event.type() == QEvent.MouseMove:
            self._model.activate_cell(x, y)

        if self._model.is_empty():
            self._view.set_empty()
        else:
            self._view.set_not_empty(self._timer.isActive())
