import tensorflow as tf
import pandas as pd
from tkinter import *
import tkinter.scrolledtext as tkst
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import math
import numpy as np

marathon_2015_2017_qualifying = pd.read_csv('../source/marathon_2015_2017_qualifying.csv')
marathon_2015_2017_qualifying['Grade']=1
statistics_2015_2017 = marathon_2015_2017_qualifying['Official Time'].describe()

marathon_2015_2017_qualifying.loc[marathon_2015_2017_qualifying['Official Time'] < statistics_2015_2017['25%'],'Grade']=0
marathon_2015_2017_qualifying.loc[marathon_2015_2017_qualifying['Official Time'] > statistics_2015_2017['75%'],'Grade']=2

marathon_2015_2016 = marathon_2015_2017_qualifying[marathon_2015_2017_qualifying['Year']!=2017]
marathon_2017 = marathon_2015_2017_qualifying[marathon_2015_2017_qualifying['Year']==2017]

df_2015_2016= pd.DataFrame(marathon_2015_2016,columns=['M/F','Age','Pace','Grade'])
df_2017 = pd.DataFrame(marathon_2017,columns=['M/F','Age','Pace','Grade'])

record_2015_2016 = df_2015_2016.values.tolist()
record_2017 = df_2017.values.tolist()

gender_list = ["Female","Male"]
grade_list= ['Outstanding(>25%)','Average(25~75%)','Below(<75%)']

grad_fig = Figure(figsize=(10,6),dpi=100)
grad_ax = grad_fig.add_subplot(111)
grad_ax.set_xlim(15,88)
grad_ax.set_ylim(0,1300)
grad_ax.set_ylabel("Pace")
grad_ax.set_xlabel("Age")

def seconds_to_hhmmss(seconds):
    hours = seconds//(60*60)
    seconds %= (60*60)
    minutes = seconds//60
    seconds %= 60
    return "%02i:%02i:%02i"%(hours,minutes,seconds)
def normalization(record):
    #scale의 크기를 맞춰주는 것
    r0 = record[0]
    r1 = record[1] / 10
    r2 = record[2] / 100
    return [r0,r1,r2]

x_train = [normalization(r[0:3]) for r in record_2015_2016]
y_train = [ [r[-1]] for r in record_2015_2016]
x_test = [r[0:3] for r in record_2017]
y_test = [[r[-1]] for r in record_2017]

def histogram():
    t_a = int(t_aSpbox.get())-1
    runner = x_test[t_a]
    t_g = int(runner[0])
    t_y = int(runner[1])
    t_p = int(runner[2])
    if t_g:
        gender_color = 'b'
    else:
        gender_color = 'r'
    gender_record = df_2017[df_2017['M/F']==t_g]
    gender_age_record = gender_record[gender_record.Age==t_y]
    gender_age_record_list = gender_age_record.values.tolist()

    grad_ax.plot(gender_record.Age, gender_record.Pace, '.', color=gender_color, alpha=0.5)
    grad_ax.plot(t_y, t_p, "yd")
    stat = gender_age_record['Pace'].describe()
    print(stat)
    title = 'Gender :'+gender_list[t_g]+', Age : '+str(t_y)+', Pace : '+str(t_p)
    grad_ax.set_title(title)
    grad_ax.annotate('['+gender_list[t_g]+', '+str(t_y)+']',(75, 1200), fontsize=10)
    grad_ax.annotate('%10s %7i'%('Count : ',stat[0]),(75, 1150), fontsize=10)
    grad_ax.annotate('%10s %7.3f'%('Mean : ',stat[1]),(75, 1100), fontsize=10)
    grad_ax.annotate('%10s %7.3f'%('25% : ',stat[3]),(75, 1050), fontsize=10)
    grad_ax.annotate('%10s %7.3f'%('75% : ',stat[5]),(75, 1000), fontsize=10)
    grad_fig.canvas.draw()

nb_classes = 3 # 0,1,2 로 classification을 하기 때문에
def learning():
    import numpy as np
    t_a = int(t_aSpbox.get())-1
    runner = x_test[t_a]
    t_g = int(runner[0])
    t_y = int(runner[1])
    t_p = int(runner[2])

    t_t = int(t_tSpbox.get())
    t_r = float(t_rSpbox.get())

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(nb_classes,input_shape=(3,),activation='sigmoid'))
    sgd= tf.keras.optimizers.SGD(lr=t_r)
    #multinomial할때에는 Categorical Crossentropy 를 써야한다.
    model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])
    model.summary()
    #Y_Train을 One Hot으로 만듬
    y_one_hot = tf.keras.utils.to_categorical(y_train)
    history = model.fit(np.array(x_train),np.array(y_one_hot),epochs=t_t)
    log_ScrolledText.insert(END, '\nGender :' + gender_list[t_g] + ', Age :' + str(t_a) + ', Pace :' + str(t_p) + '\n',
                            'TITLE')
    log_ScrolledText.insert(END, '\n\nCost Decent\n\n', 'HEADER')
    log_ScrolledText.insert(END, "%20s %20s %20s" % ('Step', 'Cost',"Accuracy(%)")+ '\n\n')
    for step in range(t_t):
        if step%100==0:
            cost_val = history.history['loss'][step]
            a_val = history.history['accuracy'][step]
            log_ScrolledText.insert(END, "%20i %20.5f %20.7f" % (step, cost_val,a_val) + '\n')

    winner = normalization([t_g,t_y,t_p])
    result = model.predict(np.array([normalization(winner)])) #one Hot으로 나옴
                            #해당하는 인덱스가 나옴
    grade_index = model.predict_classes(np.array([winner]))
    grade = grade_list[grade_index[0]]
    log_ScrolledText.insert(END,'\n\n')
    log_ScrolledText.insert(END,'%10s %20s'%('Value      ','Qualifying Prediction\n\n'),"HEADER")
    if (grade_index[0]):
        log_ScrolledText.insert(END,'%30s'%(grade+'\n\n'),'DisQualifier')
    else:
        log_ScrolledText.insert(END, "%30s"%(grade+'\n\n'),'Qualifier')


main = Tk()
main.title("Marathon Records")
main.geometry()
# 제목 라벨 설정
label = Label(main, text='Multi Variable Linear Regression Concept')
label.config(font=('Courier', 18))
label.grid(row=0, column=0, columnspan=4)

# Rank Spin Box
t_aVal = IntVar(value=1)
t_aSpbox = Spinbox(main, textvariable=t_aVal, from_=18, to=84, increment=1, justify=RIGHT)
t_aSpbox.grid(row=1, column=1)
t_aLabel = Label(main, text='Rank of Runner : ')
t_aLabel.grid(row=1, column=0)
# Training Spin Box
t_tVal = IntVar(value=2000)
t_tSpbox = Spinbox(main, textvariable=t_tVal, from_=0, to=100000, increment=1000, justify=RIGHT)
t_tSpbox.grid(row=1, column=3)
t_tLabel = Label(main, text="Number of Train : ")
t_tLabel.grid(row=1, column=2)
# Learning Rate Spin box
t_rVal = DoubleVar(value=1e-2)
t_rSpbox = Spinbox(main, textvariable=t_rVal, from_=0, to=1, increment=1e-6, justify=RIGHT)
t_rSpbox.grid(row=1, column=5)
t_rLabel = Label(main, text='Learning Rate : ')
t_rLabel.grid(row=1, column=4)
# Histogram,Learning Button
Button(main, text='Histogram', height=2, command=lambda: histogram()).grid(row=2, column=0, columnspan=3,
                                                                           sticky=(W, E))
Button(main, text='Prediction', height=2, command=lambda: learning()).grid(row=2, column=3, columnspan=3,
                                                                           sticky=(W, E))

grad_canvas = FigureCanvasTkAgg(grad_fig, main)
grad_canvas.get_tk_widget().grid(row=3, column=0, columnspan=4, sticky=(N, S, W, E))

log_ScrolledText = tkst.ScrolledText(main, height=15)
log_ScrolledText.grid(row=4, column=0, columnspan=4, sticky=(N, S, W, E))
log_ScrolledText.tag_config("Qualifier", foreground='blue', font=('Helvetica', 12))
log_ScrolledText.tag_config("DisQualifier", foreground='red', font=('Helvetica', 12))
log_ScrolledText.tag_config("HEADER", foreground='gray', font=('Helvetica', 14), underline=1)
log_ScrolledText.tag_config("TITLE", foreground='orange', font=('Helvetica', 18), underline=1)

main.mainloop()