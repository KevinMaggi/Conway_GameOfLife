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
        self._last_board = numpy.zeros((size, size), numpy.int)
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
        self._last_board = numpy.zeros((self._size, self._size), numpy.int)  # update of actual must be last op
        self._board.value = numpy.zeros((self._size, self._size), numpy.int)

    def board(self):
        """
        It returns the board (as matrix)
        :return: ndarray
        """
        return self._board.value

    def board_enriched(self):
        """
        It returns the board enriched with history details (as matrix)
        :return: ndarray
        """
        return numpy.add(self._board.value, numpy.subtract(self._board.value, self._last_board))

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
        self._last_board = actual
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

    def save(self, filename):
        """
        It saves as file the current board
        :param filename: file
        :type filename: str
        :return: None
        """
        if filename is not None and filename != '':
            numpy.savetxt(filename, self._board.value, "%.d",
                          header="Board population from 'Game of Life' by Kevin Maggi")

    def open(self, filename):
        """
        It loads a saved board configuration
        :param filename: file
        :type filename: str
        :return: None
        """
        if filename is not None and filename != '':
            array = numpy.loadtxt(filename, int)
            self._size = array.shape[0]
            self._last_board = numpy.zeros((self._size, self._size), numpy.int)  # update of actual must be last op
            self._board.value = array
