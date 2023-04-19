
# input: enter 5 Integer
#        number of students who received grades A, B, C and D
# output: Print GPA from (4*A)+(3*B)+(2*C)+(1*D)+(0*F) form
# Example: 15 20 10 25 10 - -> 2.0625

sum = 0.0
GPA = 0.0
nA = float(input())
nB = float(input())
nC = float(input())
nD = float(input())
nF = float(input())

sum = (4*nA)+(3*nB)+(2*nC)+(1*nD)+(0*nF)
GPA = sum / (nA+nB+nC+nD+nF)

print(GPA)
