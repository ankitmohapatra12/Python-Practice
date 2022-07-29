class Parent :
    a = 10
    def __init__ (self) :
        self.b=100
    def display(self) :
        print(self.b)


class Child(Parent) :
    c =20
    def __init__(self):
        self.d =200
    def display(self):
        print(self.d)
        
        


obj = Child()
print(Parent.a)
print(obj.__dict__)
print(obj.display())