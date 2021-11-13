class A:
    c = 0

    def __init__(self):
        self.a = 1
        self.b = 1


class B(A):
    def __init__(self, v):
        A.__init__(self)
        # self.a = v


class C(A):
    def __init__(self, v):
#        A.__init__(self)
        self.a = v


a = A()
print(a.a, a.b)

b = B(2)
print(b.a, b.b)

c = C(2)
print(c.a, c.b)
