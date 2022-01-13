"""Write a function called show_stars(rows). If rows is 5, it should print the following:
*
**
***
****
*****"""

# def Show_stars(rows):
#     for i in range(0,rows):
#         for j in range(i+1):
#             print("*",end=" ")
#         print()
# rows=int(input("enter value;--"))
# Show_stars(rows) 


       
list1=(input("enter value::")).split(",")
# print(list1)
delim=input("enter delim value::")
res1=[ele.split(delim)[0] for ele in list1]
res2=[ele.split(delim)[1] for ele in list1]
print(res1,res2)






