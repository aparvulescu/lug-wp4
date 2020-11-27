import math

def Bending(geometry,YieldStress):
    D1 = geometry[1]
    w = geometry[0]
    im = geometry[3]
    Fz = 665.7

    y = (w - D1) * YieldStress[im] / (6 * Fz) + 1 - D1 / 2
    return y
