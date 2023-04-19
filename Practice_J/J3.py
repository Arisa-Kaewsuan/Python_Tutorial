# input: enter 10 Integer put in array
# output: Print Median of numbers in array
# Example: 1 2 3 4 5 6 7 8 9 10 - -> 5.5
# 5 4 6 7 11 10 15 14 13 17 - -> 10.5
# 12 20 5 7 6 3 15 11 30 9 - -> 10.0


n = []

for i in range(10):
    n.append(int(input()))
for i in range(10):
    for j in range(10-1):
        if (n[j] > n[j+1]):
            t = n[j+1]
            n[j+1] = n[j]
            n[j] = t

a = n[int((len(n)/2)-1)]
b = n[int(len(n)/2)]
print((a + b) / 2)
