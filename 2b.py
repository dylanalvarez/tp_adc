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
t, y = signal.step2(s1, N=1000)

plt.plot(t, y, label="Salida (V)")
plt.plot([-0.0005, 0, 0, t[-1]], [0, 0, 1, 1], label="Entrada (V)")
plt.xlim(-0.0001, t[-1])
plt.xlabel('Tiempo (s)')
plt.ylabel('Tensión (V)')
plt.title('Respuesta al escalón para la transferencia asignada')
plt.grid()
plt.show()
