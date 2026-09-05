'''
We can create Series in different ways
1. Empty Series
2. From a list
3. From a array
4. By accessing single column from data frame
'''

import pandas as pd

s = pd.Series()  # Empty Series
print(s)
print(type(s))

print()
print("------------------------------------------------")
print()

a = [10, 20, 30, 40, 50]
s1 = pd.Series(a) # Series from a list
print(s1)
# Data type int64

print()
print("------------------------------------------------")
print()

b=[10.2, 56.3, 45.6, 78.9, 90.1]
s2 = pd.Series(b)
print(s2)
# Data type float64

print()
print("------------------------------------------------")
print()

c = ["John", "Alice", "Bob", "Charlie", "David"]
s3 = pd.Series(c)
print(s3)
# Data type object and not string
# The object notation is used for string data type in pandas Series. The reason is that pandas Series can hold any data type, not just strings. Therefore, it uses the object notation to represent string data type.


print()
print("------------------------------------------------")
print()

d = ["John", 10.2, 10 + 20j, True, None, {"Name": "John", "Age": 28}, (1, 2, 3), [1, 2, 3], {1, 2, 3}]
s4 = pd.Series(d) 
print(s4)
# Data type object