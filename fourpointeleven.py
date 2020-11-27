import math
from fourpointfour import holes
from main import metals,youngsm


Eb = 
youngsbackplate = 
Dfo = 
Dfi =  

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

MaxFratio = max(Frlst)
absorbtivity =
emissivity = 

alphac = #thermal coefficient hinge
alphab = #thermal coefficient bolt
emissivity = 
absorbtivity = 

C =    #backplate width
B =    #backplate length
t2 = 
y = 
w = 
D1 = 

Aabs = t2 * c + y * w + 0.5 * math.pi *(w/2)**2 - math.pi * (D1/2)**2
Aemit = 2* Aabs + 2* (B * t2 + 2*(t1*(y+((D1/2)+(w-D1)/2))) + B * C


Tmax = (((1665*absorbtivity + 179 * emissivity)*Aabs)/((5.67e-8)*emissivity*Aemit))**(1/4)
Tmin = ((179*Aabs)/((5.67e-8)*Aemit))**(1/4)


DeltaTmax = Tmax - 288.15
DeltaTmin = Tmin - 288.15

FdeltaTmax = (alphac - alphab) * DeltaTmax * Eb * (math.pi*(Dfi/2)**2) * (1-MaxFratio)
FdeltaTmin = (alphac - alphab) * DeltaTmin * Eb * (math.pi*(Dfi/2)**2) * (1-MaxFratio)

