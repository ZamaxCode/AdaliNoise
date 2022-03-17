import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import numpy as np
import threading
import time

y_ruido = []
y_fix = []

def print_noisy_signal():
    ax.cla()
    x = np.arange(0,100,0.1)
    y = np.sin(x/6)
    ax.plot(x,y, 'r') 
    x_ruido = np.arange(0,100,1)
    ax.plot(x_ruido, y_ruido, 'b')
    canvas.draw()

def clean_noise():
    global y_ruido
    print_noisy_signal()
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

            time.sleep(0.1)
            ax2.cla()
            x = np.arange(0,100,0.1)
            y = np.sin(x/6)
            ax2.plot(x,y, 'r') 
            x_fix = np.arange(0, len(y_fix),1)
            ax2.plot(x_fix, y_fix, 'g')
            plt.ylim(-2,2) 
            canvas2.draw()
        except:
            pass
    ax.plot(x_fix, y_fix, 'g')
    canvas.draw()

fig, ax= plt.subplots(facecolor='#8D96DA')
plt.ylim(-2,2) 
fig2, ax2= plt.subplots(facecolor='#8D96DA')  
plt.ylim(-2,2)

mainwindow = Tk()
mainwindow.geometry('1200x900')
mainwindow.config(bg='#8D96DA')
mainwindow.wm_title('Perceptron')

with open("amplitud.txt") as f:
    lines = f.readlines()

for line in lines:
    y_ruido.append(float(line))

eta_gui = StringVar(mainwindow, 0)
a_gui = StringVar(mainwindow, 0)
x_gui = StringVar(mainwindow, 0)

#Colocamos la grafica en la interfaz
canvas = FigureCanvasTkAgg(fig, master = mainwindow)
canvas.get_tk_widget().place(x=-90, y=-40, width=1200, height=520)

canvas2 = FigureCanvasTkAgg(fig2, master = mainwindow)
canvas2.get_tk_widget().place(x=-90, y=428, width=1200, height=520)

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
start_button.place(x=1050, y=250)

print_noisy_signal()

#Mostramos la interfaz
mainwindow.mainloop()
