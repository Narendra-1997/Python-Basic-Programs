# def last(n):
#     return n[1]
#
#
# def sort(tuples):
#
#     return sorted(tuples, key=last)
#
#
# print(sort([(1, 6), (3, 5), (6, 7), (7, 7)]))
# test=[1,1,2,2,3,3,4,4,5,5,6,6,7,8,9,7,6,5,3,3]
# t=[]
# for i in test:
#     if i not in t:
#         t.append(i)
# print(t)

# s=[]
# st=input("give strings:--")
# test=st.upper()
# s.append(test)
# for i in s:
#     print(i)


# l = [1,2,1]
#
# if  not l:
#      print("List is empty")
# else:
#     print("list is not empty")
#
# lis = [11, 22, 33, 444, 55]
# lis2 = list(lis)
# print(lis2)

#
# def least(num1, num2):
#     result = False
#     for x in num1:
#         for y in num2:
#             if x == y:
#                 result = True
#                 return result
#
#
# print(least([1, 2, 3, 4, 5], [3,7,8]))

# color=['red','pink','white','black','yello']
# color=[x for (i,x) in enumerate(color) if i not in (0,4,5)]
# print(color)
#
# for i in color:
#     print(i)

#
# array=[[["*"for i in range(6)] for j in range(4)] for k in range(3)]
# print(array)

# def list2(values):
#     lis = []
#     for i in values:
#         if i % 2 != 0:
#             lis.append(i)
#     return lis
#
#
# print(list2([1, 2, 3, 4, 5, 6, 7]))


# from random import shuffle
# lis=[1,2,3,4,5,6]
# shuffle(lis)
# print(lis)


# def test():
#     l = []
#     for i in range(1, 31):
#         l.append(i ** 2)
#     print(l[5:])
#     # print(l[-5:])
#
#
# test()

# import itertools
# print(list(itertools.permutations([1,2,3])))
#
#
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [1, 2, 3, 8, 9, 6]
# list3 = list(set(list1) - set(list2))
# list4 = list(set(list2) - set(list1))
# finnal = list3 + list4
# print(finnal)

# list1=['a','b','c','d','e']
# s=''.join(list1)
# print(s)
# print(type(s))

#
# list1 = [23, 45, 6, 76, 54, ]
# li = enumerate(list1)
# for k, v in li:
#     print(k, v)
# #
# print(list1.index(54))


# import itertools
#
# list1 = [[1, 2, 3], [4, 5, 6], [9], [9, 6, 5]]
# new_list = list(itertools.chain(*list1))
# print(new_list)

# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = [1, 2, 3, 4, 5, ]
# # list2.append(list1)
# # print(list2)
# list3=list1+list2
# print(list3)

# import random
# list1=[1,2,3,4,5,6,7,8,]
# print(random.choice(list1))
# l = [1, 2, 3, 4, 5, 6, 9, 8, 7]
# l.sort()
# l2 = [1, 9, 8, 7, 6, 5, 1, 2, 3]
# l2.sort()
#
# if l == l2:
#     print(True)
# else:
#     print(False)

#
# l = [1, 4, 7, 3, 6, 2, 7, 8, 4]
# l.sort()
# print(l[1])

#
# def list1(numbers):
#     if len(numbers) < 2:
#         return ("list is small")
#     if (len(numbers) == 2) and (numbers[0] == numbers[1]):
#         return ("list is identical")
#     numbers.sort()
#     return numbers[-2]
#
# print(list1([1]))
# print(list1([1, 1]))
# print(list1([1, 34, 65, 78, 97, 3455]))

#
# mylist=[10,10,20,30,30,4,4,50,58,]
# print(mylist)
# my_set=set(mylist)
# new_list=list(my_set)
# print(new_list)

#
# import collections
# mylist=[1,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,6,6,5,5,7,7,8,8,]
# ctr=collections.Counter(mylist)
# print(ctr)


# def count_range_in_list(li, min, max):
#     ctr = 0
#     for x in li:
#         if min <= x <= max:
#             ctr += 1
#     return ctr
#
#
# list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
# print(count_range_in_list(list1, 40, 100))

# list2 = ['a', 'b', 'c', 'd', 'e', 'f']
# print(count_range_in_list(list2, 'a', 'e'))
# def is_Sublist(l, s):
#     sub_set = False
#     if s == []:
#         sub_set = True
#     elif s == l:
#         sub_set = True
#     elif len(s) > len(l):
#         sub_set = False
#
#     else:
#         for i in range(len(l)):
#             if l[i] == s[0]:
#                 n = 1
#                 while (n < len(s)) and (l[i + n] == s[n]):
#                     n += 1
#
#                 if n == len(s):
#                     sub_set = True
#
#     return sub_set
#
#
# a = [2, 4, 3, 5, 7]
# b = [4, 3]
# c = [3, 7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))

# l=[1,2,3,4,5,6,6]
# for k,v in enumerate(l):
#     if k not in (0,2,6):
#         print(v)
# l = [1, 2, 3, 4, 5, 6, 7]
# l2 = []
# for i in l:
#     if i % 2 != 0:
#         l2.append(i)
# print(l2)
# lis1 = [1,3,5,8,4,5,6,7,7,443,3,5,5]
#
# for i in range(len(lis1) - 1, 0, -1):
#     if lis1[i] % 2== 0:
#         lis1.remove(lis1[i])
# print(lis1)


# list1=[1,2,2,3,4,4,5,6,76,2,4,4,5,6]
# set1=set(list1)
# list2=list(set1)
# print(list2)
colors = ['red', 'blue', 'black', 'yellow', 'pink', 'green']

# res=colors[1][1:3]
# print(res)
#
# colors[-2]='gold'
# # print(colors)
# color=[]
# color.append(colors)
# color.append('name')
# color.append('oil')
# color.extend(['white'])
# color.insert(0,'banana')
# print(color)
# print(colors)
# l=color.pop()
# del color[2]
# color.remove('oil')
# print(color)
# print(l)
# print(len(color))
# l2=len(colors)
# print("we have"  "  "  + str(l2) +  "  " "colors")
# print(colors)
# colors.sort()
# print(colors)
# colors.sort(reverse=True)
# print(colors)
# print(sorted(colors))
# print(sorted(colors,reverse=True))
# for i in colors:
#     print("welcome," + i + "!")
# print(" Welcome, we're glad to see you all ! ")

# for i in range(2001):
#     print(i)
# for i in range(1,2001,5):
#     print(i)
# nums=list(range(1,100))
# print(nums)

# numbers=[12,32,43,54,34,76,87,78,]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# print(colors)
# my_color=colors
# print(my_color)
# l=[]
#
# for i in range(1,11):
#     sqr=i**2
#     l.append(sqr)
# print(l)

# sqr=[i**2 for i in range(1,12)]
# print(sqr)
# col2=[cols.upper() for cols in colors]
# print(col2)
#
# l=[]
# for i in  colors:
#     l.append(i.upper())
# print(l)
# def has_duplicates(l):
#     return len(l)==len(set(l))
#
# new_list=[1,2,3,4,5,4]
# print(has_duplicates(new_list))


# l2=[1,2,3,4]
# l3=[1,2,3,4]
# if l2 in l3 or l3 in l2:
#     print(True)
# else:
#     print(False)
# def is_contained_in(l1, l2):
#   for x in set(l1):
#     if l1.count(x) > l2.count(x):
#       return True
#   return False
# print(is_contained_in([1, 2], [2, 4, 1]))
# print(is_contained_in([1], [2, 4, 1]))
# print(is_contained_in([1, 1], [4, 2, 1]))
# print(is_contained_in([1, 1], [3, 2, 4, 1, 5, 1]))
#
# def is_subset(l, s):
#     sub_set = False
#     if not s:
#         sub_set = True
#     elif s == 1:
#         sub_set = True
#     elif len(s) > len(l):
#         sub_set = False
#     # elif len(s) < len(l):
#     #     sub_set = False
#     else:
#         for i in range(len(l)):
#
#             if l[i] == s[0]:
#                 n = 1
#                 while (n < len(s)) and (l[i + n] == s[n]):
#                     n = n + 1
#                     if n == len(s):
#                         sub_set = True
#                 return sub_set
#
#
# b = [1, 2, 3, 4, 5]
# a = [4, 3]
#
# # c = [3, 7]
# print(is_subset(a, b))


# x=100
# # print(id(x))
# print(format(id(x),"x"))
# s="narendra"
# # print(id(s))
# print(format(id(s),"x"))
# print(is_subset(a, c))


# a = ['red', 'white', 'blue', 'black', 'pink']
# b = ['yellow', 'orange', 'red', 'pink', 'green']
# l = []
# for i in a:
#     if i in b:
#         l.append(i)
# print(l)

# print(set(a) & set(b))
# n=[1,2,4,6,7,8]
# for i in range(0,len(n),2):
#   n[i],n[i+1]=n[i+1],n[i]
# print(n)

# list1=[111,222,333,44]
# l=[]
# x=int(''.join(map(str,list1)))
# print(x)
# print(type(x))

#
# word_list = ['nam', 'how', 'jocy', 'naresh', 'words']
#
# word_list.sort()
# for i in word_list:
#     print(i[0])
#     print(i)


# s1='abc'
# s2='xyz'
# new_s1=s1[:2]+s2[2:]
# new_s2=s2[:2]+s1[2:]
# print(new_s1+' '+new_s2)
#
# l=list((input("enter values:").split(",")))
# l2=" ".join(l)
#
#
# print(l2)
# print(type(l2))
# num = [1, 2, 3, 4, 5]
# print(*num)
# print(type(num))