"""12)Print multiplication 
table of a given number"""

m = (int(input("Enter the value")))

for i in range(1, 101):
    print(m, "*", i, "=", m * i)
