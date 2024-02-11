class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Jar is not big enough")
        self._size = self.size + n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Not enough cookies in the jar")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return size.self



jar = Jar(10)
jar.deposit(5)
print(jar)
jar.withdraw(2)
print(jar)
print(f"{jar.size} / {jar.capacity}")
