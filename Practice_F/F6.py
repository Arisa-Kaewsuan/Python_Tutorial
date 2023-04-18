# input : enter 1 Integer(n) 
# output : Print all prime number (first 100 numbers) 
# Example : 2 3 5 7 11 13 17 ... 541 

num = 0
i = 1 

while i>0:
    count = 0
    for j in range(1,i+1):
        if(i%j==0):
            count += 1
    if count == 2:
        print(i)
        num += 1
    elif num == 100:
        break
    i += 1