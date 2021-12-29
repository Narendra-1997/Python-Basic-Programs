"""assuming that we have some email addresses in the 
"username@companyname .com" formate, please write program 
to print the user name of a given email address .
both user name and company names are composed of letters only"""
"""example:
if the folloeing email address is given as input to the program:
    narendra@gmail.com """
"""then the output of the proramm should be :
    narendra"""
"""in case of input data being supplied to the question, it should  be assumed to be a console input"""    
    # hint:--
    # use \w to match the latters
    
import re
emailadress=input("enter email adress::")
part2="(\w+)@((\w+\.)+(com))"
r2=re.match(part2,emailadress)
print(r2.group(1))





    
    
           
    