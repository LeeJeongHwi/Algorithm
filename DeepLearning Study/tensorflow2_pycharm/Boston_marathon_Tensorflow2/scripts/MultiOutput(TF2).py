import tensorflow as tf
import pandas as pd
from tkinter import *
from tkinter import ttk
import numpy as np
import tkinter.scrolledtext as tkst
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import math

marathon_2015_2017 = pd.read_csv("../source/marathon_2015_2017.csv")
marathon_2015_2017['M/F'] = marathon_2015_2017['M/F'].map({'M':1,'F':0})

marathon_2015_2016 = marathon_2015_2017[marathon_2015_2017['Year']!=2017]
marathon_2017 = marathon_2015_2017[marathon_2015_2017['Year']==2017]

df_2015_2016 = pd.DataFrame(marathon_2015_2016,columns=['M/F','Age','Pace',
                                                        '10K','20K','30K',
                                                        'Official Time']).sort_values(by=['Official Time'])
df_2017 = pd.DataFrame(marathon_2017,columns=['M/F','Age','Pace',
                                              '10K','20K','30K',
                                              'Official Time']).sort_values(by=['Official Time'])

record_2015_2016 = df_2015_2016.values.tolist()
record_2017 = df_2017.values.tolist()

x_train = [r[0:3] for r in record_2015_2016]  # M/F,Age,Pace 정보
y_train = [r[3:7] for r in record_2015_2016]

x_test = [r[0:3] for r in record_2017]
y_test = [r[3:7] for r in record_2017]

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
    t_a= int(t_aSpbox.get())-1
    runner = x_test[t_a]
    t_g = int(runner[0])
    t_y = int(runner[1])
    t_p = int(runner[2])
    if(t_g):
        gender_color='b'
    else:
        gender_color='r'
    #t_gCbbox 에 해당하는 gender의 데이터를 뽑아냄
    gender_record = df_2017[df_2017['M/F']==t_g]
    gender_age_record = gender_record[gender_record.Age==t_y]
    gender_age_record_list= gender_age_record.values.tolist()

    grad_ax.plot(gender_record.Age,gender_record.Pace,'.',color=gender_color,alpha=0.5)
    grad_ax.plot(t_g,t_p,'yd') #Yellow Circle Dot
    stat = gender_age_record['Pace'].describe()
    print(stat)
    title = 'Gender :'+gender_list[t_g]+', Age : '+str(t_y)
    grad_ax.set_title(title)
    grad_ax.annotate("%10s %7i" %('Count : ',stat[0]),(75,1200),fontsize=10)
    grad_ax.annotate("%10s %7.3f" %('Mean : ',stat[1]),(75,1150),fontsize=10)
    grad_ax.annotate("%10s %7.3f" %('25% : ',stat[3]),(75,1100),fontsize=10)
    grad_ax.annotate("%10s %7.3f" %('75% : ',stat[5]),(75,1050),fontsize=10)

    grad_fig.canvas.draw()

def learning():
    t_a= int(t_aSpbox.get())-1
    runner = x_test[t_a]
    t_g = int(runner[0])
    t_y = int(runner[1])
    t_p = int(runner[2])
    t_t = int(t_tSpbox.get())+1
    t_r = float(t_rSpbox.get())
    #DATA

    model = tf.keras.models.Sequential()
    #아웃풋을 4개로 내는 것 (output,input
    model.add(tf.keras.layers.Dense(4,input_layer=[3,]))

    sgd = tf.keras.optimizers.SGD(lr=t_r)
    model.compile(loss='mse',optimizer=sgd)
    model.summary()
    history = model.fit(np.array(x_train),np.array(y_train),epochs=t_t)

    log_ScrolledText.insert(END, '\nGender :'+gender_list[t_g]+', Age :'+str(t_y)+', Pace :'+str(t_p)+'\n', 'TITLE')
    log_ScrolledText.insert(END, '\n\nCost Decent\n\n','HEADER')
    log_ScrolledText.insert(END, "%20s %20s" % ('Step', 'Cost')+'\n\n')
    for step in range(t_t):
        if step % 100 == 0:
            cost_val = history.history['loss'][step]
            log_ScrolledText.insert(END, "%20i %20.5f" % (step,cost_val)+'\n')

    winner = [t_g, t_y, t_p] #1등 기록
    time = model.predict(np.array([winner]))
    log_ScrolledText.insert(END, "%20s" % ('\n\nThe Prediction Records\n\n'), 'HEADER')
    log_ScrolledText.insert(END, "%20s %30s %30s %20s" % ('Distance', 'Real Record', 'ML Prediction', 'Variation') + '\n\n')
    distance = [10.,20.,30.,42.195]
    for i in range(len(time[0])):
        dist_time = int(time[0][i])
        real_timne = seconds_to_hhmmss(y_test[t_a][i]) + '(' + str(y_test[t_a][i]) + ')'
        ml_time = seconds_to_hhmmss(dist_time) + '(' + str(dist_time) + ')'
        variation = y_test[t_a][i] - dist_time
        log_ScrolledText.insert(END, "%20.3f %30s %30s %20.3f" % (distance[i],real_timne, ml_time,variation) + '\n')


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
t_aVal = IntVar(value=1)
t_aSpbox = Spinbox(main,textvariable=t_aVal,from_=1, to =5000, increment=1,justify=RIGHT)
t_aSpbox.grid(row=1,column=3)
t_aLabel = Label(main,text='Rank Of Runner : ')
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