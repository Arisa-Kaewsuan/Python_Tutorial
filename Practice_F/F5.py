# input : enter 1 Integer(n) 
# output : Print all prime number < 100 
# Example : 2 3 5 7 11 13 17 ... 97 

for i in range(1,100):
    count = 0
    for j in range(1,i+1):
        if(i%j==0):
            count += 1
    if count == 2:
        print(i)