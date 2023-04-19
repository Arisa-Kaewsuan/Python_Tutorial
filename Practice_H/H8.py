#input : enter 10 Integer put it in Array
#output : Print average of number in array  
#Example : 1 2 3 4 5 6 7 8 9 10 --> 5.5 

	
avg=0.0
a = []
		
for i in range(10):
	a.append(float(input()))
	avg += a[i]
print(avg/len(a))
	