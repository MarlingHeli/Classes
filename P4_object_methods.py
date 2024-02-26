#objects can contain methods. methods in objects are functions that belong to the object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def statement(self):
        print("Hello, my name is", self.name)

person1 = Person("Frankie", 17)
#execute function with object
person1.statement()

person2 = Person("Chien", 17)
person2.statement()