"""write a program to computr 1/2+2/3+3/4+...+n/n+1
with a given n input by console (n>0)
"""
# example:
# if the fallowing n is given as input to the program
# 5
# then the out of the program should be :
# 3.55
# in the case of input data being supplied to the question, it should be assumed to be a console input


# hint:-
#  use flote()to convert an integer to float
# Solution:-

n=int(input("enter value:"))
sum=0.0
for i in range(1,n+1):
    sum=sum+float(float(i)/(i+1))
print(sum)    
