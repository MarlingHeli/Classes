#delete object properties using del

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def statement(self):
        print("Hello, my name is", self.name)

person1 = Person("Frankie", 17)

#delete age property
del person1.age

print(person1.age)