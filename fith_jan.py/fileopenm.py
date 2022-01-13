"""5)Write a Python program to 
demonstrate different modes 
of a file open method."""


# employee=open("binary64.txt","w")
# print("file created")

# employee=open("nani.txt","r")
# print(employee.read())#we can get the information while the file is in readmode
# employee.close()

# employee=open("nani.txt","a")
# print(employee.write("iam narendra"))
# employee.close()#it append the information

# file=open("nani.txt","w")
# print(file.write("file handling"))
# file.close()#it override the exixting information


# file2=open("creat.txt","x")
# print(file2,"file opend")
# file2.close()


# file=open("creat.txt","r")
# print(file.readline())
# file.close()


# file=open("creat.txt","r")
# print(file.readlines())
# file.close()


# file=open("creat.txt","r")
# print(file.readline(8))
# file.close()

# file=open("nani2.txt","w")
# print(file.write("iam marrid"))
# file.close()

# file=open("nani2.txt","w")
# print(file.read())
# file.close()

# file=open("binary64.txt","rb")
# print(file.read())
# file.close()

# file=open("creat.txt","r")
# for i in file:
#     print(i)



# from _typeshed import SupportsLenAndGetItem
import json

file=open("dict.json","r")
k=json.load(file)
# print(k)




for i in k:
    if i["name"]=="naredra babu":
        i["name"]="narendra"
print(k)
    
file=open("dict.json","w")
json.dump(k,file)    
file.close()

    
    
