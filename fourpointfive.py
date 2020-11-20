from fourpointfour import holes
import math

Asum = 0
Axsum = 0
Azsum = 0
for i in holes:
    Asum = Asum + (math.pi) * (holes[holes.index(i)][0])**2
    Axsum = Axsum + ((math.pi) * (holes[holes.index(i)][0])**2) * (holes[holes.index(i)][1])
    Azsum = Azsum + ((math.pi) * (holes[holes.index(i)][0])**2) * (holes[holes.index(i)][2])

xcg = Axsum / Asum
zcg = Azsum / Asum

print(xcg,zcg)