#input : enter 10 Integer put it in Array
#output : Print 'have' or 'don't have' even numbers
#Example : 1 2 3 4 5 6 7 8 9 10 --> have 
#          3 5 9 7 11 1 15 17 19 21 --> don't have 



count = 0;
x = [int(input()) for i in range(10)]
#print(x)

for i in range(1,10):
    if(x[i]%2 == 0):
        count += 1

    if count > 0:
        print("have")
        break
    elif (count==0  and i==9):
        print("don't have")
