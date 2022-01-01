"""Please write a program to print the running time of execution of "1+1"
for 100 times.
Hints:
Use timeit() function to measure the running time.
Solution:
from timeit import Timer
t = Timer("for i in range(100):1+1")
print t.timeit()"""
import datetime

before = datetime.datetime.now()
for i in range(100):
    x = 1 + 1
after = datetime.datetime.now()
execution_time = after - before
print(execution_time.microseconds)