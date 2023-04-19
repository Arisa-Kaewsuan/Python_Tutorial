#input : enter 10 Integer put it in Array
#output : Print numbers in array (Sort by invert enter) 
#Example : 1 2 3 4 5 6 7 8 9 10 --> 10 9 8 7 6 5 4 3 2 1 
#          3 5 9 7 11 1 15 17 19 21 --> 21 19 17 15 1 11 7 9 5 3 

x = [int(input()) for i in range(10)]
print(x[::-1])
 