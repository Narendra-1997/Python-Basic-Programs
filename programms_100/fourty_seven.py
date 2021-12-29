"""Write afunction to compute 5/0 and use try/except to catch the exceptions
"""

# hint:--

# use try/except to catch Exception

def throws():
    return 5/0
try:
    throws()
except ZeroDivisionError:
    print("division by zero")
except Exception.err:
    print("caught an exception")
finally:
    print("in finally block for cleaning")
    
        
        

    