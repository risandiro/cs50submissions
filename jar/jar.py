class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity is too small")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Jar is not big enough")
        self.size = self.size + n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Not enough cookies in the jar")
        self.size = self.size - n

'''
    @property
    def capacity(self):

    @property
    def size(self):
'''

jar = Jar()
jar.deposit(2)
print(jar)
jar.deposit(8)
print(jar)
jar.withdraw(5)
print(jar)
jar.withdraw(4)
print(jar)

