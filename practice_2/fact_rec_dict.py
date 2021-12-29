"""Write a function to find factorial of a number
but also store the factorials calculated in
a dictionary as done in the Fibonacci series example."""

def fact(n):
    if n==0 or n==1:
          return 1
    else:
        return n*fact(n-1)
n=(int(input("enter value:")))     
    
    
dict={i:fact(i) for i in range(1,n)}
        
 
print(dict)     
    
