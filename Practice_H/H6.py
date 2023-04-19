#input : enter 10 Integer put it in Array
#output : Print sum of number in array  
#Example : 1 2 3 4 5 6 7 8 9 10 --> 55 
#          11 12 13 14 15 16 17 18 19 20 --> 155 

sum = 0
x = []
for i in range(10):
	x.append(int(input())) 
	sum += x[i]
print(sum)
