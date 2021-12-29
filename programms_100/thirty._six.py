"""define a function which can generate and print a tuple where 
the value are squer of numbers between 1 and 21 (both included"""
# hint:
#use ** operator to get power of a number
#use rabge () for loops
#use list.append()to add vlues to list
# use tuple() to get a tuple from list



#solution:--


def functuple():
    list=[]
    for i in range(1,11):
        list.append(i**2)
    print(tuple(list))
functuple()    