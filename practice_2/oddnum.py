"""Write a function to check if a 
number is prime or not."""


def prime(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    if len(l)>2:
            print("n is not a primr number")
    else:
        print("n is  a prime number")
n=(int(input("Enter any value:")))             
prime(n)
        