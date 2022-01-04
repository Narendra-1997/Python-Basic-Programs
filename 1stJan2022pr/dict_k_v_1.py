"""1) Write a program to 
find the characters which
matches with the keys of given 
dictionary and replace them
with theassociated value.
d = {'a' : 'b', 'b' : 'c', 'c': 'a' }
Input: abc
Output: bca"""

d = {'a' : 'b', 'b' : 'c', 'c': 'a' }
# l1=d.keys()
# l2=d.values()
d2=[]
d3=str(input("enter string::"))
k=list(i for i in d3)
for i in k:
    d2.append(d[i])
print(",".join(d2))    
    
    
    
         
        
        
    
    