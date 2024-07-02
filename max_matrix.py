import numpy as np
input = [['Paras',90],['Rohit',80],['Sita',70],['Gita',60]]
output = max(input, key = lambda x:x[1])
print("input : ",input)
print("output : ",output)