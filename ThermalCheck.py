import math
from main import cte

def ThermalCheck(geometry, holes, t, youngsm, yieldvalues, d2): 
    youngsbackplate = youngsm[geometry[3]]
    Eb = youngsm[geometry[5]] 
    t2 = geometry[7]

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
    absorbtivity = 0.525
    emissivity = 0.09

    alphac = cte[geometry[3]]#thermal coefficient hinge
    alphab = cte[geometry[5]]#thermal coefficient bolt
    
   #backplate length
    y = geometry[6]
    w = geometry[0] 
    D1 = geometry[1]
    t1 = geometry[2]
    
    l = geometry[9]

    Aabs = t2 * w + y * w + 0.5 * math.pi *(w/2)**2 - math.pi * (D1/2)**2
    Aemit = 2* Aabs + 2* (w * t2 + 2*(t1*(y+((D1/2)+(w-D1)/2)))) + l * w

    Tmax = (((1665.0 * absorbtivity + 179.0 * emissivity) * Aabs)/((5.67e-8) * emissivity * Aemit))**(1/4)
    # Tmin = ((179 * Aabs) / ((5.67e-8) * Aemit))**(1/4)

    DeltaTmax = Tmax - 288.15
    # DeltaTmin = Tmin - 288.15

    Dfi = d2
    
    FdeltaTmax = (alphac - alphab) * DeltaTmax * Eb * (math.pi*(Dfi/2)**2) * (1-MaxFratio)
    # FdeltaTmin = (alphac - alphab) * DeltaTmin * Eb * (math.pi*(Dfi/2)**2) * (1-MaxFratio)

    Asum = 0
    Axsum = 0
    Azsum = 0

    Fx = 1427.4 + FdeltaTmax
    Fz = 665.7 + FdeltaTmax

    Ax2sum = 0
    Az2sum = 0

    Finplanemylst = []
    YieldStrength = yieldvalues[geometry[3]]

    for i in holes:
        Asum = Asum + (math.pi) * (holes[holes.index(i)][0])**2
        Axsum = Axsum + ((math.pi) * (holes[holes.index(i)][0])**2) * (holes[holes.index(i)][1])
        Azsum = Azsum + ((math.pi) * (holes[holes.index(i)][0])**2) * (holes[holes.index(i)][2])
    xcg = Axsum / Asum
    zcg = Azsum / Asum
    M_cg_y = Fz * xcg - Fx * zcg
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
    
    nf = len(holes)
    F_in_plane_x = Fx / nf
    F_in_plane_z = Fz / nf

    Pilst = []
    for i in Finplanemylst:
        Fnetx = F_in_plane_x + Finplanemylst[Finplanemylst.index(i)][1]
        Fnetz = F_in_plane_z + Finplanemylst[Finplanemylst.index(i)][2]
        Pi = math.sqrt((Fnetx**2) + (Fnetz**2))
        Pilst.append(Pi)
    
    sigmalist = []
    for i in Pilst:
        sigma = Pilst[Pilst.index(i)] / (2 * t * holes[Pilst.index(i)][0])
        sigmalist.append(sigma)
    
    MSlist = []
    for i in sigmalist:
        MS = (sigmalist[sigmalist.index(i)] / YieldStrength) - 1
        MSlist.append(MS)

    return min(MSlist)