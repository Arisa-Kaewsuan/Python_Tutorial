
# input: enter 3 Integer
# output: Print sum & avg#
# Example: 7 11 32 - -> 50  16.66
#          5 10 15 - -> 30  10.0
#          7 3  9 - -> 19  6.33

a = int(input())
b = int(input())
c = int(input())

sum = a+b+c
avg = sum/3.0

print(sum, end="  ")
print(avg, end="  ")
