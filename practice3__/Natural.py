"""15)Write a loop to 
find the factorial of any number"""

n = (int(input("enter n value;;")))
s = 1
for i in range(1, n + 1):
    s = s * i
print(s)
