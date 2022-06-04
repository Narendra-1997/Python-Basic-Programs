"""Write a Python program to multiply
all the values in a dictionary wher
all the values are integers."""

d = {1:1,2:3,3:6,5:5}
answer = 1
for i in d:
	print(i)
	answer = answer*d[i]
print(answer)
