"""Write a python program to 
demonstrate user-defined exceptions."""
# # Attribute error
# X=10
# X.append(6)
# print(X)



# # file not found error
# filename=(input("enter file name"))
# fileScan=open(filename,"r")

# index error

# import sys
# try:
#     my_list=[3,5,6,8,9,]
#     print(my_list[6])
# except IndexError as e:
#     print(e)
# print(sys.exc_type)    
    
# key error exception
# school={1:'Narendra',2:"Nani",3:"jessi"}
# print(school[4])

# name error
# Name="Narendra"
# prit(Name)


# type error
# name="narendra"
# num=10
# print(name+4+name)




# value error
# try:
#     num=7
#     mylist=[]
#     mylist.remove(num)
# except  ValueError:
#     print("Value error")
    
    # Zero division error
try:
    a=3/0
    print(a) 
except ZeroDivisionError :
    print("i know") 
          
        