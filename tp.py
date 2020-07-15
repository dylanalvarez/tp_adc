from scipy import signal
import matplotlib.pyplot as plt

s1 = signal.lti(
    [1.579e8, 0, 0],
    [1, 1.777e4, 4.737e8, 2.806e12, 2.494e16]
)
w, mag, phase = s1.bode()

plt.figure()
plt.semilogx(w, mag)
plt.figure()
plt.semilogx(w, phase)
plt.show()
