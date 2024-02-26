#self parameter refers to the current instance of the class
#self parameter is used to access variables that belong to the class
#it does not have to be called self but it has to be the first parameter in the brackets

class Cat:
    def __init__(cat, name, age):
        cat.name = name
        cat.age = age

    def statement(string):
        #string is the new self parameter?
        #needs argument to print name
        print(f"{string.name} is a silly cat :3")

cat1 = Cat("Chien", 17)
cat1.statement()