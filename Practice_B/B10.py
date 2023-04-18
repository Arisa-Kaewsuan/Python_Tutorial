# input : no input
# output :  Print 1 - 1000 only for number can be divided evenly by 3,5,7 divide into pairs (3,5 /5,7 /7,3).
# Example : 15 21 30 35 42 45 60 63 ... 990

for  i in range(1,1001):
	if((i%3==0 and i%5==0 and i%7==0) ^ ((i%3==0 and i%5==0) or (i%3==0 and i%7==0) or (i%5==0 and i%7==0))):
		print(i);