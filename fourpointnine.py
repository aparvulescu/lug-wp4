from fourpointfour import holes
from fourpointeight import Flst
import math


#Yield Stress Materials = Something
SigmaYield = 

Taulst = []
for i in holes:
    Dfi = 0.95 * 2 * holes[holes.index(i)][0]
    Fi = Flst[holes.index(i)]
    Tau = Fi / (math.pi * Dfi * (t2 + 2.5e-3))
    if Tau > SigmaYield:
        print('failure!')
    Taulst.append(Tau)

print(Taulst)