"""16)Use a loop to find elements from a 
given list that are present at even positions.
Input: [10, 20, 30, 40,
        50, 60, 70, 80, 90, 100]
Output: [20, 40, 60, 80, 100]"""

l= [10, 20, 30, 40,
        50, 60, 70, 80, 90, 100]

l2=[]
for i in range(0,len(l)):
    if i%2:
        l2.append(l[i])
print(l2)