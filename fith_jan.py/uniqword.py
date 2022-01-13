# f=open("creat.txt","r")
# k=f.read()
# k.lower()
# m=k.split()
# print(m)
# # for i in m :
    # if i==m:       

# for i in m:
#     n=0
#     for k in m:
#         if k == i:
#             n+=1
#     if n==1:
#         print(i)
        
    # print(k.find(i))
    # if k.find(i)==1:
    #     print(i)



    
def vote2(v):
    if v>=18:
        return vote2  
@vote2   
def vote(v): 
    if v>=18:
        print("vis eligible")
    else:
        print("vis not eligible")
vote(23)
   