# input : no input
# output : Print triangle with number&- characters
#          (C2.1) use Loop 
#          (C2.2) use Recursive 
# Example : ---------1 
        #   --------121 
        #   -------12321 
        #   ------1234321 
        #   -----123454321 
        #   ----12345654321 
        #   ---1234567654321 
        #   --123456787654321 
        #   -12345678987654321 
        #   12345678910987654321 

for i in range(1,11):
    for j in range(1,(10-i)+1):
        print("-",end="")
    for j in range(1,i+1):
        print(j,end="")
    for x in range(i-1,0,-1):
        print(x,end="")
    print()