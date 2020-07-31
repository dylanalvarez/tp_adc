import fractions

import numpy as np

a = 5767.16
b = 7.59038e7
c = 12002.8
d = 3.28574e8
k = 1.579e8

a = np.array([
    [1, 0, 1, 0],
    [c, 1, a, 1],
    [d, c, b, a],
    [0, d, 0, b]
])

b = np.array([
    0, 0, k, 0
])

x = np.linalg.solve(a, b)

print("")
print("Decimal")
print(x)
print("")
print("Fractions")
np.set_printoptions(formatter={
    'all': lambda _x: str(fractions.Fraction(_x).limit_denominator())})
print(x)
