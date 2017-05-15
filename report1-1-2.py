'''
Abo-san class.
Report1 2017/4/18
Answer of Probrem 1-2.
'''

import matplotlib.pylab as plt
import math

eps1 = 1.
eps2 = 80.
n = math.sqrt(eps2/eps1)

def toRad(x_degree):
    return x_degree  * 2. * math.pi / 360.

max_theta1 = 90
R1 = []
T1 = []
for i in range(max_theta1):
    theta1 = toRad(float(i))
    E3 = eps2 * math.cos(theta1) - eps1 * math.sqrt(n*n - math.sin(theta1)**2)
    E2 = 2 * n * eps1 * math.cos(theta1)
    E1 = eps2 * math.cos(theta1) + eps1 * math.sqrt(n*n - math.sin(theta1)**2)
    R1.append(math.fabs(E3/E1))
    T1.append(math.fabs(E2/E1))

x = range(max_theta1)
plt.plot(x, R1, label="Reflection coef.")
plt.plot(x, T1, label="Transmission coef.")
plt.legend(loc="center left")
plt.xlabel(r"$\theta_1 [degree]$")
plt.title('air to water')
plt.savefig('abosan1-1-2.png')
plt.show()
