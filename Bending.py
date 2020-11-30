import math

def Bending(geometry, YieldStress):
    D1 = geometry[1]
    w = geometry[0]
    im = geometry[3]
    t1 = geometry[2]
    Fz = 665.7 / 2

    # y = (w - D1) * YieldStress[im] * t1 * t1 / (6 * Fz) + 1 - D1 / 2
    y = YieldStress[im] * t1 * t1 * w / (6 * Fz) - D1 / 2

    # to be checked
    return y
    