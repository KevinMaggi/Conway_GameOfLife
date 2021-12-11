class GoLController:
    def __init__(self, view):
        self._view = view

        self._view.connect_exit(self.exit)
        self._view.connect_info(self.info)
        self._view.connect_help(self.help)

    def exit(self):
        self._view.close()

    def info(self):
        self._view.info_window.show()

    def help(self):
        self._view.help_window.show()
