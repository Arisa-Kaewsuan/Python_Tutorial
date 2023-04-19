
# input: enter Integer(Celsius)
# output: Print result of ... convert Celsius to Fahrenheit(C=5/9*(F-32))
# Example: 37 - -> 98.6
#          27 - -> 80.6
#          32 - -> 89.6

C = float(input())

F = (C*1.8)+32
print("%.1f" % F)
