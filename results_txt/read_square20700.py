import re


def read_square20700():
    t = []
    mag = []
    with open('results_txt/square20700.txt') as f:
        for line in f.readlines()[1:]:
            m = re.match(r'(.*)	(.*)', line)
            _t = float(m.group(1))
            _mag = float(m.group(2))
            t.append(_t)
            mag.append(_mag)
    return t, mag
