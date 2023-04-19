#input : enter 10 Integer put it in Array
#output : Print all even numbers in array 
#Example : 1 2 3 4 5 6 7 8 9 10 --> 2 4 6 8 10 
#          11 12 13 14 15 16 17 18 19 20 --> 12 14 16 18 20 

x = [int(input()) for i in range(10)]
for i in range(10):
	if (x[i] % 2 == 0):
		print(x[i],end="  ")
	