#input : enter 10 Integer put it in Array
#output : Print maximum number in array  
#Example : 1 2 3 4 5 6 7 8 9 10 --> 10 

import sys
max =  -sys.maxsize - 1 
x = []
for i in range(10):
	x.append(int(input()))
	if(max<x[i]):
         max = x[i]
print(max)