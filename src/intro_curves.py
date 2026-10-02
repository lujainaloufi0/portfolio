"""Intro motion curves, measured frame by frame from a 1920 px wide screen recording of the motion study.

Units are half-resolution page pixels of that recording: page height 472.5, the card's final top edge 154,
final height 283.5 (scale 1). Times are video seconds; the page starts drawing at T0.
Each phase is fitted with a monotone cubic (PCHIP) through cleaned measurements, then sampled at 60 Hz,
so the browser plays one continuous curve instead of eased keyframe segments that stop at every step.
"""
import json
import numpy as np
from scipy.interpolate import PchipInterpolator as P

T0, T1, HZ = 0.12, 5.30, 60
t = np.arange(T0, T1 + 1e-9, 1 / HZ)

def curve(pts, x):
    xs, ys = zip(*pts)
    return P(xs, ys)(np.clip(x, xs[0], xs[-1]))

# phase 1 (0.12-0.8): small card, tilted back about its bottom edge, fades in and lies flat
s1 = curve([(0.12, .555), (0.3, .563), (0.5, .578), (0.7, .600), (0.78, .610)], t)
th = curve([(0.12, 18), (0.35, 15), (0.5, 11), (0.56, 8.2), (0.62, 5.4), (0.68, 2.2), (0.76, 0), (5.3, 0)], t)
op = curve([(0.12, 0), (0.25, .08), (0.3, .13), (0.4, .22), (0.47, .31), (0.53, .5), (0.6, .7),
            (0.65, .83), (0.7, .91), (0.76, .96), (0.86, 1), (5.3, 1)], t)
# phase 2 (0.78-1.6): grows toward you and sinks until only its top shows at the bottom edge
p = curve([(0.78, 0), (0.82, .025), (0.85, .07), (0.9, .142), (0.95, .232), (1.0, .34), (1.05, .47),
           (1.1, .597), (1.15, .705), (1.2, .78), (1.25, .85), (1.3, .903), (1.35, .932), (1.4, .957),
           (1.45, .974), (1.5, .988), (1.6, 1)], t)
# phase 4 (2.88-3.85): rises back into the middle, slow start, fast middle, long settle
q = curve([(2.88, 0), (2.95, .012), (3.0, .026), (3.05, .042), (3.1, .072), (3.15, .118), (3.2, .17),
           (3.25, .235), (3.3, .335), (3.34, .5), (3.38, .655), (3.42, .765), (3.47, .852), (3.52, .905),
           (3.57, .94), (3.62, .963), (3.68, .981), (3.75, .993), (3.85, 1)], t)
# phase 5 (4.35-5.25): drops into its final place to make room for the title
r = curve([(4.35, 0), (4.45, .015), (4.55, .046), (4.65, .108), (4.7, .154), (4.75, .215), (4.8, .30),
           (4.84, .45), (4.88, .6), (4.93, .74), (5.0, .86), (5.07, .93), (5.15, .975), (5.25, 1)], t)
# phase 3 (1.8-2.75): the fanned stack behind it collapses down into it
c = curve([(1.78, 0), (1.82, .03), (1.85, .085), (1.9, .145), (1.95, .225), (2.0, .335), (2.05, .45),
           (2.1, .575), (2.15, .672), (2.2, .755), (2.25, .823), (2.3, .87), (2.35, .906), (2.4, .932),
           (2.45, .951), (2.5, .965), (2.6, .982), (2.75, 1)], t)

s = np.where(t < 0.78, s1, .610 + (1.10 - .610) * p)
s = np.where(t >= 2.88, 1.10 - .10 * q, s)
bottom = 380.5 + (674 - 380.5) * p
bottom = np.where(t >= 2.88, 674 - 302 * q, bottom)
bottom = np.where(t >= 4.35, 372 + 65.25 * r, bottom)
top = bottom - s * 283.5

r4 = lambda a: [round(float(v), 4) for v in a]
DATA = {'hz': HZ, 's': r4(s), 'top': [round(float(v), 2) for v in top], 'th': [round(float(v), 2) for v in th],
        'op': r4(op), 'c': r4(c)}
JS = 'const INTRO=' + json.dumps(DATA, separators=(',', ':')) + ';\n'

if __name__ == '__main__':
    print(len(t), 'samples', len(JS), 'bytes')
    for i in range(0, len(t), 15):
        print(round(t[i], 2), DATA['s'][i], DATA['top'][i], DATA['th'][i], DATA['op'][i], DATA['c'][i])
