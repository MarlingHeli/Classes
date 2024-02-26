#str() controls what should be returned when the class object is represented as a string
#if the str() is not set, it will return the string version of the object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        #prints name. prints age in brackets
        return f"{self.name} ({self.age})"

object = Person("Chien", 17)

print(object)

