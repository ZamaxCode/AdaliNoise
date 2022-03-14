import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import numpy as np
import threading
import time


def clean_noise():
    ax.cla()

    x = np.arange(0,100,0.1)
    y = np.sin(x/6)

    ax.plot(x,y, 'r') 
    
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

    x_ruido = np.arange(0,100,1)
    ax.plot(x_ruido,y_ruido, 'b')
    eta = float(eta_gui.get())
    a = float(a_gui.get())
    numX = int(x_gui.get())
    W = []
    for i in range(numX+1):
        W.append(random.random())

    y_fix = []
    for i in range(numX):
        y_fix.append(y_ruido[i])

    for i in range(len(y_ruido)):
        try:
            X=[]
            X.append(1)
            for j in range(i,i+numX):
                X.append(y_ruido[j])
            salida_y = np.dot(X,W)*a
            e = y_ruido[i+numX] - salida_y
            W = W + np.dot(eta*e*a,X)
            salida_y = np.dot(X,W)*a
            y_fix.append(salida_y)

            #ax.plot(i+numX, salida_y, '.g')
            #time.sleep(0.3)
        except:
            pass

    x_fix = np.arange(0, len(y_fix),1)
    ax.plot(x_fix, y_fix, 'g')
    plt.ylim(-2,2)
    canvas.draw()

fig, ax= plt.subplots(facecolor='#8D96DA')

mainwindow = Tk()
mainwindow.geometry('1200x600')
mainwindow.config(bg='#8D96DA')
mainwindow.wm_title('Perceptron')
#Creamos los valores de los pesos y humbral de activacion 

x = np.arange(0,100,0.1)
y = np.sin(x/6)

ax.plot(x,y, 'r') 

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

x_ruido = np.arange(0,100,1)
ax.plot(x_ruido,y_ruido, 'b') 

eta_gui = StringVar(mainwindow, 0)
a_gui = StringVar(mainwindow, 0)
x_gui = StringVar(mainwindow, 0)

#Colocamos la grafica en la interfaz
canvas = FigureCanvasTkAgg(fig, master = mainwindow)
canvas.get_tk_widget().place(x=10, y=10, width=1100, height=580)

NumX_label = Label(mainwindow, text = "Numero de X: ", bg='#8D96DA')
NumX_label.place(x=1050, y=90)

NumX_entry = Entry(mainwindow, textvariable=x_gui)
NumX_entry.place(x=1050, y=110)

Eta_label = Label(mainwindow, text = "Eta: ", bg='#8D96DA')
Eta_label.place(x=1050, y=140)

Eta_entry = Entry(mainwindow, textvariable=eta_gui)
Eta_entry.place(x=1050, y=160) 

a_label = Label(mainwindow, text = "A: ", bg='#8D96DA')
a_label.place(x=1050, y=190)

a_entry = Entry(mainwindow, textvariable=a_gui)
a_entry.place(x=1050, y=210)

start_button = Button(mainwindow, text="Go!", command=lambda:threading.Thread(target=clean_noise).start())
start_button.place(x=1050, y=290)

#Mostramos la interfaz
mainwindow.mainloop()
