# input : Integer(n)
# output :  Print the results of 1 + 1/2^2 + 1/3^2 + 1/4^2 +.... + 1/n^2  */
            # ^ = power     
# Example : 10 --> 1.54976 
        #   15 --> 1.58044 
        #   6 --> 1.491388889 


import math
      
n = input("Enter number : ")
#print(type(n))
n = int(n)
#print(type(n))
polinomial = 0
i = 1
while i <= n:
    polinomial += 1/math.pow(i,2)
    i += 1
print(polinomial)

