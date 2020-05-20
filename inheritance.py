class x:
    def a(self):
        print("a is access")

    def b(self):
        print("b is access")


class y(x):
    def c(self):
        print("c is access")

    def d(self):
        print("d is access")

class z(y):
    pass

a1 = y()
a1.a()
a1.c()
a1.b()
a1.d()
a2 = z()
