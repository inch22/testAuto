class A:
    def x(self):
        print('class A')

class B(A):
    def y(self):
        print('class B')

bb = B()
bb.x()

