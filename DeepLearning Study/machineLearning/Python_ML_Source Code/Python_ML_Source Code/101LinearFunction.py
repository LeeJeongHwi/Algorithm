"""
Chapter 1. 
"""
import numpy as np
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

MAXVAL = 10
INTERVAL = (MAXVAL*10) + 1

fig = Figure(figsize=(5,4), dpi=100)
ax = fig.add_subplot(111)
t_xdata, t_ydata, h_xdata, h_ydata = [], [], [], [] 

def update():
    t_a = float(t_aSpbox.get())
    t_b = float(t_bSpbox.get())
    h_a = float(h_aSpbox.get())    
    doMeet = False

    f = open("01LinearFunction_log.txt", "a")
    for t in np.linspace(0, MAXVAL, INTERVAL):
        t_y = t_a*t + t_b
        h_y = h_a*t
        t_xdata.append(t)
        t_ydata.append(t_y)
        h_xdata.append(t)
        h_ydata.append(h_y)
        if(h_y >= t_y and (not doMeet)):
            doMeet = True
            meetTime = t
            meetDistance = t_y
        # write entry value to file

        f.write("x: "+str(math.ceil(t*100)/100)+", t_y: "+str(math.ceil(t_y*100)/100)+", h_y: "+str(math.ceil(h_y*100)/100)+"\n")
        # print("t : "+str(math.ceil(t*100)/100)+", t_y: "+str(math.ceil(t_y*100)/100)+", h_y : "+str(math.ceil(h_y*100)/100)+", doMeet : "+str(doMeet))

    f.close()
    ax.set_xlabel('Time(hour)')
    ax.set_ylabel('Distance(km)')
    ax.plot(t_xdata,t_ydata, label='Tortoise')
    ax.plot(h_xdata,h_ydata, label='Hare')

    if (doMeet):
        ax.set_title('The tortoise overcome from '+str(math.ceil(meetTime*100)/100)+'hour(s), '+str(math.ceil(meetDistance*100)/100)+'km(s)')
        ax.plot(meetTime, meetDistance, 'ro')
    else:
        ax.set_title('They will not meet')
    ax.legend()
    fig.canvas.draw()

#main
main = Tk()
main.title("The Hare and the Tortoise")
main.geometry()

label=Label(main, text='The Hare and the Tortoise')
label.config(font=("Courier", 18))
label.grid(row=0,column=0,columnspan=4)

t_aVal  = DoubleVar(value=1.0)
t_bVal  = DoubleVar(value=4.0)
h_aVal  = DoubleVar(value=2.0)

t_aSpbox = Spinbox(main, textvariable=t_aVal ,from_=0, to=10, increment=1, justify=RIGHT)
t_aSpbox.config(state='readonly')
t_aSpbox.grid(row=1,column=1)
t_aLabel=Label(main, text='The tortoise (km/h) : ')                
t_aLabel.grid(row=1,column=0)

t_bSpbox = Spinbox(main, textvariable=t_bVal,from_=0, to=10, increment=1, justify=RIGHT)
t_bSpbox.config(state='readonly')
t_bSpbox.grid(row=2,column=1)
t_bLabel=Label(main, text='The tortoise (km) : ')                
t_bLabel.grid(row=2,column=0)

h_aSpbox = Spinbox(main, textvariable=h_aVal ,from_=0, to=10, increment=1, justify=RIGHT)
h_aSpbox.config(state='readonly')
h_aSpbox.grid(row=3,column=1)
h_aLabel=Label(main, text='The hare (km/h) : ')                
h_aLabel.grid(row=3,column=0)

Button(main,text="Run",width=20,height=5,command=lambda:update()).grid(row=1, column=2,columnspan=2, rowspan=3)

canvas = FigureCanvasTkAgg(fig, main)
canvas.get_tk_widget().grid(row=4,column=0,columnspan=3) 

# create initial blank file
f = open("01LinearFunction_log.txt", "w")
f.close()

main.mainloop()
