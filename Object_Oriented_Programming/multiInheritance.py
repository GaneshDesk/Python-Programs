
# multiple inheritance
class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"


class C(A, B):              # multiple inheritance
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)

# create instance of C class
c = C()
c.showprops()
# method resolution order
print(C.__mro__)