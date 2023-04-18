# input : enter 2 integer (a,b) 
# output : Print the least common multiple of 2 numbers
# Example : 12 24 --> 24 
        #   18 32 --> 288
        #   10 15 --> 30 
        
a = input("Enter number : ")
a = int(a)
b = input("Enter number : ")
b = int(b)
i = 2

while True:
    if((i%a == 0)and(i%b == 0)):
        print(i)
        break
    i += 1