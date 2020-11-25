from fourpointfour import holes
from fourpointeight import Flst
from main_e import metals,aFty
import math


#Yield Stress Materials = Something
SigmaYield = 

Taulst = []
for i in holes:
    Dfi = 2 * holes[holes.index(i)][0]
    Dfo = 1.20 * 2 * holes[holes.index(i)][0]
    Fi = Flst[holes.index(i)]
    Tau = Fi/((4*math.pi) * (Dfo**2 - Dfi**2))
    if Tau > SigmaYield:
        print('failure!')
    Taulst.append(Tau)

print(Taulst)


