from fourpointsix import Finplanemylst,F_in_plane_x,F_in_plane_z
from fourpointfour import holes
import math

t_2 = 
material_bearing_strength = 

Pilst = []
for i in Finplanemylst:
    Fnetx = F_in_plane_x + Finplanemylst[Finplanemylst.index(i)][1]
    Fnetz = F_in_plane_z + Finplanemylst[Finplanemylst.index(i)][2]
    Pi = math.sqrt((Fnetx**2) + (Fnetz**2))
    Pilst.append(Pi)

sigmalist = []
for i in Pilst:
    sigma = Pilst[Pilst.index(i)] / (t_2 * 2 * holes[Pilst.index(i)][0])
    sigmalist.append(abs(sigma))

if max(sigmalist) >= material_bearing_strength:
    print('failure!')
