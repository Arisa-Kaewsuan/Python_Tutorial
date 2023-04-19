#input : enter 10 Integer put it in Array
#output : Print multiplication of number in array  
#Example : 1 2 3 4 5 6 7 8 9 10 --> 3628800 


multiply = 1
x = []
for i in range(10):
	x.append(int(input()))
	multiply *= x[i]
print(multiply)

















