import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

from results_txt.read_sine2070 import read_sine2070

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

degrees = list(range(0, 360 * 4))
period = 4.8309e-4
sin_v = np.sin(np.array(degrees) * np.pi / 180.)
sin_t = [deg * period / 360 for deg in degrees]

t, y, x = s1.output(list(sin_v), sin_t)
t1, y1 = read_sine2070()

plt.plot(t, y, color='blue', linestyle='dotted', label='Salida (V) (valores exactos)')
plt.plot(t1, y1, color='blue', label='Salida (V) (LTspice)')
plt.plot(sin_t, sin_v, color='orange', label='Entrada (V)')
plt.xticks(
    [0, period, 2 * period, 3 * period],
    ['0', '0.48m', '0.97m', '1.45m']
)
plt.xlim(-0.0001, t[-1])
plt.xlabel('Tiempo (s)')
plt.ylabel('Tensión (V)')
plt.title('Respuesta a la entrada senoidal de 2070Hz para la transferencia asignada')
plt.grid()
plt.legend()
plt.show()
