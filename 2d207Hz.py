import matplotlib.pyplot as plt
import numpy as np
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

degrees = list(range(0, 360 * 3))
period = 4.8309e-3
sin_v = np.sin(np.array(degrees) * np.pi / 180.)
sin_t = [deg * period / 360 for deg in degrees]

t, y, x = s1.output(list(sin_v), sin_t)

plt.plot(t, y, label='Salida (V)')
plt.plot(sin_t, [sin / 100 for sin in sin_v], label='Entrada (V/100)')
plt.xticks(
    [0, period, 2 * period, 3 * period],
    ['0', '4.8m', '9.7m', '14.5m']
)
plt.xlim(-0.0001, t[-1])
plt.xlabel('Tiempo (s)')
plt.ylabel('Tensión (V)')
plt.title('Respuesta a la entrada senoidal de 207Hz para la transferencia asignada')
plt.grid()
plt.legend()
plt.show()
