# decorator
 
# def dec1(func):
#     def inner():
#         x=func()
#         return x*x
#     return inner
# def decor(func):
#     def inner():
#         x=func()
#         return 2*x
#     return inner
# @dec1
# # @decor
# def num():
#     return 2
# print(num())


# def div(func):
#     def inner(a,b):
#         if b==0:
#             print("error")
#         else:
#             return func(a,b)
#     return inner
# @div
# def sum(a,b):
#     print(a/b)
# sum(10,8)            
def div (func):
    def inner(a,b):
        if b==0:
            print("error")
        else:
            return func(a,b)
    return inner
@div
def sum (a,b):
    print(a/b)
sum (10,8)
           