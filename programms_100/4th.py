#write a program which accepts a sequence of comma separatednumbers from console and generate a list and a tuple which contains every number
# uppose the following input is supplied to the program
#34,67,55,33,12,98
# then the output should be
# ('34','67','55','33','12','98')
#  in case of input data being supplied to the queastion it should be assumed to be a console
# tuple() method can convert list to tuple 
# from typing import List


# values=input("input some comma seperated numbers:")
values=list(int(i) for i in input("enter value::").split(",")) 
list=values
tuple= tuple(list)
print('list:',list)
print('tuple:',tuple)