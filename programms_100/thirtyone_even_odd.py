"""define a function that can accept an integer number as 
input and print that"it is an even number"if the number is even,
other wise print "it is an odd number"""
# hint:__

# use % operator to chech if the number is even or odd

def evenodd(n):
    if n%2==0:
        print("it is an even number")
    else:
        print("it is an odd number")
evenodd(67)        