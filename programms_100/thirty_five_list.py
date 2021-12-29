"""define a function which can genarate and print in list where the values are squer of numbers 1and 20 """
# hint:---

"""use ** operator to get power of a number.
use range for loops.
use list.append() to add values into a list"""



def listvalues():
    list=[]
    for i in range(1,20):
        i=i**2
        list.append(i)
    print(list)
listvalues()        
     