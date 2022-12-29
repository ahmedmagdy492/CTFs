#!/bin/python3

import math
from sympy.ntheory.primetest import is_square

#n = 631371953793368771804570727896887140714495090919073481680274581226742748040342637
n = 15
a = math.isqrt(n)

while True:
    b2 = a^2 - n
    if is_square(b2):
        b = math.sqrt(b2)
        break
    a = a + 1

p = a + b
q = a - b

print(str(p))
print(str(q))
