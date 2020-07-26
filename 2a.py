import math

from scipy import signal
import matplotlib.pyplot as plt

n_2 = 1.579e8

d_4 = 1
d_3 = 1.777e4
d_2 = 4.737e8
d_1 = 2.806e12
d_0 = 2.494e16

s1 = signal.lti(
    [n_2, 0, 0],
    [d_4, d_3, d_2, d_1, d_0]
)
frequencies = [f * (2 * math.pi) for f in range(80, 50000, 10)]
w, mag, phase = s1.bode(w=frequencies)

plt.figure()
plt.semilogx(w, mag)
plt.figure()
plt.semilogx(w, phase)
plt.show()
