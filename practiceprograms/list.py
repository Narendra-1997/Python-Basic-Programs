# new_list=[23,43,"narendra",2.3,2j]
# print(new_list[1])
# print(new_list[2])
# print(new_list[3])
# print(new_list[4])
# print(new_list[1])

# print(new_list[2:1])
# print(new_list[5:4])
# print(new_list[:4])
# print(new_list[3:])
# # print(new_list[:4:3])
# # #multidimensional list
# ver=[[[1,2],[3,4]],[[5,6],[9,8]]]
# print(ver[1][0])
# for i in ver:
#     print(i)
# for i in range(len(ver)):
#     print(ver[i])

# a=[e+e for e in range(10) if e%2]
# print(a)

# def even_list(l):
#     l1=[]
#     for i in l:
#         if i%2==0:
#             l1.append(i)
#     return l1
# print(even_list([1,2,3,4,5,6,7,8]))    

# l1=[]
# l=list(map(int,input("enter value").split(",")))

# for i in l:
#     if i%2==0:
#         l1.append(i)
# print(l1)        
            

# lis=[1,2,3,59,3,4,32,5,67] 
# x=sorted(lis)
# print(x)



l=[1,2,3]
l2=[4,5,6]
l.append(l2)
print(l)
# l.extend(l2)
# print(l)