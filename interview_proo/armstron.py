num = int(input("enter value:-"))
s = 0
t = str(num)
count=0
while count < len(t):
    s=s+(int(t[count])**len(t))
    count+=1

#     c = t % 10
#     s = s + c ** 3
#     t = t // 10
# for i in t:
#     s = s + int(i) ** len(t)
if num == s:
    print("it is a armstromg number")
else:
    print("it is not armstrong number")
