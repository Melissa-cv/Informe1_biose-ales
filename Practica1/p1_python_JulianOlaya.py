import numpy as np

v1 = np.array([67.1, 1, -0.3, 5.2, -6])
v2 = np.array([1, 3, 2.2, 5.1, 1])
me = v1 * v2

print (me)
#%%
pp = np.dot (v1,v2)
print (pp)
#%%
matriz = np.array ([(2,-1,-3),(4,-1.5,-2.5),(7.3,-0.9,-0.2)],)
print (matriz)
#%%
t = np.transpose(matriz)
print (t)
#%%
a= np.ones((2,2))
print (a)
#%%
b = np.array(3.3896)
c= np.round(b, 1)
print ('dato sin redondear', b)
print ('dato con 1 decimal', c)
#%%
d = np.array(5.26)
e = np.ceil(d)
print ('dato sin redondear', d)
print('dato redondeado hacia numero más cercano arriba', e)
#%%
f = np.array(8.72)
g = np.floor(f)
print ('dato sin redondear', f)
print('dato redondeado hacia numero más cercano abajo', g)
#%%
p = matriz[0][2]
print(p)
#%%
f = matriz[1]
print (f)
#%%
d = np.shape(matriz)
print (d)
#%%
intervalo = np.arange(0, 81)
seno = np.sin(np.pi * 0.18 * intervalo)
#%%
senosoidal = np.cos(2 * np.pi * 0.03 * intervalo)
#%%
s1 = seno + senosoidal
s2 = seno * senosoidal
#%%
import matplotlib.pyplot as plt

plt.plot(intervalo, seno, label="Seno", color="blue")
plt.plot(intervalo, senosoidal, label="Senosoidal", color="red")
plt.legend()
plt.title("Señales seno y senosoidal")
plt.xlabel("intervalo")
plt.ylabel("Amplitud")
plt.show()
#%%
plt.plot(intervalo, s1, label="Señal 1", color="black")
plt.plot(intervalo, s2, label="Señal 2", color="orange")
plt.legend()
plt.title("Señales seno y senosoidal")
plt.xlabel("intervalo")
plt.ylabel("Amplitud")
plt.show()