class a:
    def __init__(self):
        print("a init")

    def a1(self):
        print("class a is access")


class b(a):
    def __init__(self):
        super().__init__()
        print("b init")

    def b1(self):
        print("class b is access")


class c(b):
    def __init__(self):
        super().__init__()
        print("c init")

    def c1(self):
        print("class c is access")


class g:
    def __init__(self):
        print("g init")

    def g1(self):
        print("g is access")


class h:
    def __init__(self):
        print("h init")

    def h1(self):
        print("h is access")

class i:
    def __init__(self):
        print("i init")

    def i1(self):
        print("i is access")


class d(g, h, i):
    def __init__(self):
        super().__init__()
        print("d init")

    def d1(self):
        print("class d is access")


x = a()
x.a1()
print("--------------------------------------------------------a")
z = b()
z.a1()
z.b1()

print("--------------------------------------------------------b")
y = c()
y.b1()
y.a1()
y.c1()
print("--------------------------------------------------------c")
p = d()
p.d1()
p.g1()
p.i1()
print("--------------------------------------------------------d")

