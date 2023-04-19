# input : enter 10 Integer put it in Array
# output : Print minimum number in array
# Example : 1 2 3 4 5 6 7 8 9 10 --> 1#


import sys
min = sys.maxsize
x = []
for i in range(10):
    x.append(int(input()))
    if (min > x[i]):
        min = x[i]
print(min)
