"""1)Write a Python program to get the number of occurences of the given character in overall dictionary.
 d = {1:['a', 'G', 'k', 'l'], 2:['G', 'b', 'c'], 3:['a', 'k', 'G', 'c']}
Input: G
Output: 3"""


d = {1:['a', 'G', 'k', 'l'], 
     2:['G', 'b', 'c'], 
     3:['a', 'k', 'G', 'c']}
# d2=d.get(1)
# d3=d.get(2)
# d4=d.get(3)
# print(d2,d3,d4)
# d6=list
l=[]
for i in d.values():
    l.extend(i) 
l2=l.count(input("enter steing::"))  
print(l2) 

    
    
