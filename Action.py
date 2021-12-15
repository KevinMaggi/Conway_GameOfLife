from PyQt5.QtWidgets import QAction


class Action(QAction):
    """
    A QAction complete with tips and shortcuts
    """

    def __init__(self, parent, name, tip, shortcuts, icon=None):
        """
        :param parent: parent
        :type parent: QObject
        :param name: name
        :type name: str
        :param tip: tips' text
        :type tip: str
        :param shortcuts: shortcuts
        :type shortcuts: Iterable[Union[QKeySequence, StandardKey, str, int]]
        :param icon: icon
        :type icon: QIcon
        """
        if icon is not None:
            super().__init__(icon, name, parent)
        else:
            super().__init__(name, parent)

        self.setStatusTip(tip)
        self.setToolTip(tip)
        self.setShortcuts(shortcuts)
