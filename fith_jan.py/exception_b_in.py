"""3)Write a python program to 
demonstrate different kinds of 
predefined exceptions."""

# print(dir(locals()['__builtins__']))   

#Arithmetic Error
# try:
#     a=10/0
#     print(a)
# except ArithmeticError:
#     print("this Statement is raising an eror")
# else:
#     print("success")
    
#     #LookupError
    
    
# try:
#     a=[1,2,3]
#     print(a[3])
# except LookupError:
#     print("Index is out of range")
# else:
#     print("success") 
    
    
        #    Exception Attribute error
        
# class Attributes(object):
#     pass
# object=Attributes()
# print(object.attribute)

#   exception EOFErro     
# while True:

    # data=input("enter name:")
    # print("hello",data)  
    
    
    # exception Floating point DError
# import math
# print(math.exp(10))   

#  Exception GeneratorExit


def my_generator():
    try:
        for i in range(5):
            print("yielding",i)
            yield i
    except GeneratorExit:
        print("Exiting early")
g=my_generator()
print(g.next()) 
g.close()               
                                                          