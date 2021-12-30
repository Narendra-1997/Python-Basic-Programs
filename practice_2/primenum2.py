"""Write a function that prints all the prime 
numbers between 0 and limit 
where limit is a parameter."""

def prime(l):
    lis1=[]
    for i in range(2,l+1):
        for j in range(2,i):
            if i%j==0:
                pass
        else:
            lis1.append(i)
l=int(input("enter value:"))
lis1=prime(l) 
print(lis1)        
                
                
            
        