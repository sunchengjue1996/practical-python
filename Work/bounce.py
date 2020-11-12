# bounce.py
#
# Exercise 1.5
import math
h = 100
bounce = 0
for i in range(10):
    h = h * (3/5)
    bounce = bounce + 1 
    print("第%s次，弹起第高度是%s" % (bounce,h))

# print(100 * (3/5))