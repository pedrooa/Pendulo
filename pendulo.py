# ANGULO MAIOR
from scipy.integrate import odeint
import math
from numpy import arange
import matplotlib.pyplot as plt

def Eqdif(T,t):
    teta = T[0]
    w = T[1]
    g= 10  # gravidade
    l = 2 # comprimento do fio
    dtetadt = w
    dwdt = -g*math.sin(teta)/l
    return [dtetadt,dwdt]


teta0 = 32.97*math.pi/180  # transforma graus em radianos
T0 = [teta0,0]  # condicao inicial

t = 0  # tempo inicial
deltat = 0.0001  # variação de tempo
t = arange(t,30,deltat)  # tempo
sol = odeint(Eqdif,T0,t)

X = []
Y = []

for n in sol[:,0]:
    x = 2*math.sin(n)
    y = 2 - 2*math.cos(n)

    X.append(x)  # lista com as posicao em x
    Y.append(y)  #  lista posicao em y



plt.plot(X,Y)
plt.grid(True)
plt.xlabel("Eixo x(m)")
plt.ylabel("Eixo y(m)")
plt.title("Pêndulo")
plt.grid(True)
plt.show()

plt.plot(t,X)
plt.grid(True)
plt.xlabel("tempo(s)")
plt.ylabel("Eixo x(m)")
plt.title("x vs tempo")
plt.grid(True)
plt.show()

plt.plot(t,Y)
plt.grid(True)
plt.xlabel("tempo(s)")
plt.ylabel("Eixo y(m)")
plt.title("y vs tempo")
plt.grid(True)
plt.show()

plt.plot(t,sol[:,0]*180/math.pi)
plt.grid(True)
plt.xlabel("tempo")
plt.ylabel("angulo teta(em graus)")
plt.title("angulo  vs tempo")
plt.grid(True)
plt.show()




#ANGULO PEQUENO
def Eqdif(T,t):
    teta = T[0]
    w = T[1]
    g= 10  # gravidade
    l = 2 # comprimento do fio
    dtetadt = w
    dwdt = -g*math.sin(teta)/l

    return [dtetadt,dwdt]


teta0 =  4.25*math.pi/180  # transforma graus em radianos
T0 = [teta0,0]  # condicao inicial

t = 0
deltat = 0.0001  # 0.33
t = arange(t,10,deltat)  # tempo
sol = odeint(Eqdif,T0,t)

X = []
Y = []

for n in sol[:,0]:
    x = 2*math.sin(n)
    y = 2 - 2*math.cos(n)

    X.append(x)  # lista com as posicao em x
    Y.append(y)  #  lista posicao em y



plt.plot(X,Y)
plt.grid(True)
plt.xlabel("Eixo x(m)")
plt.ylabel("Eixo y(m)")
plt.title("Pêndulo")
plt.grid(True)
plt.show()

plt.plot(t,X)
plt.grid(True)
plt.xlabel("tempo(s)")
plt.ylabel("Eixo x(m)")
plt.title("x vs tempo")
plt.grid(True)
plt.show()

plt.plot(t,Y)
plt.grid(True)
plt.xlabel("tempo(s)")
plt.ylabel("Eixo y(m)")
plt.title("y vs tempo")
plt.grid(True)
plt.show()

plt.plot(t,sol[:,0]*180/math.pi)
plt.grid(True)
plt.xlabel("tempo(s)")
plt.ylabel("angulo teta(em graus)")
plt.title("angulo  vs tempo")
plt.grid(True)
plt.show()
