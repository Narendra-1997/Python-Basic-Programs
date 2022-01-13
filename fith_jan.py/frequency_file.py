"""6)Write a python program to 
find all the longest words
(which have more than 10
 characters) from the file."""
 
# f=open("longword.txt","w")
# f.write("the word encyclopedia is big")
# f.close()

f2=open("longword.txt","r")
k=f2.read()
l=k.split()
ans=[]


for  i in l:
    if len(i)>=10:
        ans.append(i)
print(ans)        
        
    


    
        
        