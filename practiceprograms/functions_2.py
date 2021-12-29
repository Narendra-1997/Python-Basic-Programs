# def my_function():#defining function
#     print("narendra mani")# function dlock
# my_function()# function calling


# def sum():
#     a=2
#     d=7
#     c=a+d
#     return c
# print(sum())
    
    
    
    
# def func(names,age):
#      print ("name of person:",names,"and age is:",age)
# func("narendra",24)       
# print(type(func("names","ages")))


# def sum(a,b):
#     return a+b
# a=int(input("enter a::"))
# b=int(input("enter b::"))
# print(sum(a,b))


def list_changes(list1):
    list1.append(30)
    list1.append(90)
    print("list inside function=",list1)
    
list1=[12,34,5,6,78,2,55,]

list_changes(list1)
print("list out side the function ",list1)


def change_str(str):
    str=str+"hows you"
    print("printing the function is side the function:::",str)
string1="hi iam there"    
change_str(string1)
print("print the string out side the function::",string1)



    





