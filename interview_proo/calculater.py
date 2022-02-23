# def sum(a, b):
#     return a + b
#
#
# def sub(a, b):
#     return a - b
#
#
# def mul(a, b):
#     return a * b
#
#
# def div(a, b):
#     return a % b
#
#
# def intre(p, t, r):
#     return p * t * r / 100
#
#
# def intre2(p, t, r):
#     return p * pow((1 + r / 100), t)
#
#
# def sqr(a):
#     return a ** 2
#
#
# def st(num):
#     return num ** 0.5
#
#
# print(st(100))

# str1 = "iam narendra good boy"
# list1=[]
#
# for i in str1.split():
#     list1.append(i[::-1])
#
# print(' '.join(list1))

year = int(input("enter Year:-"))
if year % 4 == 0:
    print(year, "is a leap year")
else:
    print(" not a leap year")
