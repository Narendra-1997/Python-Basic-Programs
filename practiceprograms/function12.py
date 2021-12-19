def narendra(country="india"):
    print("   iam from     "+ country )
narendra("chaina")
narendra("bangladesh")
narendra("french")
narendra()
def narendra1(school="dont"):
    print("i go to "+  school)
narendra1("collage")
narendra1("bus")
narendra1()
narendra1("daddy")

# # a=abs(6+7y)
# # print(a) 

# # mylist=[True, True, False]
# # x=all(mylist)
# # print(x)


# # x=ascii("my name is st")



def myfunc(n):
    return lambda a:a*n
name=myfunc(2)
name1=myfunc(9)

# # print(name(2))
# # print(name1(1345)) 



""" def add(a,b):
#     c=a+b
#     return c
# solution=add(1123,34567)
# print(solution)


# def fact(a,b=20):
#     print(a,b)
# fact(8)or(3)"""




# def display(a,b,c):
#     print(a,b,c)
# display(c=67,b=8,a=45)


# def display(*marks):
#     print(marks)
# display(12,3,4,4,5,5,66,67,678,7,7,88889,9,)    


# a=int(input("enter value:"))
# b=int(input("enter value:"))
# c=a+b
# print(c)

# a=3+5j
# print(abs(a))


# def sum():
#     a=23
#     b=29
#     c=a+b
#     return c
# print(sum())

    



# def my_function(name):
#     print("hi", name)
# my_function("jaswik")



# def sum(a,b):
#     return a+b
# a=int(input("enter value of a:"))
# b=int(input("enter value of b:"))
    
    
# print("te sum of a,b is",sum(a,b))




# def change_list(list1):
#     list1.append(20)
#     list1.append(27)
#     print("list inside function:",list1)
# list1=[20,4,5,6,78,]
# change_list(list1)
# print("out side function :",  list1)    


# positional arguments

from os import name


def function(school):
    name="hi   "+ school
    return name
school=input("enter the school::::::")
print(function(school))

