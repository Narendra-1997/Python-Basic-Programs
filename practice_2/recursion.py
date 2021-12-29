# def function(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return  n* function (n-1)
# n=int(input("enter number:"))
# result=function(n)
# print(result) 

# import sys
# # print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)

# i=0

# def narendra(name):
#     global i
    
#     i=i+1
#     print(name,i)
        
#     narendra(name)
    
# name=input("enter na me:")  
# narendra(name)


def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
    
result=fact(5)  
print(result)


  

    
    