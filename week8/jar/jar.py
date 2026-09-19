class Jar:
    # initialises the attributes
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
            self._size = 0

    # return the object as string
    def __str__(self):
        return "🍪"*self.size

    # deposit cookie into jar
    def deposit(self, n):
        if self.size+n > self.capacity:
            raise ValueError
        else:
            self._size = n + self.size

    # withdraw cookie from jar
    def withdraw(self, n):
        if self.size < n:
            raise ValueError
        else:
            self._size = self.size - n

    # returns jar capcity
    @property
    def capacity(self):
        return self._capacity

    # returns number of cookies in the jar
    @property
    def size(self):
        return self._size
