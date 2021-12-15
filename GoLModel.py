import numpy

from Observable import Observable


class GoLModel:
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

    def observe(self, slot):
        self._board.observe(slot)
