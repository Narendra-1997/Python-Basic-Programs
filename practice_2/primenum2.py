"""Write a function that prints all the prime 
numbers between 0 and limit 
where limit is a parameter."""

def prime(l):
    lis1=[]
    for i in range(2,l):
        n = False
        for j in range(2,i):
            if i%j==0:
                n = True
        if n is False:
            lis1.append(i)
    return lis1
l=int(input("enter value:"))
lis1=prime(l) 
print(lis1)        
                
                
            
        