"""9)Write a function to pass
keyword args and update the
dictionary"""
def dict(**kwargs):
    print(locals())
dict(a="karthik",b="nani")    
    