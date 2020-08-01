import fractions

import numpy as np

a = 5767.16
b = 7.59038e7
c = 12002.8
d = 3.28574e8
w = 1300.6

a = np.array([
    [1, 0, 1, 0],
    [0, 1, a, 1],
    [w ** 2, 0, b, a],
    [0, w ** 2, 0, b]
])

b = np.array([
    0, 0.69 * w, 1295 * w, 0
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
