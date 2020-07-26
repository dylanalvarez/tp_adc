import math

from scipy import signal
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
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

mag_plot = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
phase_plot = mag_plot.twinx()

mag_plot.plot(w, mag, label="H (dB)")
mag_plot.set_ylabel('H (dB)')
mag_plot.set_ylim(-55, 1)

phase_plot.plot(w, phase, label="Φ (grados)")
phase_plot.set_ylabel('Φ (grados)')
phase_plot.set_ylim(-186, 186)
phase_plot.axis["right"] = phase_plot.get_grid_helper().new_fixed_axis(
    loc="right",
    axes=phase_plot,
    offset=(0, 0)
)
phase_plot.set_yticks([180, 90, 0, -90, -180], minor=False)
phase_plot.set_yticklabels(['180º', '90º', '0º', '-90º', '-180º'])
phase_plot.grid(True, which="major", axis="y")

plt.title('Bode de módulo y fase para la transferencia asignada')
plt.xlabel('w (rad/s)')
plt.xlim(frequencies[0], frequencies[-1])
plt.xscale("log")
plt.xticks(
    [1300, 13000, 130000, 8714, 18128],
    ['1.3k', '13k', '130k', 'ω₁=8714          ', '               ω₂=18128']
)
plt.grid(True, axis="x")
plt.legend()
plt.show()
