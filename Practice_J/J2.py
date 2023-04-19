# input: enter 10 Integer put in array
# output: Print Sorted array(Descending)
# Example: 1 2 3 4 5 6 7 8 9 10 - -> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

x = []
for i in range(10):
    x.append(int(input()))
for i in range(10):
    for i in range(10-1):
        if (x[i] < x[i+1]):
            a = x[i]
            x[i] = x[i+1]
            x[i+1] = a
print(x)
