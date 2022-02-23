def fact(a):
    l=[]
    n=1
    if a<0:
        print("not possible")
    elif a==1:
        print("fact is 1")
    else:
        for i in range(1,a+1):
            n=n*i
            l.append(n)
        print(l)
        
a=int(input("enter value:"))    
fact(a)
    
        
    
    
            
        