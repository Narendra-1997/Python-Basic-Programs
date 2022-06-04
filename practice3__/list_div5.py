"""13)Given a list iterate it and display numbers
that are divisible by 5 and if you find a number 
greater than 150 stop the loop iteration
Ex: Input: list1 = [12, 15, 32, 42, 55,
                    75, 122, 132, 150, 180, 200]
Output: 15
55
75
150"""

list1 = [12, 15, 32, 42, 55,
         75, 122, 132, 150, 180, 200]
for i in list1:
    if i <= 150:
        if i % 5 == 0:
            print(i)
