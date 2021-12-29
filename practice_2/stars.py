"""Write a function called show_stars(rows). If rows is 5, it should print the following:
*
**
***
****
*****"""

def Show_stars(rows):
    for i in range(0,rows):
        for j in range(i+1):
            print("*",end=" ")
        print()
rows=int(input("enter value;--"))
Show_stars(rows)        