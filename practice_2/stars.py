"""Write a function called show_stars(rows). If rows is 5, it should print the following:
*
**
***
****
*****"""


def Show_stars(rows):
    for i in range(0, rows):
        for j in range(i + 1):
            print(rows)
        print()
# def Show_stars(rows):
#     for i in range(1, rows):
#         print("* "*i)
#     for j in range(1, rows):
#         print(' '*((rows+2)-j+1),"* " * j)
#         # print()

rows = int(input("enter value;--"))
Show_stars(rows)
