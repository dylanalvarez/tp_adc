import math
import re


def read_bode():
    w = []
    mag = []
    phase = []
    with open('results_txt/bode.txt') as f:
        for line in f.readlines()[1:]:
            m = re.match(r'(.*)	\((.*)dB,(.*)°\)', line)
            _freq = float(m.group(1))
            _mag = float(m.group(2))
            _phase = float(m.group(3))
            w.append(2 * math.pi * _freq)
            mag.append(_mag)
            phase.append(_phase)
    return w, mag, phase
