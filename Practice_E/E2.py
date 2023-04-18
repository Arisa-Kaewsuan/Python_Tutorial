# input : enter 2 integer (a,b) 
# output : Print the Greatest Common Factor of 2 numbers
# Example : 12 32 --> 4 
          # 25 10 --> 5 
          # 100 60 --> 20 
        
a = input("Enter number : ")
a = int(a)
b = input("Enter number : ")
b = int(b)
max = b if True else a

for i in range(max,-1,-1):
    if((a%i == 0)and(b%i == 0)):
        print(i)
        break