"""define a class nmed rectangle which can be constructed by a lendth and width
the Rectangle class has a method which can compute the area"""
#hint:--
#use def method(self) to define a method

#solution:



class Rectangle(object):
    def __init__(self, l, w):
        self.length=l
        self.width=w
    def area(self):
        return self.length*self.width
    
arectangle= Rectangle (2,10)
print(arectangle.area())
   