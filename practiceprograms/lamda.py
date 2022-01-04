# l=[1,2,3,4,5,6]
# l1=tuple(map(lambda  i:i*i,l))
# print(l1)



def squer_root(l):
    l1=[]
    for i in l:
        if i%2==0:
            l1.append(i)
    return l1
l=[1,2,3,4,5,6]
print(squer_root(l))

from functools import reduce
l1=reduce(lambda x,y:x+y,[1,2,3,4,5])
print(l1)
    