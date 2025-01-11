class Jar:
    def __init__(self, capacity=12, size = 0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        cookies = []
        for _ in range(self.size):
            cookies.append("🍪")
        string =  "".join(cookies)
        return string

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("Cookies have exceed capacity")
        self.size = self._size + n

    def withdraw(self, n):
        if n:
            if n > self._size:
                raise ValueError("There is not so many cookies")
            self.size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity should be a positive number")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("size should be a positive number")
        self._size = size

def main():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    print(jar)
    jar.deposit(2)
    print(jar)


if __name__ == "__main__":
    main()