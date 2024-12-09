# File Handling
import os

file = open("data.txt","r")

# data = file.read()
data = file.readlines()
# data2 = file.readline()
# data1 = file.readline()
print(data[-2])
# print(data1)
# print(data2)
# for i in data:
#     print(i,end='')
