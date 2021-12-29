""" define a class ,which have a class parameter and have a same 
instance parameter


Define a instance parameter, need abdd it in __init__method you can init a object with counstruct
or set the value later"""

class person:
    name="person"
    def __init__(self,name=None):
        self.name= "narendra","venky"
        
narendra=person()
name="narendra"
print("%s name is %s" % (person.name,narendra.name))


venky=person()
name="VENKY"
print("%s name is %s" % (person.name , venky.name))


        
        
    
