"""Write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it
should return “FizzBuzz”."""

def fizz_buzz(n):
    if n%5==0 and n%3==0:
        print("fizz_buzz")
    elif n%5==0:
        print("fizz")
    elif n%3==0:
        print("buzz")
    else:
        print(n)      
n=int(input("enter value:"))    
fizz_buzz(n)    
        
        
        