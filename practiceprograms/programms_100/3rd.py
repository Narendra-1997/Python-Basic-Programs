#print a programm which can compute the factorial of given number
#the results should be printed as comma separated sequence on a single line
#suppose the following input is supplied to the program:8
#then the output should be
#40320
#hint
# in case of input data being supplied to the queastion it should be assumed to be a cons
num=int(input("enter the number"))
factorial=1
if num<0:
     print("factorial does not exist for negative numbers")
elif num==0:
     print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial =factorial*i
    print("the factorial of",num,"is",factorial)
