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
s2 = signal.lti(
    [5.767e-9, 0, 0],
    [4.264e-17, 7.608e-13, 1.948e-8, 1.142e-4, 1]
)
t, y = signal.step2(s1, N=1000)
t2, y2 = signal.step2(s2, N=1000)

plt.plot(t, y, color='blue', linestyle='dotted', label="Salida (V) (valores exactos)")
plt.plot(t2, y2, color='blue', label="Salida (V) (valores normalizados)")
plt.plot([-0.0005, 0, 0, t[-1]], [0, 0, 1, 1], color='orange', label="Entrada (V)")
plt.xlim(-0.0001, t[-1])
plt.xlabel('Tiempo (s)')
plt.ylabel('Tensión (V)')
plt.title('Respuesta al escalón para los valores normalizados elegidos')
plt.grid()
plt.legend()
plt.show()
