
# input: enter 2 Integers(width, height)
# output: Print square area & Perimeter#
# Example: 5   10 - -> 50  30
#          10  16 - -> 160 52
#          7   13 - -> 91  40

W = int(input())
H = int(input())
A = W*H
L = 2*(W+H)
print(A, end="  ")
print(L)
