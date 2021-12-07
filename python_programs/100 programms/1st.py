# from os import linesep


# question 1
# level 1
# question:
# write a program
# which will find all such numbers which are divisible dy 7 but are not amultiple of 5
# between 2000 and 3200 (both included)
# the numbers obtained should be prited in comma separated sequence on sigle line
# hints:
# cosider use range(#begin,#end) method
# solution:
l=[]
for i in range(2000, 3200):
    if(i%7==0)and(i%5!=0):
        i.append(str(i))
        print(join(l))
        
