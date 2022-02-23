def pal(num):
    x = num[::-1]
    if num == x:
        print("it is a palindrome")
    else:
        print("it is not palindrome")


num = input("enter value:-")
pal(num)
