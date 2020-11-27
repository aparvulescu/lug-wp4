import numpy as np

def HolePattern(solutions,yieldvalues):
    v = 3653.76
    boltconfig = [] 
    h = 0.0131
    t1 = solutions[2] 
    tau_max = yieldvalues[solutions[3]]

    for n in range(2, 20, 2):
        tau_fast = 0
        d2 = 0.1
        while tau_fast < tau_max:
            d2 -= 0.001
            fs = v / n
            tau_fast = fs / (np.pi * (d2/2)**2)
        boltconfig.append([n, d2 + 0.002]) # find different configurations

    d2 = boltconfig[1][1]
    n = boltconfig[1][0]
    # note: we chose the configuration with 4 bolts because it provides more redundancy than 2, 
    # and more than 4 would cause diameter to be very small. The configuration can be changed later
    x = []
    f_top = 0
    f_bottom = 0

    for i in range(int(n/2)):
        for a in range(2):
            if i % 2 ==0:
                x.append(d2 + (f_top * 2 * d2))
                f_top += 1
            else:
                x.append(-d2 - (f_bottom * 2 * d2))
                f_bottom +=1

    length = h + (2*t1) + (4 * d2)
    z = []
    for i in range(n):
        if i % 2 ==0:
            z.append((length/2) - 1.5*d2)
        else:
            z.append(-(length/2) + 1.5*d2)
    r = n * [(d2/2)]

    holes = []
    for i in range(n):
        holes.append([r[i], x[i], z[i]])

    return holes,d2