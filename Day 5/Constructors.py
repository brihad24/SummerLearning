from unicodedata import name


class Point:
    def __init__(self, x, y): # This is a constructor
        self.x = x # Self is a reference to the current object
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

# Constructor is a fucntion that's called at the time of creating an object

point = Point(10, 20)
print(point.x)

#########################################################

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()