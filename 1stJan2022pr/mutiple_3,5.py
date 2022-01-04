"""6)Write a function that returns 
the sum of multiples of 3 and 5 
between 0 and limit (parameter). 
For example, if the limit is 20,
it should return the sum of 3, 5,
6, 9, 10, 12, 15, 18, 20."""


mul=int(input("enter range::"))
l=[]
for i in range(1,mul+1):
    if i%5==0 or i%3==0:
        l.append(i)
print(l)        
        