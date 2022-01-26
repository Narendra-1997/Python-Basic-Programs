"""5)Print the type of integer until 
the given index position in 
characters(Even or Odd) 
exclude index 0.
Input: [0,1,2,3,4,6,7,8]
index: 5
Output: ['Odd','Even', 
         'Odd', 'Even', 'Even']"""
l=list(int(i) for i in input("enter value:").split(","))
even=[]
for i in l:
    if i%2==0:
        print("even",end=",")
    else:
        print("odd",end=",")
        
print("iam ok")        
      
                     
         