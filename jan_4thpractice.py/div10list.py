"""5)Write a function that takes a list as input 
and returns a new list by multiplying
all the elements from the given list with 10."""


def div(l):
    l2 = []
    for i in l:
        l2.append(i * 10)
    print(l2)


l = list(int(i) for i in input("enter value::").split(","))
div(l)
