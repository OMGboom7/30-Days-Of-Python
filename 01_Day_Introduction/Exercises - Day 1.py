# Check the python version you are using
import sys

python_version = sys.version
print('Python版本为：' + python_version)

# Find an Euclidian distance between (2, 3) and (10, 8)
import math

a = (2, 3)
b = (10, 8)
distance = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
print(distance)