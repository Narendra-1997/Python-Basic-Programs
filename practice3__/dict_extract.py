"""5) Create a new dictionary by
extracting the following 
keys from a given dictionary.
d = {"name": "Kelly",  "age":25,
     "salary": 8000, 
     "city": "New york"}
Keys to extract:
keys = ["name", "salary"]
Output: {'name': 'Kelly',
         'salary': 8000}"""
         
d = {"name": "Kelly",  "age":25,
     "salary": 8000, 
     "city": "New york"}
dit={}
for i,j in d.items():
    if i==("name"or"salary"):
        dit[i]=d[i]
print(dit)        
        
        
    
    
    
    