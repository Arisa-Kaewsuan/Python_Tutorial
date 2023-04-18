# input : Integer(n)
# output :  Print the results of 1*2*3*4*..*n
# Example : 10 --> 3628800 
        #   5 --> 120 
        #   7 --> 5040 


        
n = input("Enter number : ")
#print(type(n))
n = int(n)
#print(type(n))
mul = 1
for i in range(1,n+1):
    mul *= i
print(mul)

