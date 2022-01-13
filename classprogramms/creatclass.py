# class person:
#     hight=5.3
#     wight=60
#     def human(self):
#         print(self.hight,self.wight)
# narendra=person()
# narendra.human() 
# class Arthametic:
#     def __init__(self,name):
#         self.name=name
#     def say_hi(self):
#         print("my name is :",self.name)
# p=Arthametic("Narendra")
# p.say_hi()        

class Arthemetic:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
a=int(input("enter a value:;"))
b=int(input("enter b avlue:;"))    
res=Arthemetic(a,b)
print(res.sum()) 
print(res.sub()) 
print(res.mul()) 
        
        
        