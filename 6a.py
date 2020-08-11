import math

import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as AA
from mpl_toolkits.axes_grid1 import host_subplot
from scipy import signal

from results_txt.read_bode import read_bode

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
frequencies = [f * (2 * math.pi) for f in range(80, 50000, 10)]
w, mag, phase = s1.bode(w=frequencies)
w2, mag2, phase2 = s2.bode(w=frequencies)
w3, mag3, phase3 = read_bode()

mag_plot = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)
phase_plot = mag_plot.twinx()

mag_plot.plot(w, mag, color='orange', linestyle='dotted', label="H (dB) (valores exactos)")
mag_plot.plot(w2, mag2, color='orange', linestyle='dashed', label="H (dB) (valores normalizados)")
mag_plot.plot(w3, mag3, color='orange', label="H (dB) (LTspice)")
mag_plot.set_ylabel('H (dB)')
mag_plot.set_ylim(-55, 1)

phase_plot.plot(w, phase, color='blue', linestyle='dotted', label="Φ (grados) (valores exactos)")
phase_plot.plot(w2, phase2, color='blue', linestyle='dashed', label="Φ (grados) (valores normalizados)")
phase_plot.plot(w3, phase3, color='blue', label="Φ (grados) (LTspice)")
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

plt.title('Bode de módulo y fase para los valores normalizados elegidos')
plt.xlabel('w (rad/s)')
plt.xlim(frequencies[0], frequencies[-1])
plt.xscale("log")
plt.xticks(
    [1256.85, 12568.5, 125685, 8714, 18128, 871.4, 1812.8, 87140, 181280],
    ['1256.85', '12568.5', '125685', 'ω₁=8714          ', '               ω₂=18128', '0.1ω₁        ', '        0.1ω₂', '10ω₁        ', '        10ω₂']
)
plt.grid(True, axis="x")
plt.legend()
plt.show()
