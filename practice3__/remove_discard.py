""")Write a program to 
demonstrate difference
b/w discard and remove 
methods on a set"""

s={1,2,3,4,5,6,7,8,9}
s.remove(10)
print(s)   #  it showes error if value is not avilable
s.discard(10)# where it dosnt show
print(s)