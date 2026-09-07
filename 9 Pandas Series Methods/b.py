import pandas as pd

a = [10,20,30,40,50,60,70,80,90,100]
s = pd.Series(a)

# To see only top 5 values we use head method
# The head method by default it will only show 5 
print(s.head())

# To see last 5 we use tail method
print(s.tail())
