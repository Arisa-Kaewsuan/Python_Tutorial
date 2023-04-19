# input: enter 10 Integer put in array
# output: Print Sorted array(ascending)
# Example: 1 2 3 4 5 6 7 8 9 10 - -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = []
for i in range(10):
    x.append(int(input()))

for j in range(10):
    for i in range(10-1):
        if (x[i] > x[i+1]):
            t = x[i]
            x[i] = x[i+1]
            x[i+1] = t

print(x)
