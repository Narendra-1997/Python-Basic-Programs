# def simple():
#     for i in range(0,10):
#         if i%2==0:
#          yield i
# for i in simple():
#     print(i) 
 
 
def multiple_yield():
    str1="fist string"
    yield str1
    str2="string 2"
    yield str2
    str3="string 3"
    yield str3
    
obj=multiple_yield()
print(next(obj))
print(next(obj))
print(next(obj))         
 
           










