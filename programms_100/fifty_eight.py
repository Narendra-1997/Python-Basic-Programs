"""The fibonacci sequence  is 
computed based on the fallowing foemula"""
"""f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2)if n>1
Please write a program to compute
the value of f(n) with a given n
input by console.
"""
# Example:
# uf the fallowing n is given as input to the
# program 7
# then the out put of the program should be 13
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
# Hints
# We can define recursive function in Python.



def f(n):
    if n==0:return 0
    elif n==1:return 1
    else: return f(n-1)+f(n-2)
n=int(input("N value:"))
print(f(n))    
    
    