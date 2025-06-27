print("hi")
a  = "amit"
print(a)

import pandas as pd

print(pd.__version__)


# map , lambda, reduce 4

seq = [1, 2, 3, 4, 5, 6, 7, 8]

# find even numbers
even_num = [y for y in seq if y % 2 == 0]
print(even_num)