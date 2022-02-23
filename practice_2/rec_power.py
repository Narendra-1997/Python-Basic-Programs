"""Write a function to calculate power 
of a number raised 
to other ( ab ) using recursion."""


def power(a, b):
    if b == 1:
        return a
    else:
        return a * power(a, b - 1)


print(power(6, 2))
