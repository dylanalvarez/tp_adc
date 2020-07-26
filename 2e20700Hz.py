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

periods = 30
period = 4.8309e-5
dots_per_period = 1000
square_v = [1 if step % dots_per_period < dots_per_period / 2 else -1 for step
            in range(dots_per_period * periods)]
square_t = [step * period / dots_per_period for step in
            range(dots_per_period * periods)]

t, y, x = s1.output(list(square_v), square_t)

plt.plot(t, y, label='Salida (V)')
plt.plot([-1e-20] + square_t, [0.] + [x / 100 for x in square_v],
         label='Entrada (V/100)')
plt.xticks(
    [0, period, 3 * period, 5 * period, 7 * period,
     9 * period, 11 * period, 13 * period, 15 * period,
     17 * period, 19 * period, 21 * period, 23 * period,
     25 * period, 27 * period, 29 * period, 31 * period],
    ['0', '', '', '', '7T=0.34m',
     '', '', '', '15T=0.72m',
     '', '', '', '23T=1.11m',
     '', '', '', '31T=1.50m']
)
plt.xlim(-0.00001, t[-1])
plt.xlabel('Tiempo (s)')
plt.ylabel('Tensión (V)')
plt.title(
    'Respuesta a la entrada cuadrada de 20700Hz para la transferencia asignada')
plt.grid()
plt.legend()
plt.show()
