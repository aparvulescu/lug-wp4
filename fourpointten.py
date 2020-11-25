import math
from fourpointfour import holes
from main_e import metals,youngsm

Dlst = []
Frlst = []
for i in holes:
    Dsublst = []
    Dfi = 2 * holes[holes.index(i)][0]
    Dfo = 1.20 * 2 * holes[holes.index(i)][0]
    Dsublst.append(Dfi)
    Dsublst.append(Dfo)
    Dlst.append(Dsublst)
    della = (4 * t2) / (youngsbackplate *math.pi * (Dfo**2 - Dfi**2))
    dellb = (1/Eb)*(((0.4 * 4)/(math.pi * Dfo))+((0.4 * 4)/(math.pi * Dfi))+((0.4 * 4)/(math.pi * Dfo)))
    Fratio = della / (della + dellb)
    Frlst.append(Fratio)

youngsa =
Eb = 
youngsbackplate =  
yeildstress = 
thermalexpansion = 





