"""4)Write a Python program to count the
number of characters 
(character frequency) in a string
Sample String: google.com'
Expected Result : {'o': 3, 'g': 2,
'.': 1, 'e': 1, 'l': 1, 
'm': 1, 'c': 1}"""

str1 = input("string::")
dic = dict()
for i in str1:

    keys = dic.keys()
    if i in keys:
        dic[i] = dic[i]+1
    else:
        dic[i] = 1
print(dic)
