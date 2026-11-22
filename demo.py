import time

class myQueue:
    def __init__(self, size = 10):
        self._content = []
        self._size = size
        self._current = 0

    def setSize(self, size):
        if size < self._current:
                for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

  
