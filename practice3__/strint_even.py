"""20)Given a string, display only
those characters which are 
present at an even index number."""
str=input("enter str:")
s=[]
for i in range(0,len(str)):
    if i%2==0:
        s.append(str[i])
print(s)        
        
