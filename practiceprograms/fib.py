import copy


def fib(n):
    l=[]
    a=0
    b=1
    if n==0 or n==1:
        
        l.extend([0,1])
        
    
    for i in range(2,n):
        c=a+b   
        a=b
        b=c
        l.append(copy.deepcopy(c))
        # print(c,end=",")
    print(l)
n=int(input("Enter fib value:"))        
fib(n)

    
        
        
    
    
        
        


        
        
            



