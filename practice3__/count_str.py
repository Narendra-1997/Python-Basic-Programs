"""4)Write a Python program to count the
number of characters 
(character frequency) in a string
Sample String: google.com'
Expected Result : {'o': 3, 'g': 2,
'.': 1, 'e': 1, 'l': 1, 
'm': 1, 'c': 1}"""


str1=input("string::")
dict={}
for i in str1:
    print(i)
    keys =dict.keys()
    if i in keys:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)          
    


