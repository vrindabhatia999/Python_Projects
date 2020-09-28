import csv
from collections import Counter

file=open("test.txt",'r')

dict={}

for line in file:
    x=line.split(",")
    a=x[0]
    b=x[1]
    dict[a]=b


print(dict)
print(dict['aasha'])