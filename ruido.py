import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import numpy as np
import threading
import time

x = np.arange(0,201,0.1)
y = np.sin(x)

plt.plot(x,y, 'r') #señal limpia

pos_neg = True
y_ruido = []
i=0
while i < len(y):
    if pos_neg:
        y_ruido.append(y[i]+0.3)
        pos_neg = False
    else:
        y_ruido.append(y[i]-0.3)
        pos_neg = True
    i = i+10

x_ruido = np.arange(0,201,1)
#plt.plot(x_ruido,y_ruido, 'b') #señal con ruido

y_fix = []
eta = 0.3
w0 = random.random()
w1 = random.random()
w2= random.random()



y_fix.append(y_ruido[0])
y_fix.append(y_ruido[1])


for i in range(len(y_ruido)):
    try:
        W = [w0,w1,w2]
        X = [1,y_ruido[i],y_ruido[i+1]]
        salida_y = np.dot(X,W)*0.5
        e = y_ruido[i+4] - salida_y
        W = W + np.dot(eta*e*0.5,X)
        salida_y = np.dot(X,W)*0.5
        w0 = W[0]
        w1 = W[1]
        w2 = W[2]
        y_fix.append(salida_y)
    except:
        pass
print(y_fix)
x_fix = np.arange(0, len(y_fix),1)
plt.plot(x_fix, y_fix, 'g')
plt.ylim(-2,2)
plt.show()