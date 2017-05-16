from math import sin, cos, sqrt,pi
import matplotlib.pylab as plt

def toRad(deg):
    return deg * 2. * pi / 360.

d = 1000.
_lambda = 0.3
r_list = [0., 0.9, 0.8, 0.7, 0.6]
dB_list = [1000., 1200., 1100., 1200., 900.]
theta_list = [0., 18., 20., 0., 18.] # degree

n_of_builldings = 4
def delta_l(db, theta_deg, dl):
    theta_rad = toRad(theta_deg)
    return db - (d+dl) + sqrt(db**2 + (d+dl)**2 -2. * db *(d+dl) * cos(theta_rad))

E0 = 1.
sumcos = 0.
sumsin = 0.
moving_d = 10 # [m] 

Elist = []
for d_l in range(-moving_d, moving_d):
    for i in range(n_of_builldings-1):
        sumcos += r_list[i] * cos(2.* pi * delta_l(dB_list[i], theta_list[i], d_l)/_lambda)
        sumsin += r_list[i] * sin(2.* pi * delta_l(dB_list[i], theta_list[i], d_l)/_lambda)
    _E = sqrt( (1. + sumcos)**2 + sumsin**2)
    Elist.append(_E)

x = range(-moving_d, moving_d)
plt.plot(x, Elist)
plt.plot()
plt.show()
