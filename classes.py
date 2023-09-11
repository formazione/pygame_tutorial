class B:
    def b(self):
        print('b')


class C:
    def c(self):
        print('c')


class D(B, C):
    def d(self):
        print('d')


d = D()
d.b()
d.c()
d.d()
