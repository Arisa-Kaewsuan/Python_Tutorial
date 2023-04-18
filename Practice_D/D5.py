# input : Integer(n)
# output :  Print the results of square root(6*(1 + 1/2^2 + 1/3^2 + 1/4^2 +.... + 1/n^2)) 
            # ^ = power     
# Example : 10000 --> 3.141 
        #   100 --> 3.132 
        #   50 --> 3.123 

import math
      
polinomial = 0
sqrt = 0
n = input("Enter number : ")
#print(type(n))
n = int(n)
#print(type(n))
i = 1
while i <= n:
    polinomial += 1/math.pow(i,2)
    i += 1
sqrt = math.sqrt(6*polinomial)
print(sqrt)

