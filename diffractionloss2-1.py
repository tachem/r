from matplotlib import pyplot as plt
from scipy import  integrate
import math

d1 = 1000.
d2 = 9000.
lmbd = 1.
A = math.sqrt(2. * (d1+d2)/(d1*d2*lmbd))

E_list = []
u_list = []

for hc in range(0,101):
    u = hc * A
    s, _ = integrate.quad(lambda x: math.sin(0.5 * math.pi * x**2), 0, u)
    c, _ = integrate.quad(lambda x: math.cos(0.5 * math.pi * x**2), 0, u)
    _E = c*s + 0.5*(c+s) + 0.25
    print('h:{0}, u:{1}, s:{2}, c:{3}, E:{4}'.format(hc,u,s,c,_E))
    assert _E >= 0.
    E = math.sqrt(_E)
    E_list.append(E)
    u_list.append(u)

fig, ax1 = plt.subplots()
ax2=ax1.twiny()
ax1.plot(range(0,101), E_list)
ax2.plot(u_list, E_list)
ax1.set_xlabel(r'$h_c [m]$', fontsize=12, fontname='serif')
ax1.set_ylabel(r"$|E/E_0|$", fontsize=12, fontname='serif')
ax2.set_xlabel(r"$\mu$ [m]", fontsize=12, fontname='serif')
# plt.title("2-1", fontsize=20, fontname='serif')
ax1.grid(True, linestyle='dotted')
#plt.savefig("p1.png")
plt.show()
