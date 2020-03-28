import tensorflow.compat.v1 as tf
import pandas as pd
from tkinter import *
from tkinter import ttk
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

gender_list = ['Female','Male']
grad_fig = Figure(figsize=(6,6),dpi=100)
grad_ax = grad_fig.add_subplot(111)
grad_ax.set_xlim(15,88) #Age
grad_ax.set_ylim(0,1300) #Pace
grad_ax.set_title("Cost Gradient Descent")
grad_ax.set_ylabel("Pace : Runner's overall minute per mile pace")
grad_ax.set_xlabel("Age : Age on Race Day")
g_xdata,g_ydata = [],[]
gn, = grad_ax.plot([],[],'ro')

def seconds_to_hhmmss(seconds):
    hours = seconds//(60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i"%(hours,minutes,seconds)
#TensorFlow 1
def histogram():
    gender = t_gCbbox.get()
    t_g = int(gender_list.index(gender))
    t_a = int(t_aSpbox.get())
    t_p = int(t_pSpbox.get())
    if(t_g):
        gender_color='b'
    else:
        gender_color='r'
    #t_gCbbox 에 해당하는 gender의 데이터를 뽑아냄
    gender_record = record[record['M/F']==t_g]
    gender_age_record = gender_record[gender_record.Age==t_a-1]
    gender_age_record_list= gender_age_record.values.tolist()

    grad_ax.plot(gender_record.Age,gender_record.Pace,'.',color=gender_color,alpha=0.5)
    grad_ax.plot(t_a,t_p,'yd') #Yellow Circle Dot
    stat = gender_age_record['Pace'].describe()
    print(stat)
    title = 'Gender :'+gender_list[t_g]+', Age : '+str(t_a)
    grad_ax.set_title(title)
    grad_ax.annotate("%10s %7i" %('Count : ',stat[0]),(75,1200),fontsize=10)
    grad_ax.annotate("%10s %7.3f" %('Mean : ',stat[1]),(75,1150),fontsize=10)
    grad_ax.annotate("%10s %7.3f" %('25% : ',stat[3]),(75,1100),fontsize=10)
    grad_ax.annotate("%10s %7.3f" %('75% : ',stat[5]),(75,1050),fontsize=10)

    grad_fig.canvas.draw()

def learning():
    gender = t_gCbbox.get()
    t_g = int(gender_list.index(gender))
    t_a = int(t_aSpbox.get())
    t_p = int(t_pSpbox.get())
    t_t = int(t_tSpbox.get())+1
    t_r = float(t_rSpbox.get())
    #DATA
    x_train = [r[0:3] for r in record_list] # M/F,Age,Pace 정보
    y_train = [[r[-1]] for r in record_list]

    w= tf.Variable(tf.random_normal([3,1]),name='weight1')
    b = tf.Variable(tf.random_normal([1]),name='bias')

    x = tf.placeholder(tf.float32, shape=[None,3])
    Y = tf.placeholder(tf.float32, shape=[None,1])
    hypothesis = tf.matmul(x, w) + b
    cost = tf.reduce_mean(tf.square(hypothesis-Y))
    train = tf.train.GradientDescentOptimizer(learning_rate=t_r).minimize(cost)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        log_ScrolledText.insert(END, '\nGender :'+gender_list[t_g]+', Age :'+str(t_a)+', Pace :'+str(t_p)+'\n', 'TITLE')
        log_ScrolledText.insert(END, '\n\nCost Decent\n\n','HEADER')
        log_ScrolledText.insert(END, "%20s %20s" % ('Step', 'Cost')+'\n\n')
        for step in range(t_t):
            _,cost_val,h_val = sess.run([train,cost,hypothesis],feed_dict={x:x_train,Y:y_train})
            if step % 100 == 0:
                print(step,cost_val,h_val[0])
                log_ScrolledText.insert(END, "%20i %20.5f" % (step,cost_val)+'\n')

        winner = [t_g, t_a, t_p] #1등 기록
        time = sess.run(hypothesis,feed_dict={x:[winner]})
        ml_time = seconds_to_hhmmss(time[0][0])+'('+str(time[0][0])+')'
        log_ScrolledText.insert(END, "%20s" % ('\n\nThe Prediction Records\n\n'), 'HEADER')
        log_ScrolledText.insert(END, "%10s %10s %10s %50s" % ('Gender', 'Age', 'Pace', 'Record Prediction(Second) at 42.195km') + '\n\n')
        log_ScrolledText.insert(END, "%10s %10s %10s %50s" % (gender_list[t_g], str(t_a), str(t_p), ml_time) + '\n')


main = Tk()
main.title("Marathon Records")
main.geometry()
#제목 라벨 설정
label=Label(main,text='Multi Variable Linear Regression Concept')
label.config(font=('Courier',18))
label.grid(row=0,column=0,columnspan=4)

#Gender Check Box
t_gVal = StringVar(value=gender_list[0])
t_gCbbox = ttk.Combobox(main,textvariable=t_gVal)
t_gCbbox['values']=gender_list
t_gCbbox.config(state='readonly')
t_gCbbox.grid(row=1,column=1)
t_gLabel = Label(main,text='Gender : ')
t_gLabel.grid(row=1,column=0)
#Age Spin Box
t_aVal = IntVar(value=45)
t_aSpbox = Spinbox(main,textvariable=t_aVal,from_=18, to =84, increment=1,justify=RIGHT)
t_aSpbox.grid(row=1,column=3)
t_aLabel = Label(main,text='Age : ')
t_aLabel.grid(row=1,column=2)
#Pace Spin box
t_pVal = IntVar(value=500)
t_pSpbox = Spinbox(main,textvariable=t_pVal,from_=0, to =1500, increment=1,justify=RIGHT)
t_pSpbox.grid(row=1,column=5)
t_pLabel = Label(main,text='Pace : ')
t_pLabel.grid(row=1,column=4)
#Training Spin Box
t_tVal = IntVar(value = 2000)
t_tSpbox= Spinbox(main,textvariable=t_tVal,from_=0,to=100000,increment=1000,justify=RIGHT)
t_tSpbox.grid(row=2,column=1)
t_tLabel = Label(main,text= "Number of Train : ")
t_tLabel.grid(row=2,column=0)
#Learning Rate Spin box
t_rVal = DoubleVar(value = 1e-6)
t_rSpbox = Spinbox(main,textvariable=t_rVal,from_=0,to=1, increment=1e-6,justify=RIGHT)
t_rSpbox.grid(row=2,column=3)
t_rLabel = Label(main,text='Learning Rate : ')
t_rLabel.grid(row=2,column=2)
#Histogram,Learning Button
Button(main,text='Histogram',height=2,command=lambda:histogram()).grid(row=2,column=4,columnspan=1,sticky=(W,E))
Button(main,text='Prediction',height=2,command=lambda:learning()).grid(row=2,column=5,columnspan=1,sticky=(W,E))

grad_canvas = FigureCanvasTkAgg(grad_fig,main)
grad_canvas.get_tk_widget().grid(row=3,column=0,columnspan=6,sticky=(N,S,W,E))

log_ScrolledText = tkst.ScrolledText(main, height=15)
log_ScrolledText.grid(row=4,column=0,columnspan=6,sticky=(N,S,W,E))
log_ScrolledText.tag_config("RESULT",foreground='blue',font=('Helvetica',12))
log_ScrolledText.tag_config("HEADER",foreground='gray',font=('Helvetica',14),underline=1)
log_ScrolledText.tag_config("TITLE",foreground='orange',font=('Helvetica',18),underline=1)



main.mainloop()