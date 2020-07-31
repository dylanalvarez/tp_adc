import math

import matplotlib.pyplot as plt
from scipy import signal

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
t, y = signal.impulse2(s1, N=1000)

a = 2883.5
b = 6001.5
c = 0.69
d = 0.0844
e = 0.0857
f = 8228
g = 17088

plt.plot(t, y)
plt.plot(t, [-a * math.exp(-a * _t) * (
            c * math.cos(f * _t) - d * math.sin(f * _t)) - math.exp(-a * _t) * (
                         c * f * math.sin(f * _t) + d * f * math.cos(
                     f * _t)) + b * math.exp(-b * _t) * (
                         c * math.cos(g * _t) + e * math.sin(
                     g * _t)) - math.exp(-b * _t) * (
                         -c * g * math.sin(g * _t) + e * g * math.cos(g * _t))
             for _t in t])
plt.xlim(-0.0001, t[-1])
plt.xlabel('Tiempo (s)')
plt.ylabel('Tensión (V)')
plt.title('Respuesta al impulso para la transferencia asignada')
plt.grid()
plt.show()
