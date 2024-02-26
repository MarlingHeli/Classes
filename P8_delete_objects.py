class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def statement(self):
        print("Hello, my name is", self.name)

person1 = Person("Frankie", 17)

#delete person1
del person1

print(person1)
