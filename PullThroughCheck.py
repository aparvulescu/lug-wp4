import math

def PullThroughCheck(holes,geometry,yieldvalues):
    Asum = 0
    Azsum = 0
    Az2sum = 0

    nf = len(holes)
    Fy = 899.795
    Fpi = Fy / nf
    Mx = 90.7

    for i in holes:
        Asum = Asum + (math.pi) * (holes[holes.index(i)][0])**2
        Azsum = Azsum + ((math.pi) * (holes[holes.index(i)][0])**2) * (holes[holes.index(i)][2])
    zcg = Azsum / Asum
    for i in holes:
        Az2sum = Az2sum + ((math.pi) * (holes[holes.index(i)][0])**2) * ((holes[holes.index(i)][2] - zcg)**2)
    
    Flst = []
    for i in holes:
        Fpmx = (Mx * ((math.pi) * (holes[holes.index(i)][0])**2) * (holes[holes.index(i)][2] - zcg)) / (Az2sum)
        F = abs(Fpmx) + Fpi
        Flst.append(F)

    SigmaYield = yieldvalues[geometry[3]]
    MSlst = []
    for i in holes:
        Dfi = 2 * holes[holes.index(i)][0]
        Dfo = 1.20 * 2 * holes[holes.index(i)][0]
        Fi = Flst[holes.index(i)]
        Tau = Fi/((4*math.pi) * (Dfo**2 - Dfi**2))
        MS = ( SigmaYield / Tau ) - 1
        MSlst.append(MS)

    return min(MSlst)