"""Write a function to calculate area and perimeter of a rectangle."""



def areaRectangle(a,b):
    return (a*b)
def perimeterRectangle(a,b):
    return 2*(a+b)
a=int(input("enter a value:"))
b=int(input("enter b value:"))

print("area=",areaRectangle(a,b))
print("perimeter=",perimeterRectangle(a,b))