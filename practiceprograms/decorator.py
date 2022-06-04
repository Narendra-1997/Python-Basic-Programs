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
# def div (func):
#     def inner(a,b):
#         if b==0:
#             print("error")
#         else:
#             return func(a,b)
#     return inner
# @div
# def sum (a,b):
#     print(a/b)
# sum (10,8)


# def shout(text):
#     return text.upper()
#
#
# print(shout('hello'))
# yell = shout
# print(yell('fellow'))

# def narendra(a,b):
#     c=a+b
#     return c
# print(narendra(12,21))
# add=narendra
# print(add(12,23))
# def shout(text):
#     return text.upper()
#
#
# def scream(text):
#     return text.lower()
#
#
# def greet(text):
#     greeting=text("hi narendra ")
#     print(greeting)
#
# greeting = greet
# greeting(shout)
# greeting(scream)


# def Create_adder(x):
#     def adder(y):
#         return x + y
#
#     return adder
#
#
# an_adder = Create_adder(23)
# print(an_adder(34))


# def hello_dec(func):
#     def inner():
#         print('hi narendra')
#
#         func()
#         print("he3llo ")
#
#     return inner
#
#
# def function():
#     print('this is function')
#
#
# fun = hello_dec(function)
# fun()


# import time
# import math
#
#
# def calc_time(func):
#     def inner1(*args, **kwargs):
#         begin = time.time()
#         func(*args, *kwargs)
#         end = time.time()
#         print("total time take in :", func.__name__, end - begin)
#
#     return inner1
#
#
# @calc_time
# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))
#
#
# factorial(5)

#
# def hello_decorator(func):
#     def inner1(*args, **kwargs):
#         print("before arguments")
#         returned_value = func(*args, **kwargs)
#         print("After exiicution")
#         return returned_value
#
#     return inner1
#
#
# @hello_decorator
# def sum_of_two_numbers(a, b):
#     print("inside the function")
#     return a + b
#
#
# a, b = 1, 2
#
# print("sum=", sum_of_two_numbers(a, b))
