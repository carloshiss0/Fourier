import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

R = 10
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def fourierSeries(f, N, t, T, w):    
    result = []
    for n in range(N+1):
        an = 2/T*(integrate.simps(f * np.cos(n*w*t),t))
        bn = 2/T*(integrate.simps(f * np.sin(n*w*t),t))
        result.append((an, bn))
    return np.array(result)

def Fourier(anbn, t, w):   
    result = 0
    for n, (a, b) in enumerate(anbn):
        if n == 0:
            a = a/2
        result = result + a *np.cos(n*w*t) + b * np.sin(n*w*t)
    return result


w = 2*np.pi/10
t = np.linspace(-5,5,1500)  

Vt=[]

for u in t:
    if  -5<u<-4:
        Vt.append(2*u+10)
    elif -4 <u <-1:
        Vt.append(2)
    elif -1<u<0:
        Vt.append(-2*u)
    elif 0<u<1:
        Vt.append(1*u)
    elif 1<u<2:
        Vt.append(1)
    elif 2<u<3:
        Vt.append(-1*u+3)        
    else:
        Vt.append(0)
        
print(Vt)

AnBn20 = fourierSeries(Vt,20,t,10,2*np.pi/10)  #calculo de a100b100

print(AnBn20)
Fourier_Tensao = Fourier(AnBn20, t,2*np.pi/10) #fourier para valores de ordem 20
plt.plot(t,Fourier_Tensao,'r')
plt.plot(t,Vt,'k')
plt.legend()
plt.xlabel('wt')
plt.ylabel('Tensão de saída na Carga (V)')
plt.show()
