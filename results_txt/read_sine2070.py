import re


def read_sine2070():
    t = []
    mag = []
    with open('results_txt/sine2070.txt') as f:
        for line in f.readlines()[1:]:
            m = re.match(r'(.*)	(.*)', line)
            _t = float(m.group(1))
            _mag = float(m.group(2))
            t.append(_t)
            mag.append(_mag)
    return t, mag
