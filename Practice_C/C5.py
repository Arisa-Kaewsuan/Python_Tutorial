# input : no input
# output : Print triangle with x&- characters size-10*10
#          (C2.1) use Loop 
#          (C2.2) use Recursive 
# Example : ---------x 
        #   --------xx 
        #   -------xxx 
        #   ------xxxx 
        #   -----xxxxx 
        #   ----xxxxxx 
        #   ---xxxxxxx 
        #   --xxxxxxxx 
        #   -xxxxxxxxx 
        #   xxxxxxxxxx 

for i in range(1,11):
    for j in range(1,(10-i)+1):
        print("-",end="")
    for j in range(1,i+1):
        print("x",end="")
    print()