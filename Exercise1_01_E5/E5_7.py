
# input: enter 3 decimal
# output: Print sum & avg
# Example: 3.0  7.0  1.5 - -> 11.5  3.833
#          5.2  1    6 - -> 12.2  4.066
#          7    5    2.5 - -> 14.5  4.833

a = float(input())
b = float(input())
c = float(input())

sum = a+b+c
avg = sum/3

print(sum, end="  ")
print(avg, end="  ")
