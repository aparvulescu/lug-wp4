from fourpointfive import xcg,zcg
from fourpointfour import holes
import math

Fx = 1427.4
Fz = 665.7

nf = len(holes)

M_cg_y = Fz * xcg - Fx * zcg

F_in_plane_x = Fx / nf
F_in_plane_z = Fz / nf

Ax2sum = 0
Az2sum = 0
Finplanemylst = []
for i in holes:
    Finplanemysublst = []
    Ax = ((math.pi) * (holes[holes.index(i)][0])**2) * (holes[holes.index(i)][1] - xcg)
    Az = ((math.pi) * (holes[holes.index(i)][0])**2) * (holes[holes.index(i)][2] - zcg)
    Ax2sum = Ax2sum + ((math.pi) * (holes[holes.index(i)][0])**2) * ((holes[holes.index(i)][1] - xcg)**2)
    Az2sum = Az2sum + ((math.pi) * (holes[holes.index(i)][0])**2) * ((holes[holes.index(i)][2] - zcg)**2)
    Finplane_my_x = (M_cg_y * Az)/(Az2sum)
    Finplane_my_z = (M_cg_y * Ax)/(Ax2sum)
    Finplanemysublst.append(Finplane_my_x)
    Finplanemysublst.append(Finplane_my_z)
    Finplanemylst.append(Finplanemysublst)

print(Finplanemylst)