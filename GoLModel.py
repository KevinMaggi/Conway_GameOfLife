import numpy
from scipy import signal

from Observable import Observable


class GoLModel:
    KERNEL = numpy.array([[1, 1, 1],
                          [1, 10, 1],
                          [1, 1, 1]])

    def __init__(self, size):
        self._board = Observable()
        self._size = size
        self.reset(self._size)

    def reset(self, size=None):
        if size is not None:
            self._size = size
        self._board.value = numpy.zeros((self._size, self._size), numpy.int)

    def board(self):
        return self._board.value

    def size(self):
        return self._size

    def observe(self, slot):
        self._board.observe(slot)

    def next_status(self):
        actual = self._board.value
        convolution = signal.convolve2d(actual, self.KERNEL, 'same', 'fill')
        new = numpy.zeros((self._size, self._size), numpy.int)
        new[convolution == 12] = 1
        new[convolution == 13] = 1
        new[convolution == 3] = 1
        self._board.value = new

    def toggle_cell(self, i, j):
        old = self._board.value[i, j]
        if old == 1:
            self._board.value[i, j] = 0
        else:
            self._board.value[i, j] = 1
        self._board.notify()

    def activate_cell(self, i, j):
        self._board.value[i, j] = 1
        self._board.notify()
