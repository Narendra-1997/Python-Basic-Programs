# class human:   # class creation
#     colour="black"   # attributse of class
#     hight=5.7
#     def run(self): #defining the function1
#         print("RUNNING,.,.,.,.,")
#     def walk(self): #defining the function 2
#         print("WALKING.,.,.,.,")  
# narendra=human() # creating the object for the class
# print(narendra.colour,narendra.hight)  # calling the class
# narendra.run() #calling functions
# narendra.walk() 


#############*******INHERITENCE********###############

class parent():
    father="narendra"
    mother="mani"
    def baseclass(self):
        print("base class")
class child(parent):
    child1="jaswik"
    child2="soon"
    def derivedclass(self):
        print("DERIVED CLASS")
children=child()
print(children.father,children.mother)
children.baseclass()
children.derivedclass()
print(children.child1,children.child2)               
 

