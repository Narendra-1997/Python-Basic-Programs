"""Write a function “perfect()” that determines if 
parameter number is a perfect number. Use this function in a program that determines and prints all the
perfect numbers between 1 and 1000.
[An integer number is said to be “perfect number” if 
its factors, including 1(but not the number itself), 
sum to the number. E.g., 6 is a perfect number because 
6=1+2+3]."""


# def perfect(n):
#     sum = 1
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             sum = sum + i + n / i
#         i = i + 1
#     return (True if sum == n and n != 1 else False)



n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")


# n = 2
# for n in range(1000):
#     if perfect(n):
#         print(n, "is a perfect number")
