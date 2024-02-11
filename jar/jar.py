class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity is too small")
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
        self._size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
jar.capacity()
jar.deposit(2)
jar.size()
jar.deposit(8)
print(jar)
jar.withdraw(5)
print(jar)
jar.withdraw(4)
print(jar)

def __add__(self, other):
    galleons = self.galleons + other.galleons
    sickles = self.sickles + other.sickles
    knuts = self.knuts + other.knuts
    return Vault(galleons, sickles, knuts)
