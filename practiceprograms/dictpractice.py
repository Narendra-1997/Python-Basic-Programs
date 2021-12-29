person1=[{"name":"narendra","age":23,"hight":5.7},
{"name":"venky","age":27,"hight":5.5},
{"name":"harika","age":15,"hight":5.9},
{"name":"hari","age":16,"hight":5.3},
{"name":"mani","age":18,"hight":5.1}]
def details():
    toller=[]
    smaller=[]
    mediem=[]
    for i in person1:
        if i["hight"]>5.5:
            toller.append(i)
        elif i["hight"]<5.5:
            smaller.append(i)
        else:
            mediem.append(i)
    return toller,smaller,mediem


toller,smaller,mediem=details()


print("toller",toller)
print("smaller",smaller)
print("mediem",mediem)         