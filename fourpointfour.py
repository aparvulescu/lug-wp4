from main import w,t
import numpy as np
# inputs
v = float(input("Total shear force "))
h = 0.0131
t1 = t
tau_max = 207 * 10**6  # mpa
d2 = 0.002
n = int((w-(3*d2))/d2)
tau_avg = 0

# iteration
while tau_avg < tau_max:
    n = n - 1
    fs = v / n
    tau_avg = fs / (np.pi * (d2/2)**2)
    print([tau_avg, fs, n])

# find coordinates
n = n + 1
if n % 2 != 0:
    n = n + 1

x = []
f_top = 0
f_bottom = 0

for i in range(int(n/2)):
    for a in range(2):
        if i % 2 ==0:
            x.append(d2 + (f_top * 2 * d2))
            f_top += 1
        else:
            x.append(-d2 - (f_bottom * 2 * d2))
            f_bottom +=1

length = h + (2*t1) + (4 * d2)
z = []
for i in range(n):
    if i % 2 ==0:
        z.append((length/2) - 1.5*d2)
    else:
        z.append(-(length/2) + 1.5*d2)
r = n * [(d2/2)]

holes = []
for i in range(n):
    holes.append([r[i], x[i], z[i]])
print("Coordinates: ", holes)