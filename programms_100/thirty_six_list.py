"""define a function which can genarate a list where the values are 
squer of numbers between 1 and 20"(both included
then the function needs to print  the last 5 elements in the list""


use ** operator to get power of a number"""
#use range()for loops
#use list.append() to add values into a list


def listindex():
    lis=list()
    for i in range(1,21):
        i=i**2
        lis.append(i)
    print(lis[:-2])
listindex()    
