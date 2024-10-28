import numpy as np
import matplotlib.pyplot as plt

#Teht. 1: Piirrä funktion kuvaaja

#Teht. 2: Piirrä funktion kuvaaja

x_y_range = np.linspace(-5, 0, 20)
y = (3/5)*x_y_range+3
plt.plot(x_y_range, y)

x_z_range = np.linspace(0, 4, 20)
z = np.full_like(x_z_range, 3)
plt.plot(x_z_range, z)

x_v_range = np.linspace(4, 8, 20)
v = -(3/4)*x_v_range+6
plt.plot(x_v_range, v)

x_u_range = np.linspace(8, 10, 20)
u = (1/2)*x_u_range-4
plt.plot(x_u_range, u)

plt.show()

#Teht. 3: 1A + B: huipun tarkistus
x = np.linspace(-5, 5, 20)
y = x**2-4*x+3
plt.plot(x, y)
plt.show()

x = np.linspace(-5, 5, 50)
y = -1.5*x**2-3*x+7

plt.plot(x, y)
plt.show()

#Teht. 4
x = np.linspace(0, 100, 20)
y = -0.0063*(x**2)+0.55*x
plt.ylim(0, 15)
plt.plot(x, y)
plt.show()

#Teht. 5
#1.a,b,c
x = np.linspace(-5, 5, 100)
a = x**2
b = x**3
c = x**4
plt.plot(x, a, color='red')
plt.plot(x, b, color='blue')
plt.plot(x, c, color='orange')
plt.ylim(-5, 10)
plt.show()

#2.a,b,c
x = np.linspace(-5, 5, 100)
a = x**-2
b = x**-3
c = x**-4
plt.plot(x, a, color='red')
plt.plot(x, b, color='blue')
plt.plot(x, c, color='orange')
plt.ylim(-5, 10)
plt.show()

#3.a,b,c
x = np.linspace(0, 10, 100)
a = x**2.5
b = x**0.4
c = x
plt.plot(x, a, color='red')
plt.plot(x, b, color='blue')
plt.plot(x, c, color='orange')
plt.ylim(-5, 10)
plt.show()