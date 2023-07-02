class A:
    def _init_(self, a, b, c):
        self.__a = a
        self._b = b
        self.c = c

    def display(self):
        print(f"a: {self.__a} b: {self._b} c: {self.c}")


class B(A):
    def _init_(self, a, b, c):
        super()._init_(a, b, c)

    def display(self):
        super().display()


try:
    a = A(1,2,3)
    print("A has: ")
    a.display()
    print("values.")

    b = B(10, 20, 30)
    print("B has: ")
    b.display()
    print("values.")

    print(a.__a)
except AttributeError:
    print("not accessible")