# input : enter 1 Integer(n) 
# output : Print all numbers are there in 1-n that divide n evenly 
# Example : 20 --> 1 2 4 5 10 20 
        #   17 --> 1 17 
        #   21 --> 1 3 7 21 
        
n = input("Enter number : ")
n = int(n)

for i in range(1,n+1):
    if(n%i == 0):
        print(i)