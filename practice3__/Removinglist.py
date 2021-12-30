"""2)Write a Python program to print a 
specified list after removing the 
0th, 4th and 5th elements.
Input : ['Red', 'Green', 'White', 'Black', 'pink', 'Yellow']
Output : ['Green', 'White', 'Black']"""
new_list=['Red', 'Green', 'White',
          'Black', 'pink', 'Yellow']
# new_list.remove("Red")
# new_list.remove("Black")
# new_list.remove()
new_list = [x for (i,x) in enumerate(new_list) if i not in (0,4,5)]
print(new_list)