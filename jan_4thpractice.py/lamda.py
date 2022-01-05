"""4)Write a function that takes a 
list as input param and it returns
two lists one with even, one with 
odd values use the lambda function."""
def list_lamda(l):
    l1=list(filter(lambda x:x%2==0,l))
    print(l1)
    l2=list(filter(lambda x:x%2!=0,l))
    print(l2)
l=list(int(i) for i in input("Enter value::").split(","))   
list_lamda(l) 
