#with a given intigral number n, genarate a dictionary that contains(i, i*i)
#such that is an integral number between 1and n(both included). and program should print the dictionary
#suppose the following inout is supplied to the program:8
#then the out put should be :
#(1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64)
#consider use dict()
n=int(input("input a number"))
d=dict()

for i in range(1,n+1):
      d[i]=i*i

print(d)

