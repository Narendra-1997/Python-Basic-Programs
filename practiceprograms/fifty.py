"""Assuming that we have some email addresses in the "username@company 
name .com formate please both user names and company
names are composed og letters omly"""
"""example:
    if the fallowing email address is given as input to programm
   narendra@gmail.com 
   then the output of the programm should be  """
#google
"""in case of input data being supplied to the question it 
  should assumed to be a console """
   

# solution :-- 

import re
emailAdress=input("enter email adress:")
pat2="(\w+)@(\w+)\.(com)"
r2=re.match(pat2,emailAdress)
print(r2.group(2))

   
