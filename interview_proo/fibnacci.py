# def fib(num):
#     a = 1
#     b = 0
#     print(a, b)
#     for i in range(0, num + 1):
#         c = a + b
#         a = b
#         b = c
#         print(c)
#

# fib(5)
def fib(num):
    a = 0
    b = 1

    print(a, b, end='  ')
    while num-2:
        c = a + b
        a = b
        b = c
        print(c, end='  ')
        num = num - 1


num = int(input("enter range:-"))
fib(num)
