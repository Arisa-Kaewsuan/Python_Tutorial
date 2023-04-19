
# input: enter 1 Integer(sec)
# output: Print year month day hrs min sec
# Example: 1000000 - -> 0 0 11 13 46 40
# 5000000 - -> 0 1 27 20 53 20
# 2000000 - -> 0 0 23 3  33 20

sec = int(input())
year = sec/31556926
m = sec/2629743
day = sec/86400
hrs = (sec % (24*3600)) / 3600
min = (sec % 3600) / 60
s = sec % 60
print(int(year), end="  ")
print(int(m), end="  ")
print(int(day), end="  ")
print(int(hrs), end="  ")
print(int(min), end="  ")
print(int(s), end="  ")
