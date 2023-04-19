# input: enter 2 Integer(weight, height)
# output: Print body surface area value from ..
#         Mosteller rule: s = sqrt(w*h/3600)
#         Dubois rule: (71.84*(w ^ 0.425)*(h ^ 0.725)) / 10000
#         Boyd rule: s = 0.0003207*(h ^ 0.3) * [(1000*w) ^ (0.7285-0.0188(3+log10w))]
# Example: 80  180 - -> 2.0  1.996  2.007
#          64  155 - -> 1.6  1.629  1.699
#          50  160 - -> 1.4  1.501  1.497

import math
n = [int(input()) for i in range(2)]

Mosteller = math.sqrt(n[0]*n[1]/3600)
Dubois = (71.84*(math.pow(n[0], 0.425))*(math.pow(n[1], 0.725))) / 10000
Boyd = 0.0003207*(math.pow(n[1], 0.3))*(math.pow((1000*n[0]), (0.7285-0.0188*(3+math.log10(n[0])))))

print("%.1f" % Mosteller, end="  ")
print("%.3f" % Dubois, end="  ")
print("%.3f" % Boyd, end="  ")
