# coding=utf-8
class Base:
    def test(self):
        print("-----Base")

class A(Base):
    def test(self):
        print("-----test-----A")
class B(Base):
    def test(self):
        print("-----test-----B")

class C(B,A):
    pass
    def test(self):
        print("-----test----C")
c=C();
c.test()
print(C.__mro__)