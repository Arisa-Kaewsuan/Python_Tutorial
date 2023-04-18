# input : no input
# output : Print 1 - 100 only for number can be divided evenly by 3 or 5 (include 3 and 5).
# Example : 3 5 6 9 10 12 (have 15) 18 20 21 24 25 ... 100

for i in range(1,101):
	if i%3 == 0 or i%5 == 0:
	    print(i)