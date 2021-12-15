import numpy
from scipy import signal

from Observable import Observable


class GoLModel:
    """
    [MODEL]
    This class is the model for GoLApp. It stores the status of the board. Other data such as FPS are not considered
    part of the model, because they aren't related to the status of the application, but only a parameter for
    view/controller operations.
    """

    """
    Convolving the board with this kernel is possible to obtain the next status (practically it consists on counting 
    the neighbours). Central element is higher (than the sum of the others) in order to identify if a cell is a survive 
    or a new born cell.
    """
    KERNEL = numpy.array([[1, 1, 1],
                          [1, 10, 1],
                          [1, 1, 1]])

    def __init__(self, size):
        """
        It initializes the model with an empty Observable board and a board size.
        :param size: board size
        :type size: int
        """
        self._board = Observable()
        self._size = size
        self.reset(self._size)

    def reset(self, size=None):
        """
        Re-sets the board to the empty board
        :param size: board size (if not specified the actual size will be maintained)
        :type size: int
        :return: None
        """
        if size is not None:
            self._size = size
        self._board.value = numpy.zeros((self._size, self._size), numpy.int)

    def board(self):
        """
        It returns the board (as matrix)
        :return: ndarray
        """
        return self._board.value

    def size(self):
        """
        It returns the board size
        :return: int
        """
        return self._size

    def observe(self, slot):
        """
        It allows to observe the board status
        :param slot: function to invoke on changes
        :return: None
        """
        self._board.observe(slot)

    def next_status(self):
        """
        It calculates the next status performing a convolution with the kernel and updates the status
        :return: None
        """
        actual = self._board.value
        convolution = signal.convolve2d(actual, self.KERNEL, 'same', 'fill')
        new = numpy.zeros((self._size, self._size), numpy.int)
        new[convolution == 12] = 1  # if the cell has 2 neighbours
        new[convolution == 13] = 1  # if the cell has 3 neighbours
        new[convolution == 3] = 1  # if the spot has 3 near cell alive
        self._board.value = new

    def toggle_cell(self, i, j):
        """
        It toggles the status of a cell.
        Being that it not update the reference of the board (i.e. all the board), but only a element (of the complex
        object), the change signal will not be emitted, so it is emitted manually.
        :param i: x-coordinate of the cell
        :type i: int
        :param j: y-coordinate of the cell
        :type j: int
        :return: None
        """
        old = self._board.value[i, j]
        if old == 1:
            self._board.value[i, j] = 0
        else:
            self._board.value[i, j] = 1
        self._board.notify()

    def activate_cell(self, i, j):
        """
        It make a cell born.
        Being that it not update the reference of the board (i.e. all the board), but only a element (of the complex
        object), the change signal will not be emitted, so it is emitted manually.
        :param i: x-coordinate of the cell
        :type i: int
        :param j: y-coordinate of the cell
        :type j: int
        :return: None
        """
        self._board.value[i, j] = 1
        self._board.notify()

    def is_empty(self):
        """
        It allows to check if the board is empty or not
        :return: bool
        """
        if numpy.sum(self._board.value) == 0:
            return True
        else:
            return False
