# input : no input
# output : Print triangle with number&- characters
#          (C2.1) use Loop 
#          (C2.2) use Recursive 
# Example : ---------1 
        #   --------123 
        #   -------54321 
        #   ------1234567 
        #   -----987654321 
        #   ----1234567891011 
        #   ---13121110987654321 
        #   --123456789101112131415 
        #   -1716151413121110987654321 
        #   12345678910111213141516171819 

for i in range(1,11):
    for j in range(1,(10-i)+1):
        print("-",end="")
    if(i%2 == 0):
        for j in range(1,((2*i)-1)+1):
            print(j,end="")
    else:
        for k in range((2*i)-1,0,-1):
            print(k,end="")
    print()