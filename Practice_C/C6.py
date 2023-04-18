# input : no input
# output : Print triangle with x&- characters size-10*19
#          (C2.1) use Loop 
#          (C2.2) use Recursive 
# Example : ---------x 
        #   --------xxx 
        #   -------xxxxx 
        #   ------xxxxxxx 
        #   -----xxxxxxxxx 
        #   ----xxxxxxxxxxx 
        #   ---xxxxxxxxxxxxx 
        #   --xxxxxxxxxxxxxxx 
        #   -xxxxxxxxxxxxxxxxx 
        #   xxxxxxxxxxxxxxxxxxx 

for i in range(1,11):
    for j in range(1,(10-i)+1):
        print("-",end="")
    for j in range(1,((2*i)-1)+1):
        print("x",end="")
    print()