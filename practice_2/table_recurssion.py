"""Print multiplication table of 12 using recursion."""
def mul_table(f,s):
    if (s>10):
        return
    print(f,"*",s,"=",f*s)
    return mul_table(f,s+1)

f=12
mul_table(f,1)
