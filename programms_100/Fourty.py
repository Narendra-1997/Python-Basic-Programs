"""write  a programm which can filter even numbers in the list
by using filter function. the list is [1,2,3,4,5,6,7,8,9,10].
hint:--"""
# use filter () to filter some elements in list
# use lambda to define anonymous function


# solution:--


li=[1,2,3,4,5,6,7,8,9,10]
# li1=list(filter(lambda li:(li%2==0),li))
# print(li1)
res=list(map(lambda x:(x**2),li))
print(res)