class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        cookie ="🍪"*self.size
        return f"{cookie}"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError
        if self.size + n > 12:
            raise ValueError
        self._size = self.size + n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError
        self._size = self.size - n

    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size

