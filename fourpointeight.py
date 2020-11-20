from fourpointfour import holes
from fourpointsix import Az2sum

nf = len(holes)
Fy = 899.795
Fpi = Fy / nf
Mx = 90.7

Flst = []
for i in holes:
    Fpmx = (Mx * ((math.pi) * (holes[holes.index(i)][0])**2) * (holes[holes.index(i)][2] - zcg)) / (Az2sum)
    F = abs(Fpmx) + Fpi
    Flst.append(F)

print(max(Flst))