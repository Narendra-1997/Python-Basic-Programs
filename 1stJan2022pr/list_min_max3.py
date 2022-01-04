"""3)Write a Python program
to get the maximum 
and minimum value from a list 
without using any 
predefined function."""

l=[1,1,2,3,-7,4,5,6,7,8,4]
maxi=l[0]
mini=l[0]
for i in l:
    if i>maxi:
        maxi=i
for i in l:
    if i<mini:
        mini=i        
print(maxi)
print(mini)     
