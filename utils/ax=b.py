import numpy as np
import fractions

a = np.array([
    [1013000, -11000, 0],
    [-1011000, 11100, -100],
    [0, -100, 100]
])

b = np.array([
    0, 0, -1
])

x = np.linalg.solve(a, b)

print("")
print("Decimal")
print(x)
print("")
print("Fractions")
np.set_printoptions(formatter={'all': lambda _x: str(fractions.Fraction(_x).limit_denominator())})
print(x)
