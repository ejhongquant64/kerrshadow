"""
Libraries
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.facecolor'] = 'white'

"""
Definitions
"""
#Shadow cast for Kerr BH
#M-mass, r-radial coordinate, a-spin parameter
def alpha(M,r,a):
    f = 1 - 2 * M / r #metric function f(r)
    f1 = 2 * M / r ** 2 #f'(r)
    xi = (f1 * a ** 2 * r + f1 * r ** 3 + 2 * f * a ** 2 - 2 * f * r ** 2 - 4 * a ** 2) / a / (f1 * r + 2 * f)
    return -xi / np.sin(theta)

def beta(M,r,a):
    f = 1 - 2 * M / r
    f1 = 2 * M / r ** 2
    xi = (f1 * a ** 2 * r + f1 * r ** 3 + 2 * f * a ** 2 - 2 * f * r ** 2 - 4 * a ** 2) / a / (f1 * r + 2 * f)
    eta = (-r ** 6 * f1 ** 2 + (4 * r ** 5 * f + 8 * a ** 2 * r ** 3) * f1 - 4 * f ** 2 * r ** 4) / a ** 2 / (f1 * r + 2 * f) ** 2
    return np.sqrt(eta + a ** 2 * np.cos(theta) ** 2 - xi ** 2 * np.cos(theta) ** 2 / np.sin(theta) ** 2)

"""
Global Parameters
"""
M = 1
theta = np.pi/4 #make this close to pi/2 if one wants the equatiorial plane analysis

"""
Plotting
"""
fig, ax1 = plt.subplots(figsize=(6.4,4.8)) #figsize in inches

r = np.linspace(1.00001, 5, 250000)

p1 = (0.25,'--k')
p2 = (0.50,'--b')
p3 = (0.75,'--r')
p4 = (1.00,'--g')

for a, col in [p1, p2, p3, p4]:
    y1 = alpha(M,r,a)
    y2 = beta(M,r,a)
    ax1.plot(y1, y2, col, lw = '1', label=r'$a=$'+str(a)+r'$M$, $\theta = \pi/4$')
    ax1.plot(y1, -y2, col, lw = '1')

ax1.set_aspect('equal')
#ax1.axis([-9, 8, -7, 7])
ax1.set_xlabel(r'$\alpha$') 
ax1.set_ylabel(r'$\beta$',rotation=0)

plt.axhline(y=0,color='k',linewidth='0.75',linestyle='dotted')
plt.axvline(x=0,color='k',linewidth='0.75',linestyle='dotted')

plt.legend(loc='lower right', fontsize=10)

plt.tight_layout()
#plt.savefig("shadowcast.pdf",dpi=120)
plt.show() #ignore warnings
