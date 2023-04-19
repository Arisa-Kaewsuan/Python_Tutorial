
# input: enter Integer(area of circle)
# output: Print result of circle radius
# Example: 78.539 - -> 4.999974015
#          314.159 - -> 9.9999577667

import math
a = float(input())

r = math.sqrt(a/math.pi)
print(r)
