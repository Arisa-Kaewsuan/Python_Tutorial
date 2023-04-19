
# input: enter 6 Integer(a1, b1, c1, a2, b2, c2) sequently
# output: find x and y from
#         a1X+b1Y = C1
#         a2X+B2Y = C2

# Example: 2 1 10 - 1 2 0 - -> 4.0  2.0
#          1 2 3   4 5 6 - -> -1.0 2.0

a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

x, y = 0.0, 0.0
ex1, ex2 = 0, 0
x1, x2 = 0, 0
nA1, nB1, nC1, nA2, nB2, nC2 = 0, 0, 0, 0, 0, 0
A, B, C = 0, 0, 0

if ((a1 > 0) and (a2 > 0)):
    x1 = a1
    x2 = a2
else:
    x1 = b1
    x2 = b2
if ((a1 == a2) or (b1 == b2)):
    A = a1-a2
    B = b1-b2
    C = c1-c2

    if (A == 0):
        y = C/B
        x = (c1-(b1*y))
    else:
        x = C/A
        y = (c1-(a1*x)) / b1
else:
    i = 1
    while True:
        if ((i % x1 == 0) and (i % x2 == 0)):
            ex1 = i/x1
            ex2 = i/x2
            break
        i += 1

    nA1 = ex1*a1
    nB1 = ex1*b1
    nC1 = ex1*c1
    nA2 = ex2*a2
    nB2 = ex2*b2
    nC2 = ex2*c2

    A = nA1-nA2
    B = nB1-nB2
    C = nC1-nC2

    if A == 0:
        y = float(C/B)

    else:
        x = float(C/A)

    if A == 0:
        x = (c1-(y*b1))/a1
    else:
        y = (c1-(x*a1))/b1

print(x, end="  ")
print(y, end="  ")
