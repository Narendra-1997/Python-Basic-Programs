"""1)Write a simple Python function
to check whether x is even or odd"""

def find_number(x):
    if x%2==0:
        print(x,"is even")
    else:
        print(x,"is odd")
x=int(input("enter number:"))
find_number(x)        
        