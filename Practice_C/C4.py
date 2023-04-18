# input : no input
# output : Print inverted triangle with x characters size-10*10
#          (C2.1) use Loop 
#          (C2.2) use Recursive 
# Example : xxxxxxxxxx 
#           xxxxxxxxx 
#           xxxxxxxx 
#           xxxxxxx 
#           xxxxxx 
#           xxxxx 
#           xxxx 
#           xxx 
#           xx 
#           x 

for i in range(10,0,-1):
    for j in range(1,i+1):
        print("x",end="")
    print()