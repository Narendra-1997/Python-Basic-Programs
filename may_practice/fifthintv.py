# def v_func(*var):
#     for i in var:
#         print(i, end=",")
#
#
# v_func(12)
# v_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 6)


# def unique(num):
#     if len(num) == len(set(num)):
#         return True
#     else:
#         return False
#
#
# print(unique([1, 2, 3, 4, 5]))
# print(unique([1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))


# def pairs(arr, N):
#     set1 = set()
#     for i in range(0, len(arr)):
#         # print(i)
#         val = N - arr[i]
#         # set1.add(arr[i])
#         if (val in set1):
#             print(arr[i], val)
#         set1.add(arr[i])
#
#
# arr = [1, 2, 3, 4, 5, 6, 7]
# N = 6
# pairs(arr, N)


# def sum(n1, n2):
#     while n2 != 0:
#         res = n1 & n2
#         n1 = n1 ^ n2
#         n2 = res << 1
#     return n1
#
#
# print(sum(21, 10))


# l = [1, 2, 2, 2, 5, 6, 7, 8, 9]
# k = 6
# set1 = set()
# for i in l:
#     for j in l:
#         if i + j == k:
#             print(i, j)

# def reverseInParenthases(inputString):
#     l = inputString
#     for i in range(len(l)):
#         if l[i] == '(':
#             a = i
#         if l[i] == ')':
#             z = i
#             return reverseInParenthases(l[:a] + (l[a + 1:z][::-1] + l[z + 1:]))
#     return l
#
#
# print(reverseInParenthases("(Narendra)"))

#
# l = ["banana", "apple", "krishna", "ramu"]
# l2 = []
# for i in l:
#     l2.append(i[::-1])
# print(l2)

#
# l = ["banana", "apple", "krishna", "ramu"]
#
# l3 = "n"
# for i in l:
#     if l3 in i:
#         print(i)


# import time
#
# l = [1, 2, 3, 4]
# t = (4, 5, 6, 7)
# s = time.time()
# for i in l:
#     print(i, end=" ")
#     e = time.time()
# print(" list executing time", e - s)
# s1 = time.time()
# for i in t:
#     print(i, end=" ")
#     e1 = time.time()
# print(" tuple executing time", e1 - s1)
#
#
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# n = int(input("enter value::"))
# if n <= 0:
#     print("enter positive number")
# else:
#     for i in range(n+1):
#         print(fib(i))

# s1 = "123456"
# s2 = "123456"


#
# def anagram(s1, s2):
#     a = list(s1)
#     a.sort()
#     b = list(s2)
#     b.sort()
#     if (a == b):
#         return True
#     else:
#         return False
# print(anagram(s1,s2))

#
# def inc_sequence(sequence):
#     dropped = False
#     last = prev = min(sequence) - 1
#     for ele in sequence:
#         if ele <= last:
#             if dropped:
#                 return False
#             else:
#                 dropped = True
#             if ele <= prev:
#                 prev = last
#             elif ele >= prev:
#                 prev = last = ele
#             else:
#                 prev, last = last, ele
#             return True
#
#
# print(inc_sequence([1,2,3,2,1]))


# def narendra(l):
#     for i in l:
#         if i % 2 == 0:
#             yield i
#
#
# x = narendra([1, 2, 3, 4, 5, 6, 7, 8, 9])
# for val in x:
#     print(val)
# monk.py
# def countOccurrences(arr, n, x):
#     res = 0
#     for i in range(n):
#         if x == arr[i]:
#             res += 1
#     return res
#
#
# # Driver code
# arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
# n = len(arr)
# x = 2
# # print(countOccurrences(arr, n, x))
# def countOccurrences(arr, n, x):


# arr = [0,1,8,1,7,1,9,1,2,2,6,2,6,0,1,2,3,5,1]
# l=[]
# c={}
# for i in arr:
#     if i in c:
#         c[i]+=1
#     else:
#         c[i]=1
# m=sorted(c.items(),key=lambda x:x[-1],reverse=True)
# l3=[]
# for j in m:
#     l1=(str(j[0])*j[-1])
#     l3.append(l1)
# print(l3)


# l = ["fli", "flnam", "fltl"]
#
#
# # l.sort()
# # print(l)
#
# # l2 = ["dough", "doughnut", "dought"]
#
#
# def longestCommonPrefix(l):
#     size = len(l)
#     if size == 0:
#         return "nothing"
#     if size == 1:
#         return l[0]
#     l.sort()
#     print(l)
#     name = max(len(l[0]), len(l[size-1]))
#     print(name)
#
#     i = 0
#     while i < name and l[0][i] == l[size - 1][i]:
#         i += 1
#         print(i)
#     pre = l[0][0:i]
#     return pre
#
#
# print(longestCommonPrefix(l))


# l=[0,1,8,1,7,1,9,1,2,2,6,2,6,0,1,2,3,5,1]
# l1=[]
# d={}
# for i in l:
#     if i in d:
#
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# a=list(zip(d.keys(),d.values()))
# print(a)
# for i in range(len(a)-1,0,-1):
# # for i in range(1,len(a)):
#     print(i)
#     for j in range(i):
#         if a[j+1][1]>a[j][1]:
#             a[j+1],a[j]=a[j],a[j+1]
#
# for (i,j) in a:
#     for k in range(1,j+1):
#         l1.append(i)
# print(l1)

# l = [1, 2, 3, 4, 5, 6, 7, 8]
# # print([l[7],l[6]])
# print(l[-1:-3:-1])
# l2 = {s:i ** 2 if i % 2 == 0 else i ** 3 for s, i in l}
# print(l2)


# from datetime import datetime
# s='25-12-2021'
# datetime_object = datetime.strptime(s, "%d-%m-%Y")
# new = datetime_object.strftime("%a,%b,%Y")
# new1 = datetime_object.strftime("%A,%y,%B")
# print(new1,new)


# l=[int(num) for num in (input("enter values:"))]
# print(l)
# l1=[x**2 if x%2==0 else x**3 for x in l]
# print(l1)


# import datetime
# x=datetime.datetime.now()
# print(x)

#
# import datetime
# x=datetime.datetime.now()
# print(type(x))
# x2=(x.strftime("%a"))
# print(type(x2))
# print(x.strftime("%A"))
# print(x.strftime("%w"))
# print(x.strftime("%d"))
# print(x.strftime("%b"))
# print(x.strftime("%B"))
# print(x.strftime("%m"))
# print(x.strftime("%y"))
# print(x.strftime("%Y"))
# print(x.strftime("%H"))
# print(x.strftime("%I"))
# print(x.strftime("%p"))
# print(x.strftime("%M"))
# print(x.strftime("%S"))
# print(x.strftime("%f"))
# print(x.strftime("%z"))
# print(x.strftime("%Z"))
# print(x.strftime("%j"))
# print(x.strftime("%U"))
# print(x.strftime("%W"))
# print(x.strftime("%c"))
# print(x.strftime("%C"))
# print(x.strftime("%X"))
# print(x.strftime("%x"))
# print(x.strftime("%%"))
# print(x.strftime("%G"))
# print(x.strftime("%u"))
# print(x.strftime("%V"))
# print(x.strftime("%D"))

# from datetime import datetime
# x=datetime.now()
# print(x.strftime("%B"))
# from datetime import datetime
# t=datetime(2022,6,29)
# print(t.strftime("%A"))
# import time
# print(time.time())
# import datetime
# ticks = 52707330000
# converted_ticks = datetime.datetime.now() + datetime.timedelta(microseconds = ticks/10)
# print(converted_ticks)
# import time
# x=time.localtime(time.time())
# print(x)
#
# import time
# l=time.asctime(time.localtime(time.time()))
# l2=time.asctime()
# print(l2)
# print(l)
# import time
# for i in range(1,3):
#     print(i)
#     time.sleep(10)

# import datetime
# print(datetime.datetime.now())
# l=(datetime.datetime(1997,9,8,4,25,50))
# print(l.strftime("%m"))

# from datetime import datetime as dt
# if dt(dt.now().year,dt.now().month,dt.now().day,9)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
#     print("working hours")
# else:
#     print("fun hours")
#
#
# import calendar
#
# cal=calendar.calendar(1)
# print(cal)
#
# cal2=calendar.prcal(1997)
# print(cal2)
# from datetime import datetime, date
#
#
# def age_calc(Dob):
#     today = datetime.now()
#     age = today.year - Dob.year - ((today.month, today.day) <
#                                    (Dob.month, Dob.day))
#     age6 = today - Dob
#
#     print(age6)
#     return age
#

# Dob=datetime(int(input("enter DOB")))
# here i cannot be able to enter the date in date formate

# print(age_calc(datetime(1996, 1, 4)))
import pdb
def addition(a,b):
    ans=a+b
    return ans
# pdb.set_trace()
a=10
b=10
sum=addition(a,b)
pdb.set_trace()
print(sum)
pdb.set_trace()