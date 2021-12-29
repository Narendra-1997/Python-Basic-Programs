"""define a class named American which has a static method called print nationality
hint:--
Use @staticmethod decorator to define class static method

solution:--"""

class America(object):
    @staticmethod
    def printNationality():
        print("america")
        
anAmerican=America() 
anAmerican.printNationality()
America.printNationality()       