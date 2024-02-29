class Person:
    #attributes (values/features) below
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase

#add methods (functions)
    def walk(self):
        print("Walking...")

    def run(self):
        print("Running...")

#create instances of the person class
#instance means to use the class in other parts of our code
user = Person(25, 80, 177, "Jon", "Snow", "You know nothing, Jon Snow")
print(user.catch_phrase)

#execute method
user.walk()
print()

class Bottle:
    def __init__(self, volume, type_):
        self.volume = volume
        self.type_ = type_

    def pour(self):
        print("Pouring...")

    def fill(self):
        print("Filling...")

    def recycle(self):
        print("Recycling...")

water = Bottle(69, "plastic")
print(water.volume)