# input : enter 1 Integer(n) 
# output :  Print how many numbers are there in 1-n that divide n evenly 
# Example : 20 --> 6 
        #   17 --> 2 
        #   21 --> 4 
          
n = input("Enter number : ")
n = int(n)
count = 0

for i in range(1,n+1):
    if(n%i == 0):
        count += 1
print(count)