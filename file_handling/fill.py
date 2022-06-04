# with open("learn.txt","r")as nani:
#     info=nani.read()
#     print(info)
#
# with open("learn.txt",'w')as n:
#     res=n.write("narendra is not good boy")
#     print(res)

#
# with open('nani.txt','r') as file:
#     print(file.readlines())
# #
# file = open('nani.txt', 'w')
# print(file.read(10))
# print(file.read(6))
#  print(file.read(10))

# list1 = []
# for i in range(3):
#     name = input("enter employee name:")
#     list1.append(name + '\n')
# file.writelines(list1)
# file.close()
# print("data saved")


file1 = open('learn.txt', 'r')
print(file1.readline())
file2 = open('nani3.txt', 'a')

str1 =''
while str1:
    str1 = file1.readline()
    file2.write(str1)



file1.close()
file2.close()
print('its yes')
# s = open('nani.txt', 'r')
# s1 = s.readlines()
# print(s1)
