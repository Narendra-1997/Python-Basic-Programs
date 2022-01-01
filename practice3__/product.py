"""19)Given two integer numbers return their
product and  if the product is greater than 1000,
then return their sum:"""
a=(int(input("enter a value:")))
b=(int(input("enter b value")))

c=a*b
d=a+b
if c>=1000:
    print(d)
else:
    print(c)   
    