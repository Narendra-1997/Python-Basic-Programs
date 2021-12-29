"""define a class named circle which can be constructed
 by a radius. the circle claa has amethod which can compute the area"""
 
 
 #use def method namme (self) to define a method 
 
 
class circle(object):
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
    
    
aCircle= circle(2)
print(aCircle.area())        
        
        