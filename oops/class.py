# polymorphism : one name many forms
# encapsulation : hidind data and allowing controlled access
# inheritance : reuse properties/methods from a parent class
# abstraction : hidind unnecessary details


# Inside class	__init__()	Initialize object
# Inside folder	__init__.py	Make folder a package

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)   # call parent constructor
        self.age = age

    def show(self):
        print(self.name, self.age)


s = Student("Raj", 25)
s.show()