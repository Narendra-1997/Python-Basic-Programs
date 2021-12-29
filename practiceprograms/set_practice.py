"""python program to demonstrate set """
myset=set(["a","b","c","d"])
print(myset)

# "adding elements to set"

myset.add("u")
print(myset)


"""deference between normal set and frozen set"""

normal=set([1,2,3,4])
print(normal)

frozen_set=frozenset([2,5,67,8,4,])
print(frozen_set)

people={"narendra","mahi","jaswik"}
people.add("sai")
print(end=" ")
for i in range(1,5):
    people.add(i)
print(people)    
    
