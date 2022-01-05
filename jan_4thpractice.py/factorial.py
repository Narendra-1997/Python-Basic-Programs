"""6)Write a function to 
print the factorial 
of a number."""
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter value:"))   
print(fact(n))     
            