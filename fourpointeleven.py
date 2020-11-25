import math
from main_e import metals and youngsm
from fourpointten import Fratio
absorbtivity =
emissivity = 
Eb = 
alphac = #thermal coefficient hinge
alphab = #thermal coefficient bolt


Tmax = ((1665 * absorbtivity + 179 * emissivity)/ (emissivity * 5.67*10**(-8)))**(1/4)
Tmin = (179/(5.67*10**(-8)))**(1/4)


DeltaTmax = Tmax - 288.15
DeltaTmin = Tmin - 288.15

FdeltaTmax = (alphac - alphab) * DeltaTmax * Eb * (math.pi*(Dfi/2)**2) * (1-Fratio)
FdeltaTmin = (alphac - alphab) * DeltaTmin * Eb * (math.pi*(Dfi/2)**2) * (1-Fratio)