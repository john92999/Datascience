def m1(a):
    print(a)
    return a

def m1(a=10):
    print(a)
    return a

def m1(*args):
    print(args)
    return args

m1()  # Calls the function with the default argument
m1(15)  # Calls the function with an explicit argument
m1(1, 2, 3)  # Calls the function with multiple arguments

# In Python we can create function through two ways:
# 1. Using def keyword
# 2. Using lambda keyword

m2 = lambda x: x + 10
print(m2(5))

m3 = lambda a: print(a) or a
m4 = m3(20)  
print(m3) 

'''
The above lambda function is same as the following function defined using def keyword:

def m2(a):
    print(a)
    return a

'''

print(m1)
print(m2)

m6 = lambda x, y: x + y
print(m6(20, 30))


prices = [100, 200, 300, 400, 500]
# final prices after gst should be [118, 236, 354, 472, 590]
final_prices = map(lambda x: x + x * 0.18, prices)
print(final_prices)
print(list(final_prices)) 

values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# using filter function to get values less than 50
filtered_values = map(lambda x: x < 50, values)
print(filtered_values)
print(list(filtered_values))

# map functions if we use it instead of filter function then it will return boolean values for each element in the list since it is a aggregate function that means it will do +, -, % and * and it will return True or False for each element in the list based on the condition provided in the lambda function.

filtered_values = filter(lambda x: x < 50, values)
print(filtered_values)
print(list(filtered_values))

# Reduce function will return a single value from the list based on the condition provided in the lambda function.

prices = [100, 200, 300, 400, 500]
from functools import reduce
total = reduce(lambda x, y: x + y, prices)
print(total)