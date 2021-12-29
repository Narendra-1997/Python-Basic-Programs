str="my name is narendra"
l=[]
m=str.split()
for i in range(1,len(m)+1):
    if i%2==0:
        l.append(m[i-1][::-1])
    else:
        l.append(m[i-1])
print(l)
print("  ".join(l))