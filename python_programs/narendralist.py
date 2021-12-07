new_list1=['narendra',143,'manemma']
new_list2=[1,2,0,23,22,24]
print(type(new_list1))
print(type(new_list2))
print(new_list2[1:6:])
print(new_list2[1:6:2])
print(new_list2==new_list1)
for i in new_list1:
    print(i)
    stu=['narendrs',143,'AP']
    dep1=['BSC',10]
    dep2=['com',3]
    STU_BSC=[10,'mr.venky']
    STU_COM=[3,'mr.mani']
    print('printing student data')
    print('Name  :   %s,   ID:  %d, country:  %s'%(stu[0],stu[1],stu[2]))
    print('printing department')
    print('department 1:\nName:%s, ID: %d\ndep++artment 2:\nName: %s,ID:%s'%(dep1[0],dep2[1],dep2[0],dep2[1]))
print('STU details')
print('BSC  STU  Name:%s  id:    %d'%(STU_BSC[1],STU_COM[0]))
print('com  STU  name:  %s, id:%d'%(STU_BSC[1],STU_COM[0]))
v=[]
n=int(input("Enter the number of elements inthe list:"))
for i in range(0,n):
    v.append(input(" Enter the items:"))
    print('printing the list items')
    for i in v:
        print(i,end="  ")
m='manemma'
p='narendra'
print(m+p)
