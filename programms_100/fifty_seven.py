"""te fibanacci sequence is computed based on the fallowing formula

"""
def f(n):
    # n=int(input("enter value"))
    if n==0:
        if n>1:
         return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+(n-2)
n=int(input("enter value"))
print(f(n))


    

    
        
        
        