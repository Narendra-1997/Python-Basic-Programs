"""define a function that can accept two strings as input and print 
the string with maximum length in console if two strings have the same length then the 
function should print all strings line by line"""


# hint:---

# use len () to get the length of a String

def length_value(s1,s2):
    len1=len(s1)
    len2=len(s2)
    if len1>len2:
        print("s1 is big",s1)
    elif len2>len1:
        print("s2 is big",s2)
    else:
        print("equal",s1)
        print("equal",s2)
#     return len1,len2
# len1,len2=length_value()
length_value("sd","three")

     
            