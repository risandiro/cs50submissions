class Jar:
    def __init__(self, capacity=12):
        if capacity is not int:
            raise ValueError("Only integers supported")
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


def main():
    jar_fred = Jar("9")
    print(f"{jar_fred.size} / {jar_fred.capacity}")
    jar_fred.deposit(5)
    print("+5", jar_fred)
    jar_fred.deposit(3)
    print("+3", jar_fred)
    jar_fred.withdraw(6)
    print("-6", jar_fred)
    print(f"{jar_fred.size} / {jar_fred.capacity}")

if __name__ == "__main__":
    main()
