import math
import numpy as np

print("Hello project!")

# Graphs Kt (0 < w/D < 5)
# 1 y = 0.0008*x**6 - 0.0151*x**5 + 0.1007*x**4 - 0.3179*x**3 + 0.485*x**2 - 0.3574*x + 1.1067
# 2 y = -1e-05*x**6 - 0.0017*x**5 + 0.0107*x**4 - 0.0146*x**3 - 0.0195*x**2 + 0.0097*x + 0.9957
# 3 y = -0.0002*x**6 + 0.0027*x**5 - 0.0189*x**4 + 0.0645*x**3 - 0.1043*x**2 + 0.0119*x + 0.9957
# 4 y = -0.0002*x**6 + 0.004*x**5 - 0.0268*x**4 + 0.0906*x**3 - 0.1471*x**2 + 0.0057*x + 1.0003
# 5 y = -0.0003*x**6 + 0.0045*x**5 - 0.0261*x**4 + 0.0671*x**3 - 0.0555*x**2 - 0.1367*x + 1.0102
# 6 y = -0.0008*x**6 + 0.0132*x**5 - 0.0871*x**4 + 0.2668*x**3 - 0.3574*x**2 - 0.0562*x + 0.9906
# 7 y = -0.085*x + 0.765
# x = (w/D)
# y = Kt

# New curves
# 1 y = 3E-05*x**6 + 0.0014*x**5 - 0.0349*x**4 + 0.2593*x**3 - 0.8526*x**2 + 1.2345*x + 0.3477
# 2 y = 0.0011*x**6 - 0.0234*x**5 + 0.1705*x**4 - 0.5725*x**3 + 0.9316*x**2 - 0.7094*x + 1.1928 (1 < x < 4.3)
# 3 y = 0.0011*x**5 - 0.0182*x**4 + 0.1109*x**3 - 0.3089*x**2 + 0.3177*x + 0.9044
# 4 y = 0.0004*x**5 - 0.0091*x**4 + 0.0695*x**3 - 0.2243*x**2 + 0.1974*x + 0.9816
# 5 y = 0.0008*x**5 - 0.0102*x**4 + 0.0429*x**3 - 0.0403*x**2 - 0.2345*x + 1.2616
# 6 y = 0.0014*x**4 - 0.0228*x**3 + 0.1457*x**2 - 0.6176*x + 1.5311
# 7 y = 8E-05*x**5 - 0.0012*x**4 + 0.0058*x**3 - 0.007*x**2 - 0.0932*x + 0.7695


# Graphs Kbry (0.5 < e/D < 4)
# t/D = 0.06 --> y = -0.0256*x**6 + 0.3702*x**5 - 2.1559*x**4 + 6.4708*x**3 - 10.657*x**2 + 9.4033*x - 2.7146
# 0.08 --> y = -0.0274*x**6 + 0.4012*x**5 - 2.3667*x**4 + 7.2128*x**3 - 12.092*x**2 + 10.872*x - 3.2178
# 0.1 --> y = -0.0109*x**6 + 0.177*x**5 - 1.1718*x**4 + 4.065*x**3 - 7.8731*x**2 + 8.2806*x - 2.6362
# 0.12 --> y = -0.0019*x**6 + 0.0468*x**5 - 0.4298*x**4 + 1.9444*x**3 - 4.7295*x**2 + 6.0807*x - 2.0705
# 0.15 --> y = 0.0015*x**6 - 0.001*x**5 - 0.1642*x**4 + 1.2258*x**3 - 3.7981*x**2 + 5.6596*x - 2.0566
# 0.2 --> y = 0.007*x**6 - 0.0878*x**5 + 0.3792*x**4 - 0.4782*x**3 - 1.0448*x**2 + 3.6085*x - 1.5053
# 0.3 --> y = 0.0029*x**6 - 0.0405*x**5 + 0.1898*x**4 - 0.2193*x**3 - 0.9402*x**2 + 3.2203*x - 1.3373
# 0.4 --> y = -0.0074*x**6 + 0.0982*x**5 - 0.5319*x**4 + 1.6104*x**3 - 3.2634*x**2 + 4.6355*x - 1.6634
# 0.6 and higher -->  y = -0.0024*x**6 + 0.0295*x**5 - 0.1652*x**4 + 0.6366*x**3 - 1.9271*x**2 + 3.7516*x - 1.4463
# x = (e/D)
# y = Kbry

# Graphs Ktu and Kty (0 < Aav/Abr < 1.4)
# (Kty for all aluminium and steel alloys) y = -0.8673*x**6 + 3.3352*x**5 - 4.4913*x**4 + 2.4227*x**3 - 0.7468*x**2 + 1.3913*x - 0.0106
# y = Ktu and Kty
# x = (Aav/Abr)

# Materials
# 2014-T6 = 365 [MPa]
# 7075-T6 = 462 [MPa]
# 2024-T4 = 275 [MPa]
# 356-T6 = 138 [MPa]

metals = ["2014-T6", "7075-T6", "2024-T4", "356-T6", "4130 steel", "8630 steel"]
aFty = [365e6, 462e6, 275e6, 138e6, 360e6, 372.5e6]  # Pa
aFtu = [415e6, 538e6, 425e6, 207e6, 560e6, 562.5e6]  # Pa
youngsm = [72.4e9, 71.7e9, 73.1e9, 72.4e9, 200e9, 200e9]  # Pa
density = [2800, 2810, 2780, 2680, 7850, 7850]  # kg/m^3
cte = [23e-6, 23.6e-6, 23.2e-6, 21.4e-6, 12e-6, 11.25e-6]  # K^(-1)

Pa = 3911.73  # N
Ptr = 713.7  # N

opt = 0
solutions_43 = []

for w in np.arange(10e-3, 80e-3, 1e-3):  # m
    for D in np.arange(1e-3, w*4/5, 2e-3):  # m
        for t in np.arange(2e-3, 20e-3, 0.1e-3):  # m
            for im in range(len(metals)):

                # yield & ultimate strengths
                Fty = aFty[im]
                Ftu = aFtu[im]

                # shear out-bearing strength (longitudinal)
                Abr = D * t
                e = w / 2
                x = e / D
                if not (0.5 <= x <= 4.0):
                    # print("Value e/D is out of range. Exiting...")
                    break
                if 0.05 <= t / D <= 0.07:
                    Kbry = -0.0275 * x ** 6 + 0.3981 * x ** 5 - 2.3197 * x ** 4 + 6.965 * x ** 3 - 11.449 * x ** 2 + 10.025 * x - 2.8939
                    # old Kbry = -0.0256 * x ** 6 + 0.3702 * x ** 5 - 2.1559 * x ** 4 + 6.4708 * x ** 3 - 10.657 * x ** 2 + 9.4033 * x - 2.7146
                elif 0.07 < t / D <= 0.09:
                    Kbry = -0.0172 * x ** 6 + 0.2551 * x ** 5 - 1.527 * x ** 4 + 4.7355 * x ** 3 - 8.1534 * x ** 2 + 7.6987 * x - 2.2158
                    # old Kbry = -0.0274 * x ** 6 + 0.4012 * x ** 5 - 2.3667 * x ** 4 + 7.2128 * x ** 3 - 12.092 * x ** 2 + 10.872 * x - 3.2178
                elif 0.09 < t / D <= 0.11:
                    Kbry = -0.0041 * x ** 6 + 0.0815 * x ** 5 - 0.6436 * x ** 4 + 2.5948 * x ** 3 - 5.7124 * x ** 2 + 6.6933 * x - 2.1772
                    # old Kbry = -0.0109 * x ** 6 + 0.177 * x ** 5 - 1.1718 * x ** 4 + 4.065 * x ** 3 - 7.8731 * x ** 2 + 8.2806 * x - 2.6362
                elif 0.11 < t / D <= 0.135:
                    Kbry = -0.0024 * x ** 6 + 0.057 * x ** 5 - 0.5039 * x ** 4 + 2.2102 * x ** 3 - 5.2186 * x ** 2 + 6.5077 * x - 2.1991
                    # old Kbry = -0.0019 * x ** 6 + 0.0468 * x ** 5 - 0.4298 * x ** 4 + 1.9444 * x ** 3 - 4.7295 * x ** 2 + 6.0807 * x - 2.0705
                elif 0.135 < t / D <= 0.175:
                    Kbry = 0.0067 * x ** 6 - 0.0736 * x ** 5 + 0.2384 * x ** 4 + 0.1088 * x ** 3 - 2.1753 * x ** 2 + 4.492 * x - 1.7229
                    # old Kbry = 0.0015 * x ** 6 - 0.001 * x ** 5 - 0.1642 * x ** 4 + 1.2258 * x ** 3 - 3.7981 * x ** 2 + 5.6596 * x - 2.0566
                elif 0.175 < t / D <= 0.25:
                    Kbry = 0.0087 * x ** 6 - 0.1096 * x ** 5 + 0.4889 * x ** 4 - 0.749 * x ** 3 - 0.6999 * x ** 2 + 3.3867 * x - 1.4387
                    # old Kbry = 0.007 * x ** 6 - 0.0878 * x ** 5 + 0.3792 * x ** 4 - 0.4782 * x ** 3 - 1.0448 * x ** 2 + 3.6085 * x - 1.5053
                elif 0.25 < t / D <= 0.35:
                    Kbry = 0.009 * x ** 6 - 0.1194 * x ** 5 + 0.5882 * x ** 4 - 1.1927 * x ** 3 + 0.2351 * x ** 2 + 2.5822 * x - 1.2107
                    # old Kbry = 0.0029 * x ** 6 - 0.0405 * x ** 5 + 0.1898 * x ** 4 - 0.2193 * x ** 3 - 0.9402 * x ** 2 + 3.2203 * x - 1.3373
                elif 0.35 < t / D <= 0.5:
                    Kbry = 0.0031 * x ** 6 - 0.0432 * x ** 5 + 0.2126 * x ** 4 - 0.31 * x ** 3 - 0.7637 * x ** 2 + 3.0971 * x - 1.3066
                    # old Kbry = -0.0074 * x ** 6 + 0.0982 * x ** 5 - 0.5319 * x ** 4 + 1.6104 * x ** 3 - 3.2634 * x ** 2 + 4.6355 * x - 1.6634
                elif t/D > 0.5:  # t/D > 0.5
                    Kbry = -0.001 * x ** 6 + 0.0141 * x ** 5 - 0.0999 * x ** 4 + 0.5185 * x ** 3 - 1.8566 * x ** 2 + 3.7725 * x - 1.46
                    # old Kbry = -0.0024 * x ** 6 + 0.0295 * x ** 5 - 0.1652 * x ** 4 + 0.6366 * x ** 3 - 1.9271 * x ** 2 + 3.7516 * x - 1.4463
                else:
                    # print(f"Value t/D for Kbry is out of range! (t/D = {t/D:.4f}) Exiting...")
                    break

                Pbry = Kbry * Fty * Abr

                # Bolt or pin bending (transverse)
                A3test = (e - D / 2) * t
                A2 = (w - D) * (t / 2)
                A1 = A4 = ((w - D) / 2 + D / 2 * (1 - math.sqrt(2) / 2)) * t
                A3 = min(A2, A1, A3test)
                Aav = 6 / (3 / A1 + 1 / A2 + 1 / A3 + 1 / A4)
                x = Aav / Abr

                if 0 < x <= 1.4:
                    Kty = -0.8673 * x ** 6 + 3.3352 * x ** 5 - 4.4913 * x ** 4 + 2.4227 * x ** 3 - 0.7468 * x ** 2 + 1.3913 * x - 0.0106
                else:
                    # print(f"Value Aav/Abr for Kty is out of range! (Aav = {Aav}, Abr = {Abr}) Exiting...")
                    break

                Pty = Kty * Abr * Fty

                # tension across the net section (longitudinal)
                At = (w - D) * t

                if metals[im] == "2014-T6":
                    aKt = [1, 2, 4, 5]
                elif metals[im] == "7075-T6":
                    aKt = [1, 2, 4, 6]
                elif metals[im] == "2024-T4":
                    aKt = [3, 4]
                elif metals[im] == "356-T6":
                    aKt = [7]
                elif metals[im] == "4130 steel" or "8630 steel":
                    aKt = [1]
                else:
                    # print("Wrong metal selected. Exiting...")
                    break

                # x value for Kt curves
                xKt = (w / D)

                # Kt curves
                for iKt in range(len(aKt)):
                    curveKt = aKt[iKt]



                    if curveKt == 1 and 1 < xKt < 5:
                        Kt = 3e-05 * xKt ** 6 + 0.0014 * xKt ** 5 - 0.0349 * xKt ** 4 + 0.2593 * xKt ** 3 - 0.8526 * xKt ** 2 + 1.2345 * xKt + 0.3477
                    elif curveKt == 2 and 1 < xKt < 4.3:
                        Kt = 0.0011 * xKt ** 6 - 0.0234 * xKt ** 5 + 0.1705 * xKt ** 4 - 0.5725 * xKt ** 3 + 0.9316 * xKt ** 2 - 0.7094 * xKt + 1.1928
                    elif curveKt == 3 and 1 < xKt < 5:
                        Kt = 0.0011 * xKt ** 5 - 0.0182 * xKt ** 4 + 0.1109 * xKt ** 3 - 0.3089 * xKt ** 2 + 0.3177 * xKt + 0.9044
                    elif curveKt == 4 and 1 < xKt < 5:
                        Kt = 0.0004 * xKt ** 5 - 0.0091 * xKt ** 4 + 0.0695 * xKt ** 3 - 0.2243 * xKt ** 2 + 0.1974 * xKt + 0.9816
                    elif curveKt == 5 and 1 < xKt < 5:
                        kt = 0.0008 * xKt ** 5 - 0.0102 * xKt ** 4 + 0.0429 * xKt ** 3 - 0.0403 * xKt ** 2 - 0.2345 * xKt + 1.2616
                    elif curveKt == 6 and 1 < xKt < 5:
                        Kt = 0.0014 * xKt ** 4 - 0.0228 * xKt ** 3 + 0.1457 * xKt ** 2 - 0.6176 * xKt + 1.5311
                    elif curveKt == 7 and 1 < xKt < 5:
                        Kt = 8e-05 * xKt ** 5 - 0.0012 * xKt ** 4 + 0.0058 * xKt ** 3 - 0.007 * xKt ** 2 - 0.0932 * xKt + 0.7695
                    else:
                        # print("Value w/D is out of range!. Exiting....")
                        break

                    Pu = Kt * Fty * At

                    # Checking condition
                    Ra = Pa / min(Pu, Pbry)
                    Rtr = Ptr / Pty
                    check = Ra ** 1.6 + Rtr ** 1.6

                    if 0.99 <= check <= 1.01:
                        opt += 1
                        # print(f"Found the best dimensions option {opt}!")
                        # print(f"w = {w:.4f}, D = {D:.4f}, t = {t:.4f}, e = {e:.4f}, metal = {metals[im]}, curve_d1.12 = {curveKt}, check = {check:.4f}")
                        SM = 1 / (check ** 0.625) - 1  # safety margin
                        for fm in range(len(metals)):
                            if fm != im:
                                solution = [w, D, t, im, SM, fm]  # im = index of lug material
                                solutions_43.append(solution)

# print(solutions_43)

#----------------------------------- START MAIN---------------------------------------
from BearingCheck import BearingCheck,BearingCheckWall
from PullThroughCheck import PullThroughCheck
from ThermalCheck import ThermalCheck
from Holes import HolePattern
from masscalc import masscalculator
from Bending import Bending

MSavgLst = []
MSTotalLst = [] #order: [lug, backplate bearing, s/c wall bearing, backplate pullthrough, s/c pull through, backplate thermal, s/c thermal, average]
NewSolLst = []
for i in range(len(solutions_43)):
    MSLst = []
    
    holes,d2 = HolePattern(solutions_43[i], aFty)

    MSLst.append(solutions_43[i][4])
    
    y = Bending(solutions_43[i], aFty)
    solutions_43[i].append(y)

    t2 = BearingCheck(holes, solutions_43[i], aFty)
    solutions_43[i].append(t2)
   
    m_tot,l = masscalculator(solutions_43[i], density,holes,d2)
    solutions_43[i].append(m_tot)
    solutions_43[i].append(l)

    MSLst.append(0)

    MSbearingwall = BearingCheckWall(holes, solutions_43[i], aFty, 2.5e-3)
    MSLst.append(MSbearingwall)

    MSpullthrough = PullThroughCheck(holes, solutions_43[i], aFty, solutions_43[i][7])
    MSLst.append(MSpullthrough) 
    MSpullthrough = PullThroughCheck(holes, solutions_43[i], aFty, 2.5e-3)
    MSLst.append(MSpullthrough) 

    MSthermalbackplate1 = ThermalCheck(solutions_43[i], holes, solutions_43[i][7], youngsm, aFty, d2, cte)
    MSLst.append(MSthermalbackplate1)

    MSthermalbackplate2 = ThermalCheck(solutions_43[i], holes, 2.5e-3, youngsm, aFty, d2, cte)
    MSLst.append(MSthermalbackplate2)

    if any(t < 0 for t in MSLst) or solutions_43[i][6] < 0:
        continue
    else:
        MSTotalLst.append(MSLst)
        NewSolLst.append(solutions_43[i])

for i in MSTotalLst:
    MSavg = sum(i) / len(i)
    MSavgLst.append(round(MSavg, 3))

for i in range(len(NewSolLst)):
    if NewSolLst[i][6] >= 0.001 and MSavgLst[i] <= 0.2:
        print(f"Mtot = {round(NewSolLst[i][8], 3)}, MSavg = {round(MSavgLst[i], 3)}, Material = {metals[NewSolLst[i][3]]}, w = {NewSolLst[i][0]:.3f}, D1 = {NewSolLst[i][1]:.4f}, t1 = {NewSolLst[i][2]:.4f}, t2 = {NewSolLst[i][7]:.4f}, l = {NewSolLst[i][9]:.3f}, y = {NewSolLst[i][6]:.3f}, Fastener Material = {metals[NewSolLst[i][5]]}")
        print(f"List of MS's = {MSTotalLst[i]}")
# print(solutions_43)



