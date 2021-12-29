new_list=[1,2,3,4,"narendra",2.34,4+5j]
new_list.append(["nani",34])
print(new_list)


new_list=[1,2,3,4,"narendra",2.34,4+5j]
new_list.append(34)
print(new_list)


new_list1=[1,5,"memo","tom",3+5j]
new_list1.clear()
print(new_list1)


new_list2=[1,2,3,"jarry",9+5j]
new_list4=new_list2.copy()
print(new_list4)
print(new_list4.count(9+5j))


new_list7=[1,2,3,4]
new_list6=[23,43,"sheker",4.7,5+7j,{"a":"cat"}]
new_list6.extend(new_list7)
print(new_list6)



sheker=[1,2,3,4,"narendra",8.9999]
print(sheker.index("narendra"))
print(sheker[-1])



list2=[9,8,7,]
list2.insert(1,8)
print(list2)
list2.pop()
print(list2)



list5=[23,45,67,"narendra","tom"]
print(list5.remove("narendra"))



list7=[23,45,67,"narendra","tom"]
list7.remove("narendra")
print(list7)

list7.reverse()
print(list7)

list8=[1,2,3,1,2,3]
list8.sort()
print(list8)
#   tuple methods


tp=(1,2,2,2,2,3,4,5,"narendra",2.4)
print(tp.count(2))
print(tp.index(2))
