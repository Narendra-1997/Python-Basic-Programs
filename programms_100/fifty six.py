"""write a programm to compute
f(n)=f(n-1)+100 when n>0
with a given n input by console (n>0)

example:---
if the fallowing n is given as input to the program:
5
then the output of the program should be 
500

in case of input data being supplied to the 
question ,it should be assumed to be console input"""

# hint:-
# we can define a recurssive function in python

# solution:

def f(n):
    if n==0:
        return 0
    return f(n-1)+100
n=(int(input("enter value:-")))
print(f(n))    
    