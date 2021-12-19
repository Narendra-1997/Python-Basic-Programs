class PrintingNames:
    def __init__(self):
        self.name = None
        self.age=None
    
    def take_input(self):
        self.name=input("enter name: ")
        self.age=int(input("enter age: "))
        
    def printing_details(self):
        return self.name, self.age
    
obj = PrintingNames()
obj.take_input()
name, age = obj.printing_details()
print("Name: ",name)
print("Age: ",age)