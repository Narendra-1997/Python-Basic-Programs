
set3={}
print(type(set3))
set4=set()
print(type(set4))

set1={1,1,2,2,3,3,3,3,4,5,5,6,6,7,7,8,5,4,3,3,44}
print(set1)

def new_func():
    month={'jan','feb','mar','april','may','june','july'}
    month.add('november')
    month.add('desember')
    return month

month = new_func()
print(month)
for i in month:
    print(i)
# new_set1={1,2,3,'s','we','pop'} 
# new_set2={1,2,3,'s','we','pop'} 
# print(new_set1)
# print(new_set2)
# new_set1.add(8)
# new_set2.update(3)
  
  
  
  