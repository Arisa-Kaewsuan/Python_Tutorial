# Tip : create multiple file : use gitBash > run touch D{1..5}.py

# input : Integer(n)
# output : Print the results of 1+2+3+4+..+n
# Example : 10 --> 55 
        #   20 --> 210 
        #   15 --> 120 
        
n = input("Enter number : ")
#print(type(n))
n = int(n)
#print(type(n))
sum = (n*(n+1))/2
print(sum)

