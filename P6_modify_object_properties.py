#objects can contain methods. methods in objects are functions that belong to the object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def statement(self):
        print("Hello, my name is", self.name)

person1 = Person("Frankie", 17)

#change age property
person1.age = 16
print(person1.age)
person1.statement()
