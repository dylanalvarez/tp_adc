import matplotlib.pyplot as plt
from scipy import signal

from results_txt.read_square2070 import read_square2070

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

periods = 5
period = 4.8309e-4
dots_per_period = 1000
square_v = [1 if step % dots_per_period < dots_per_period / 2 else -1 for step in range(dots_per_period * periods)]
square_t = [step * period / dots_per_period for step in range(dots_per_period * periods)]

t, y, x = s1.output(list(square_v), square_t)
t1, y1 = read_square2070()

plt.plot(t, y, color='blue', linestyle='dotted', label='Salida (V) (valores exactos)')
plt.plot(t1, y1, color='blue', label='Salida (V) (LTspice)')
plt.plot([-1e-20] + square_t, [0] + square_v, color='orange', label='Entrada (V)')
plt.xticks(
    [0, period, 2 * period, 3 * period],
    ['0', '0.48m', '0.97m', '1.45m']
)
plt.xlim(-0.0001, t1[-1])
plt.xlabel('Tiempo (s)')
plt.ylabel('Tensión (V)')
plt.title('Respuesta a la entrada cuadrada de 2070Hz para la transferencia asignada')
plt.grid()
plt.legend()
plt.show()
