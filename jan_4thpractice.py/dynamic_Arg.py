"""8)Write a function to
pass dynamicargs and return
the sum of the dynamic args."""


def dynamic(*num):
    sum=0
    for i in num:
        sum=sum+i
    return sum
        
res=dynamic(20,30)
print(res)        
        
          
        
        

    
 