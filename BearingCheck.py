import math
def BearingCheck(holes,geometry,yieldvalues):
    Asum = 0
    Axsum = 0
    Azsum = 0

    Fx = 1427.4
    Fz = 665.7

    Ax2sum = 0
    Az2sum = 0

    nf = len(holes)
    F_in_plane_x = Fx / nf
    F_in_plane_z = Fz / nf

    Finplanemylst = []
    sigma = yieldvalues[geometry[3]]
    
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

    Pilst = []
    for i in Finplanemylst:
        Fnetx = F_in_plane_x + i[0]
        Fnetz = F_in_plane_z + i[1]
        Pi = math.sqrt((Fnetx**2) + (Fnetz**2))
        Pilst.append(Pi)
    
    tlst = []
    for i in Pilst:
        t_2 = Pilst[Pilst.index(i)] / (2 * sigma * holes[Pilst.index(i)][0])
        tlst.append(t_2)

    return max(tlst)

def BearingCheckWall(holes,geometry,yieldvalues, t):
    Asum = 0
    Axsum = 0
    Azsum = 0

    Fx = 1427.4
    Fz = 665.7

    Ax2sum = 0
    Az2sum = 0

    nf = len(holes)
    
    F_in_plane_x = Fx / nf
    F_in_plane_z = Fz / nf

    Finplanemylst = []
    SigmaYield = yieldvalues[geometry[3]]

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
    
    Pilst = []
    for i in Finplanemylst:
        Fnetx = F_in_plane_x + i[0]
        Fnetz = F_in_plane_z + i[1]
        Pi = math.sqrt((Fnetx**2) + (Fnetz**2))
        Pilst.append(Pi)
    
    sigmalist = []
    for i in Pilst:
        sigma = Pilst[Pilst.index(i)] / (2 * t * holes[Pilst.index(i)][0])
        sigmalist.append(sigma)
    
    MSlist = []
    for i in sigmalist:
        MS = ( SigmaYield / sigmalist[sigmalist.index(i)] ) - 1
        MSlist.append(MS)

    return min(MSlist)   