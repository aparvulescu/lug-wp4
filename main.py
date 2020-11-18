import math
import numpy as np


print("Hello project!")


#Graphs Kt
#1 y = 0.0008*x**6 - 0.0151*x**5 + 0.1007*x**4 - 0.3179*x**3 + 0.485*x**2 - 0.3574*x + 1.1067
#2 y = -1e-05*x**6 - 0.0017*x**5 + 0.0107*x**4 - 0.0146*x**3 - 0.0195*x**2 + 0.0097*x + 0.9957
#3 y = -0.0002*x**6 + 0.0027*x**5 - 0.0189*x**4 + 0.0645*x**3 - 0.1043*x**2 + 0.0119*x + 0.9957
#4 y = -0.0002*x**6 + 0.004*x**5 - 0.0268*x**4 + 0.0906*x**3 - 0.1471*x**2 + 0.0057*x + 1.0003
#5 y = -0.0003*x**6 + 0.0045*x**5 - 0.0261*x**4 + 0.0671*x**3 - 0.0555*x**2 - 0.1367*x + 1.0102
#6 y = -0.0008*x**6 + 0.0132*x**5 - 0.0871*x**4 + 0.2668*x**3 - 0.3574*x**2 - 0.0562*x + 0.9906
#7 Kt = -0.085*x + 0.765
# x = (w/D)
# y = Kt

# Graphs Kbry
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

# Graphs Ktu and Kty 
# (Kty for all aluminium and steel alloys) y = -0.8673*x**6 + 3.3352*x**5 - 4.4913*x**4 + 2.4227*x**3 - 0.7468*x**2 + 1.3913*x - 0.0106
# y = Ktu and Kty
# x = (Aav/Abr)









metals = ["2014-T6", "7075-T6", "2024-T4", "356-T6"]
aFty = [365e6, 462e6, 275e6, 138e6]  # Pa
aFtu = [415e6, 538e6, 425e6, 207e6]  # Pa

opt = 0

for w in np.arange(1e-3, 100e-3, 1e-3): # m
    for D in np.arange(1e-3, w, 1e-3): # m
        for t in np.arange(0.1e-3, 10e-3, 0.1e-3): # m
            for im in range(len(metals)):
                
                # yield & ultimate strengths
                Fty = aFty[im]
                Ftu = aFtu[im]

                # shear out-bearing strength (longitudinal)
                Abr = D * t
                Pbry = Kbry * Ftu * Abr

                # Bolt or pin bending (transverse)
                A2 = A3 = (w - D) / 2
                A1 = A4 = A3 + D/2 * (1 - math.sqrt(2)/2)
                Aav = 6 / (3 / A1 + 1 / A2 + 1 / A3 + 1 / A4)
                x = Aav / Abr

                Kty = -0.8673*x**6 + 3.3352*x**5 - 4.4913*x**4 + 2.4227*x**3 - 0.7468*x**2 + 1.3913*x - 0.0106

                Pty = Kty * Abr * Fty

                # tension across the net section (longitudinal)
                At = w * t

                if metals[im] == "2014-T6":
                    aKt = [1, 2, 4, 5]
                elif metals[im] == "7075-T6":
                    aKt = [1, 2, 4, 6]
                elif metals[im] == "2024-T4":
                    aKt = [3, 4]
                elif metals[im] == "356-T6":
                    aKt =[7]
                else:
                    print("Wrong metal selected. Exiting...")
                    break

                for iKt in len(aKt):
                    Kt = aKt[iKt]
                    Pu = Kt * Ftu * At 

                    # Checking condition
                    Ra = Pa / min(Pu, Pbry)
                    Rtr = Ptr / Pty
                    check = Ra**1.6 + Rtr**1.6

                    if (0.99 <= check <= 1.01):
                        opt += 1
                        print(f"Found the best dimensions option {opt}!")
                        print(f"w = {w:.4f}, D = {D:.4f}, t = {t:.4f}, metal = {metals[im]}, curve_d1.12 = {iKt}")


# Materials
# 2014-T6 = 365 [MPa]
# 7075-T6 = 462 [MPa]
# 2024-T4 = 275 [MPa]
# 356-T6 = 138 [MPa]
