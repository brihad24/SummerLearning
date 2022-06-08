class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point() # Here, Point() is an object, which is used to call the functions in the object class. Each object is a different instance of our class
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw() # .draw() is a method in the Point class

point2 = Point()
point2.x = 1
print(point2)