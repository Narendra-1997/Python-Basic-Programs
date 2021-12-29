"""define a function which can genarate a dictionary where the keys are numbers betwwen 1,21(boyh included)
and the values are squers of keys the functio should just printthe values only"""
"""hint:---
use dict[key]=value pattern to put entry into a dictionary"""

#use ** operator to get power of number
#use range()for loops.
#use keys() to iterate keys in the dictionary also we can use item()
#to get key/values paires


def dictvalues():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for (keys,value) in d.items():
        print(keys,end=" ")
dictvalues()        