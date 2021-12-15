from PyQt5.QtWidgets import QMessageBox


class GoLController:
    def __init__(self, view, model):
        self._view = view

        self._view.connect_exit(self.exit)
        self._view.connect_info(self.info)
        self._view.connect_help(self.help)
        self._view.connect_size(self.reset_model_board)
        self._view.connect_clear(self.ask_clear_confirm)

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
