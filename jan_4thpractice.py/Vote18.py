"""Write a function to tell user if he/she is able to vote or not.
( Consider minimum age of voting to be 18. )"""



def vote(v):
    if v>=18:
        print("v is eligble for vote")
    # elif v<=18:
    else:
        print("v is not eligble to vote")
v=int(input("enter age of the person:"))
vote(v)
        