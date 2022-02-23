# class PrintingNames:
#     def __init__(self):
#         self.name = None
#         self.age=None
#
#     def take_input(self):
#         self.name=input("enter name: ")
#         self.age=int(input("enter age: "))
#
#     def printing_details(self):
#         return self.name, self.age
#
# obj = PrintingNames()
# obj.take_input()
# name, age = obj.printing_details()
# print("Name: ",name)
# print("Age: ",age)

# class employee:
#     name = 'nani'
#     id = 12

#     def disply(f):
#         print(f.name,f. id)


# c1 = employee()
# c1.disply()
# single  inheritence

# class animal:
#     def speak(self):
#         print("animal speak")
# class dog(animal):
#     def bark(self):
#         print("dog bark")
# d=animal()
# d.bark()
# d.speak()

# multilevel inheritence

# class animal:
#     def speak(self):
#         print("animal speak")
# class dog(animal):
#     def bark(self):
#         print("dog bark")
# class smalldog(dog):
#     def talk(self):
#         print("dog sneez")


# d=dog()
# d.bark()
# d.speak()
# d.talk()                  


# class calc1:
#     def sum(self, a, b):
#         return a + b


# class calc2:
#     def sub(self, a, b):
#         return a - b
#
#
# class devide(calc1, calc2):
#     def div(self, a, b):
#         return a / b
#
#
# op = devide()
# print(op.sum(4, 6))
# print(op.sub(8,10))
# print(op.div(12,14))


# mro
# class A:
#     def su(self):
#         print("in class A")
#
#
# class B(A):
#     def sum(self):
#         print("in class B")
#
#
# class C(B):
#     def su1(self):
#         print("in class c")
#
#
# class D(C):
#     pass
#
#
# r = D()
# r.su()
# r.sum()
# r.su1()


# class employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def display(self):
#         print("ID: %d\n Name:%s"%(self.id,self.name))
# emp1=employee("nani",12)
# emp2=employee("nani1",13)
# emp1.display()
# emp2.display()
#
#
#
# class student:
#     count=0
#     def __init__(self):
#         student.count=student.count+1
# s1=student()
# s2=student()
# s3=student()
# print(student.count)


# class student:
#     def __init__(self):
#         pass
#     def Show(self,name):
#         print("hello",name)
# s=student()
# s.Show("nani")

# class sum:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
# Ans=sum(12,4)
# print(Ans.add())


# factorial in class

# class name:
#     def fact(self,num):
#         l=[]
#         n=1
#         if num==1:
#             return num
#         else:
#             for i in range(1,num+1):
#                 n=n*i
#                 l.append(n)
#             print(l)
#
# num=int(input("enter n value;-"))
# res=name()
# res.fact(num)



# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# s=Student("jessi",2021,7)
# print(getattr(s,"name"))
# setattr(s,"age",6)
# print(getattr(s,"age"))
# print(hasattr(s,'id'))
#
# print(s.id)


# Abstract method



# from abc import ABC , abstractmethod
# class claas1(ABC):
#       @abstractmethod
#       def clsproo(self):
#           pass
# class cla2(claas1):
#       def clsproo(self):
#           print("noting")
#
# class clsp2(cla2):
#       def work(self):
#           print("somthing")
# c=cla2()
# pro=clsp2
# pro.work(c)


class encap:
    def __init__(self):
        self.__a="narendra"
        self.b="jaswik"
    def test(self):
        print(self.__a+self.b)


res=encap()
print(res._mani__a)

 