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

periods = 3
period = 4.8309e-3
dots_per_period = 1000
square_v = [1 if step % dots_per_period < dots_per_period / 2 else -1 for step in range(dots_per_period * periods)]
square_t = [step * period / dots_per_period for step in range(dots_per_period * periods)]

t, y, x = s1.output(list(square_v), square_t)

plt.plot(t, y, label='Salida (V)')
plt.plot([-1e-20] + square_t, [0] + square_v, label='Entrada (V)')
plt.xticks(
    [0, period, 2 * period, 3 * period],
    ['0', '4.8m', '9.7m', '14.5m']
)
plt.xlim(-0.0001, t[-1])
plt.xlabel('Tiempo (s)')
plt.ylabel('Tensión (V)')
plt.title('Respuesta a la entrada cuadrada de 207Hz para la transferencia asignada')
plt.grid()
plt.legend()
plt.show()
