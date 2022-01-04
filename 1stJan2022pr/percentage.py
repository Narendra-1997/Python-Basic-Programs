"""4)Define a list that contains the marks
percentage for the students. Print a 
list that contains the Grades
of the students.The grading will
be decided by the following conditions.
  A+ if the percentage is greater than 90
  A if the percentage is less than or
  equal to 90 and greater than 70
  B if the percentage is less than or
  equal to 70 and greater than 50
  C if the percentage is less than
  or equal to 50 and greater than 35
  F if the percentage is 
  less than or equal to 35"""
  
  
marks=list(int(i) for i in input("enter value:").split(","))
print(marks)
ans=[]
for i in marks:
    
    if i>90:
        ans.append("A+")
    elif i<=90 and i>70:
        ans.append("A")
    elif i<=70 and i>50:
        ans.append("B") 
    elif i<=50 and i>35:
        ans.append("c")
    elif i<35:
        ans.append("f") 
print(ans)           
                 