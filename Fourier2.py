


import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

#dados
Vm = 220*np.sqrt(2)
alfa= 1.0472

def fourierSeries(valor_y, N, t,w, T): #Calcula os valores de an e bn
    result = []
    for n in range(N+1):
        an = 2/T*(integrate.simps(valor_y * np.cos(n*w*t),t))
        bn = 2/T*(integrate.simps(valor_y * np.sin(n*w*t),t))
        result.append((an, bn))
    return np.array(result)


def Fourier(anbn, t,w): #Função de fourier para o intervalo
    result = 0
    for n, (a, b) in enumerate(anbn):
        if n == 0:
            a = a/2
        result = result + a *np.cos(n*w*t) + b * np.sin(n*w*t)
    return result

t = np.linspace(0,2*np.pi,1500) #T -> W*T t vai de 0 a 2pi com 1500 pontos entre eles
ww = 2*np.pi/np.pi

Vt=[]


for u in t:

    if alfa < u < np.pi:
        Vt.append(Vm*np.sin(u))
    else:
        Vt.append(0)

print(Vt)

AnBn20 = fourierSeries(Vt,20,t,2,np.pi) #calculo de a20b20
print(AnBn20)
Fourier_Tensao = Fourier(AnBn20, t,2) #fourier para valores de ordem 20
plt.plot(t,Fourier_Tensao,'r', label = 'Fourier N=20')
plt.plot(t,Vt,'k')
plt.legend()
plt.xlabel('wt')
plt.ylabel('Tensão de saída na Carga (V)')
plt.show()



