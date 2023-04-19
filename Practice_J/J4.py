# input: enter 10 Integer put in array
# output: Print Mode of numbers in array & how many duplicates?
# Example: 1 1 2 1 2 4 5 6 7 8 - -> 1 3
# 4 4 4 5 5 6 1 2 3 7 - -> 4 3
# 7 7 7 4 4 1 1 5 8 7 - -> 7 4


a = [int(input()) for i in range(10)]
maxValue = 0
maxCount = 0

for i in range(10):
    count = 0
    for j in range(10):
        if (a[j] == a[i]):
            count += 1
    if (count > maxCount):
        maxCount = count
        maxValue = a[i]
print(maxValue, " ", maxCount)
