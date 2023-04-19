# input: enter 1 Integer(n)
# output: Print result of n != sqrt(2pin)*((n/e) ^ n)
# Example: 100 - -> 9.3248
#          150 - -> 5.7102


import math
n = int(input())
result = 0.0
result = math.sqrt(2*math.pi*n) * math.pow((n/math.e), n)
print(result)
