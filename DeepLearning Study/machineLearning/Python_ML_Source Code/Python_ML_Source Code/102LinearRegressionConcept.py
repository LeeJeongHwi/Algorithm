"""
Chapter 1. 
"""
import numpy as np
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import math

MAXVAL = 10
INTERVAL = MAXVAL + 1

fig = Figure(figsize=(5,4), dpi=100)
ax = fig.add_subplot(111)
h_xdata, h_ydata, x_list, y_list = [], [], [], []
ax.set_xlim(0, 11)
ax.set_ylim(0, 11)

grad_fig = Figure(figsize=(5,4), dpi=100)
grad_ax = grad_fig.add_subplot(111)
grad_ax.set_xlim(-0.1, 1.1)
grad_ax.set_ylim(0, 100)
t_xdata, t_ydata = [], []
ln, = grad_ax.plot(0, 0)
dn, = grad_ax.plot([], [], 'ro')

def update():
    h_a = int(h_aSpbox.get())    
    for t in np.linspace(0, MAXVAL, INTERVAL):
        h_y = h_a*t
        h_xdata.append(t)
        h_ydata.append(h_y)
    ax.set_xlabel('Time(hour)')
    ax.set_ylabel('Distance(km)')
    ax.set_title('Linear Regression')
    ax.plot(h_xdata,h_ydata, 'ro', label='Hare')
    ax.legend()
    fig.canvas.draw()

def get_cost(a_val):
    h_a = float(h_aSpbox.get()) 
    cost = 0
    for i in range(0, 11, 1):
        cost += pow((a_val*i - h_a*i),2)
    return cost

def showLines():
    h_a = float(h_aSpbox.get()) 
    h_s = float(h_sSpbox.get())  
    a_val = h_a + (h_s * 5) 
    h_xdata = []
    h_ydata = []
    for i in np.linspace(0, MAXVAL, INTERVAL):
        a = a_val - (i * h_s)
        for t in np.linspace(0, MAXVAL, INTERVAL):
            h_y = a*t
            h_xdata.append(t)
            h_ydata.append(h_y)
        ax.plot(h_xdata,h_ydata, alpha=0.2) 
    fig.canvas.draw()

def init():
    grad_ax.set_xlim(-0.1, 1.1)
    grad_ax.set_ylim(0, 100)
    return dn, ln, 

def animateFrame(frame):
    h_a = float(h_aSpbox.get()) 
    h_s = float(h_sSpbox.get())
    a_val = h_a + (h_s * 5) 
    i = frame * h_s
    a = a_val - i
    t_xdata.append(i)
    t_ydata.append(get_cost(a))
    dn.set_data(t_xdata, t_ydata)
    # ln.set_data(t_xdata, t_ydata)
    return dn, ln,

def gradient():
    ani = FuncAnimation(fig, animateFrame, frames=np.linspace(0, MAXVAL, INTERVAL),
                        init_func=init, blit=True)

    grad_ax.set_title('Gradient descent')
    grad_ax.set_ylabel("Total Cost")
    grad_ax.set_xlabel("Variance")

    grad_fig.canvas.draw()

#main
main = Tk()
main.title("The Hare Linear Regression")
main.geometry()

label=Label(main, text='The Hare Linear Regression')
label.config(font=("Courier", 18))
label.grid(row=0,column=0,columnspan=4)

h_aVal  = DoubleVar(value=1.0)

h_aSpbox = Spinbox(main, textvariable=h_aVal ,from_=0, to=10, increment=1, justify=RIGHT)
h_aSpbox.config(state='readonly')
h_aSpbox.grid(row=1,column=2)
h_aLabel=Label(main, text='The hare (km/h) : ')                
h_aLabel.grid(row=1,column=0,columnspan=2)

h_sVal  = DoubleVar(value=0.1)

h_sSpbox = Spinbox(main, textvariable=h_sVal ,from_=0, to=2, increment=0.01, justify=RIGHT)
h_sSpbox.config(state='readonly')
h_sSpbox.grid(row=2,column=2)
h_sLabel=Label(main, text='Velocity variance (km/h) : ')                
h_sLabel.grid(row=2,column=0,columnspan=2)

Button(main,text="Run",width=20,height=3,command=lambda:update()).grid(row=3, column=0)
Button(main,text="Lines",width=20,height=3,command=lambda:showLines()).grid(row=3, column=1)
Button(main,text="Gradient",width=20,height=3,command=lambda:gradient()).grid(row=3, column=2)

canvas = FigureCanvasTkAgg(fig, main)
canvas.get_tk_widget().grid(row=4,column=0,columnspan=4)

grad_canvas = FigureCanvasTkAgg(grad_fig, main)
grad_canvas.get_tk_widget().grid(row=5,column=0,columnspan=4) 

main.mainloop()
