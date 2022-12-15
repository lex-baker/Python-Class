class A():
    def print(self):
        print("A says:", self.m())
    def m(self):
        return 'foo'

class B(A):
    def m(self):
        return 'bar'

class C(B):
    def m(self):
        return 'baz'

class D(A):
    def m(self):
        return 'blarg'


o = A()
o.print()

q = B()
q.print()

v = C()
v.print()
