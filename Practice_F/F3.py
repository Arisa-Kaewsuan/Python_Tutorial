# input : enter 1 Integer(n) 
# output :  Print n is a prime number or not 
# Example : 17 --> is a prime number 
        #   15 --> is not a prime number 
        #   19 --> is a prime number 
          
n = input("Enter number : ")
n = int(n)
count = 0

for i in range(1,n+1):
    if(n%i == 0):
        count += 1
if count==2:
    print("is a prime number")
else:
    print("is not a prime number")