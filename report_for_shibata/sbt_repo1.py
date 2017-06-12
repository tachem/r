'''
Shibata-san class.
Report 1; 2017/6/6
'''

import matplotlib.pylab as plt
import math

# unit
pico = 10**-12
nano = 10**-9
kilo = 10**3
micro = 10**-6

c = 3.0 * 10**8 # [m/sec]
L2 = []

x_range = range(100)
p0 = 1.# * 10**12
_lambda = 1.55 * micro  #[m]
D_coef = - _lambda**2 / (2 * math.pi * c)
D1_beta = 16. * D_coef * pico/nano/kilo #[ps/nm/km]
D2_beta = -160. * D_coef * pico/nano/kilo #[ps/nm/km]
L1 = 40. * kilo #[km]

for x in x_range:
    x = x * pico
    _l2 = ((math.sqrt(0.21) /(4*math.log(2))) * x**2 - D1_beta * L1) / D2_beta
    L2.append(_l2)

plt.plot(x_range, L2, label="")
# plt.legend(loc="upper left")
plt.xlabel(r"$t_0 \times 10^{-12}[sec]$")
plt.ylabel(r"$L_2$ [m]")
plt.title('Report 1 (2017.6.6)')
# plt.savefig('shibata-san-report1.png')
plt.show()
