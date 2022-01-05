"""7)Write a function to check 
whether the given year is 
a leap year or not."""
def leap_year(y):
    if y%4==0:
        print(y,"Is leap year")
    else:
        print(y,"is not a leap year")
y=int(input("enter year:"))    
leap_year(y)    