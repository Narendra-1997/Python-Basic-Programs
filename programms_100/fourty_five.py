"""define a class named shape and its subclass square. the squere
class has an init function which takes a length as arguments
both classes have a area function which can print the area of the shape where shape's area is 0 by default
"""
#hints:---
#to override a method in super class , we can define a method with the same name in the super class
#solution:---


class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class square(Shape):
    def __init__(self,l):
        shape(_init__(self))
        self.length=1
    def area(self):
        return self.length*self.length   
aSquare=square(56)
print(aSquare.area())    