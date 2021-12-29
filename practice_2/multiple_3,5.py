"""Write a function that returns the sum of multiples of 3 and 5 
between 0 and limit (parameter). For example, if limit 
is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20."""


def sum_multiples(m):
    l=[]
    for i in range(1,m):
        if i%5 and i%3==0:
            
            l.append(i)
    print(l)
m=(int(input("enter value:")))
sum_multiples(m)           
        