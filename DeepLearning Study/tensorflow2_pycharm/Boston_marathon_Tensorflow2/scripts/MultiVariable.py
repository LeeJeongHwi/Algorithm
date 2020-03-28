import tensorflow.compat.v1 as tf
import pandas as pd
from tkinter import *
import numpy as np
import tkinter.scrolledtext as tkst
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import math
tf.disable_v2_behavior()

marathon_2015_2017 = pd.read_csv("../source/marathon_2015_2017.csv")

record = pd.DataFrame(marathon_2015_2017, columns=['M/F','Age','Pace',
                                                   '10K','20K','30K',
                                                   'Official Time']).sort_values(by=['Official Time'])
#'M' 을 1 로 , "F"를 0 으로 대체
record['M/F'] = record['M/F'].map({'M':1,'F':0})
#DF to List
record_list = record.values.tolist()

grad_fig = Figure(figsize=(6,6),dpi=100)
grad_ax = grad_fig.add_subplot(111)
grad_ax.set_xlim(0,2000)
grad_ax.set_ylim(0,10000)
grad_ax.set_title("Cost Gradient Descent")
grad_ax.set_ylabel("Total Cost")
grad_ax.set_xlabel("Number of Training")
g_xdata,g_ydata = [],[]
gn, = grad_ax.plot([],[],'ro')

def seconds_to_hhmmss(seconds):
    hours = seconds//(60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i"%(hours,minutes,seconds)
#TensorFlow 1
def learning():
    #Train of Number / Learning Rate
    t_t = int(t_tSpbox.get())+1
    t_r = float(t_rSpbox.get())
    #DATA
    x_train_1 = [r[0] for r in record_list] # M/F 정보
    x_train_2 = [r[1] for r in record_list] # AGE 정보
    x_train_3 = [r[2] for r in record_list] # PACE 정보
    y_train = [r[-1] for r in record_list] # Official Time

    w1= tf.Variable(tf.random_normal([1]),name='weight1')
    w2= tf.Variable(tf.random_normal([1]),name='weight2')
    w3= tf.Variable(tf.random_normal([1]),name='weight3')
    b = tf.Variable(tf.random_normal([1]),name='bias')

    x1 = tf.placeholder(tf.float32, shape=[None])
    x2 = tf.placeholder(tf.float32, shape=[None])
    x3 = tf.placeholder(tf.float32, shape=[None])
    Y = tf.placeholder(tf.float32, shape=[None])
    hypothesis = x1*w1+x2*w2+x3*w3 + b

    cost = tf.reduce_mean(tf.square(hypothesis-Y))
    train = tf.train.GradientDescentOptimizer(learning_rate=t_r).minimize(cost)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        log_ScrolledText.insert(END,"%10s %6i %20s %10.8f" % ('\nNo. of train is',(t_t-1),", Learning Rate is ",t_r)+'\n',"TITLE")
        log_ScrolledText.insert(END,"\n\nCost Descent\n\n","HEADER")
        log_ScrolledText.insert(END,"%20s %20s"%('Step',"Cost")+'\n\n')
        for step in range(t_t):
            _,cost_val,h_val = sess.run([train,cost,hypothesis],feed_dict={x1:x_train_1,x2:x_train_2,x3:x_train_3,Y:y_train})
            if step % 100 == 0:
                print(step,cost_val,h_val)
                g_xdata.append(step)
                g_ydata.append(cost_val)
                log_ScrolledText.insert(END, "%20i %20.5f" % (step,cost_val)+'\n')
        grad_ax.plot(g_xdata,g_ydata,'ro')
        grad_ax.set_title(("The minimum cost is",str(cost_val),'at',str(step),'times'))
        grad_fig.canvas.draw()

        winner = record_list[0] #1등 기록
        time = sess.run(hypothesis,feed_dict={x1:[winner[0]],x2:[winner[1]],x3:[winner[2]]})
        log_ScrolledText.insert(END,"%20s"%("\n\nThe Winner Records prediction\n\n"),"HEADER")
        log_ScrolledText.insert(END,"%20s %20s %20s"%("Real Record"
                                                      ,"Prediction"
                                                      ,"Variablation(Second)"+"\n\n"))
        log_ScrolledText.insert(END,"%20s %20s %20i"%(seconds_to_hhmmss(y_train[0]),
                                                      seconds_to_hhmmss(time[0]),
                                                      (y_train[0]-time[0]))+'\n')
main = Tk()
main.title("Marathon Records")
main.geometry()
#제목 라벨 설정
label=Label(main,text='Multi Variable Linear Regression Concept')
label.config(font=('Courier',18))
label.grid(row=0,column=0,columnspan=4)
#SpinBox 설정
t_tVal = IntVar(value = 2000)
t_tSpbox= Spinbox(main,textvariable=t_tVal,from_=0,to=100000,increment=1000,justify=RIGHT)
t_tSpbox.grid(row=1,column=1)
#t_tLabel
t_tLabel = Label(main,text= "Number of Train : ")
t_tLabel.grid(row=1,column=0)
#t_rSpingBox
t_rVal = DoubleVar(value = 1e-6)
t_rSpbox = Spinbox(main,textvariable=t_rVal,from_=0,to=1, increment=1e-6,justify=RIGHT)
t_rSpbox.grid(row=1,column=3)
t_rLabel = Label(main,text='Learning Rate : ')
t_rLabel.grid(row=1,column=2)

Button(main,text='Learning',height=2,command=lambda:learning()).grid(row=2,column=0,columnspan=4,sticky=(W,E))

grad_canvas = FigureCanvasTkAgg(grad_fig,main)
grad_canvas.get_tk_widget().grid(row=3,column=0,columnspan=4,sticky=(N,S,W,E))

log_ScrolledText = tkst.ScrolledText(main, height=15)
log_ScrolledText.grid(row=4,column=0,columnspan=4,sticky=(N,S,W,E))
log_ScrolledText.tag_config("RESULT",foreground='blue',font=('Helvetica',12))
log_ScrolledText.tag_config("HEADER",foreground='gray',font=('Helvetica',14),underline=1)
log_ScrolledText.tag_config("TITLE",foreground='orange',font=('Helvetica',18),underline=1)



main.mainloop()