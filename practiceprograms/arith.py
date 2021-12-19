from practiceprograms.programms_100 import first

# store input numbers
num1=input("enter first number")
num2=input("enter second number")
# add two numbers
sum=float(num1)+float(num2)
#subtract two numbers
min=float(num1)-float(num2)
#multiply two numbers
mul=float(num1)*float(num2)
#divide two numbers
div=float(num1)/float(num2)
#display the sum
print("the sum of {0}and{1}is{2}".format(num1,num2,sum))
# display the subtraction
print("the subtraction of {0}and{1}is{2}".format(num1,num2,min))
#display multiplycation
print("the multiplication of{0}and{1}is{2}".format(num1,num2,mul))
#display the divisin
print("the division of{0}and{2}is{0}".format(num1,num2,div))
