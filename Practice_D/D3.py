# input : Integer(n)
# output :  Print the results of 1 + 1/2 + 1/3 + 1/4 +.... + 1/n
# Example : 10 --> 2.9289682539 
        #   5 --> 2.28333333333 
        #   7 --> 2.59285714285 

      
n = input("Enter number : ")
#print(type(n))
n = float(n)
#print(type(n))
fraction = 0
i = 1
while i <= n:
    fraction += 1/i
    i += 1
print(fraction)

