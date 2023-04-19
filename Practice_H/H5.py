#input : enter 10 Integer put it in Array
#output : Print how many even numbers in array?  
#Example : 1 2 3 4 5 6 7 8 9 10 --> 5 
#          11 12 13 14 15 16 17 18 19 20 --> 5 

x = [10]
count = 0
for i in range(10):
    x.append(int(input()))
    if (x[i]%2 == 0):
        count += 1
print(count)