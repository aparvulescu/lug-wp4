import numpy as np

def HolePattern(solutions,yieldvalues):
    v = 3653.76
    boltconfig = [] 
    h = 0.0131
    t1 = solutions[2] 
    tau_max = yieldvalues[solutions[3]]

    d2 = 0.005
    n = 2
    # note: we chose the configuration with 4 bolts because it provides more redundancy than 2, 
    # and more than 4 would cause diameter to be very small. The configuration can be changed later
    x = []
    f_top = 0
    f_bottom = 0

    # for i in range(int(n/2)):
    #    for a in range(2):
    #        if i % 2 ==0:
    #            x.append(d2 + (f_top * 2 * d2))
    #            f_top += 1
    #        else:
    #           x.append(-d2 - (f_bottom * 2 * d2))
    #           f_bottom +=1
    x.append(0)
    x.append(0)

    # length = h + (2*t1) + (4 * d2)
    z = []
    #for i in range(n):
    #    if i % 2 ==0:
    #        z.append((length/2) - 1.5*d2)
    #    else:
    #        z.append(-(length/2) + 1.5*d2)

    z.append(h/2 + t1 + 1.5 * d2)
    z.append(-(h/2 + t1 + 1.5 * d2))

    length = h + 2 * t1 + 6 * d2

    r = [d2/2, d2/2]

    holes = []
    for i in range(n):
        holes.append([r[i], x[i], z[i]])

    return holes,d2