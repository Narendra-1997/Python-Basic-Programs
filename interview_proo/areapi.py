# from math import pi
#
#
# def circle(a):
#     return pi * a * 2
# def triangle(radias):
#     return 4(pi*radias*2)
#
#
# print(triangle(2))

def list1(values):
    l=[]
    l2=values[0]
    for i in range(1,values):
        if i[0]>l2[1]:
            l2[1]=i[2]
            l.append(i)
            print(l)

values=[[1,3],[2,6],[8,10]]
list1(values)