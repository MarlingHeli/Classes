#__init__() function assigns values to object properties
class Cat:
    def __init__(self, name, meow):
        self.name = name
        self.meow = meow

object = Cat("Mr Whiskers", "Maow")

print(object.name)
print(object.meow)