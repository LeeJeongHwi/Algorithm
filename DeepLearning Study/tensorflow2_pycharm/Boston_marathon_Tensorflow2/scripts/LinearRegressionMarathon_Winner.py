import tensorflow as tf
import numpy as np
from tkinter import *
import tkinter.scrolledtext as tkst
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import pandas as pd

#pandas 가 컬럼타입을 동적으로 추론하는데에는 많은 메모리가 소요 된다.
marathon_2015_2017 = pd.read_csv("../source/marathon_2015_2017.csv")

record = pd.DataFrame(marathon_2015_2017,
                      columns=['5K', '10K', '15K', '20K', 'Half','25K','30K', '35K', '40K', 'Official Time']).sort_values(by=['Official Time'])

record_list = record.values.tolist()

xData = [5, 10, 15, 20, 21.098, 25, 30, 35, 40, 42.195]

fig = Figure(figsize=(6, 6), dpi=100)
ax = fig.add_subplot(111)
t_xdata, t_ydata, ml_xdata, ml_ydata, p_xdata, p_ydata = [], [], [], [], [], []
#t_xydata = training
#ml - learning Data
#p - Prediction Data
# Record Of runner Graph
ax.set_xlim(0, 45)  # X값 제한
ax.set_ylim(0, 13000)
ax.set_xlabel("Distance(km)")
ax.set_ylabel("Time(Second)")
ax.set_title("Records of Runner")
ln, = ax.plot([], [], linestyle=':')
dn, = ax.plot([],[],'ro') #red Circle Dot으로 표현
pn, = ax.plot([],[],'bs') #blue Square Dot
t_a = 0

# Gradient Descent Graph
grad_fig = Figure(figsize=(6,6),dpi=100)
grad_ax = grad_fig.add_subplot(111)
grad_ax.set_xlim(0,5000)
grad_ax.set_ylim(0,50000)
grad_ax.set_title("Cost Gradient Descent")
grad_ax.set_xlabel("Number of Training")
grad_ax.set_ylabel("Totla cost")
g_xdata,g_ydata=[],[]
gn, = grad_ax.plot([],[],'ro')

#seconds 값을 hh:mm:ss 형태로 변환하는 함수
def seconds_to_hhmmss(seconds):
    seconds
    hours=seconds//(60*60)
    seconds %=(60*60)
    minutes = seconds//60
    seconds %= 60
    return "%02i:%02i:%02i"%(hours,minutes,seconds)

#초기화 함수 (Update)에서 사용 - Get History Button
def init():
    t_a = int(t_aSpbox.get())-1
    ax.set_title("Record of Runner #"+str(t_a+1))
    ax.set_xlim(0,45)
    ax.set_ylim(0,13000)
    grad_ax.set_xlim(0,5000)
    grad_ax.set_ylim(0,50000)
    return dn,

#Rank of Runner Red circle Dot 찍는 애니메이션 - Get History Button
def animateFrame(frame):
    t_a = int(t_aSpbox.get())-1
    t_x = xData[int(frame)]
    t_y = record_list[t_a][int(frame)]
    t_xdata.append(t_x)
    t_ydata.append(t_y)
    dn.set_data(t_xdata,t_ydata)
    ax.annotate(seconds_to_hhmmss(t_y), (t_x,t_y), fontsize=8)
    fig.canvas.draw()
    return dn,

def update():
    t_xdata.clear()
    t_ydata.clear()
    #animation
    ani = FuncAnimation(fig,animateFrame,frames=np.linspace(0,len(xData)-1,len(xData)),
                        init_func=init,blit=True,repeat=False)
    fig.canvas.draw()
def draw_hypothesis(w,b):

    #clear Line
    ml_xdata.clear()
    ml_ydata.clear()
    #clear Prediction
    p_xdata.clear()
    p_ydata.clear()

    x_value =[i/10 for i in xData]
    for x in range(10):
        h= w*x_value[x] +b
        ml_xdata.append(xData[x])
        ml_ydata.append(h)
    ln.set_data(ml_xdata,ml_ydata)
    b_exp =''
    if b>0:
        b_exp = '+' + str(b)
    elif b < 0:
        b_exp ='-'+str(abs(b))
    log_ScrolledText.insert(END,"Hypothesis =X "+str(w)+b_exp+'\n',"RESULT")

def learning():
    t_a = int(t_aSpbox.get())
    t_t = int(t_tSpbox.get())
    t_r = float(t_rSpbox.get())

    x_train = [i/10 for i in xData[0:7]]
    y_train = record_list[t_a-1][0:7]

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(1,input_dim=1)) # (output_dim, input_dim)

    sgd = tf.keras.optimizers.SGD(lr=t_r)
    model.compile(loss='mse',optimizer=sgd)

    model.summary() #구조파악

    history = model.fit(x_train,y_train,epochs=t_t,batch_size = 128)

    log_ScrolledText.insert(END,'\n\n')
    log_ScrolledText.insert(END,"%10s %4i %10s %6i %20s %10.8f"%
                            ("Runner # ",t_a,", No. of train is",t_t,',learning rate is,',t_r)+'\n',"TITLE")
    log_ScrolledText.insert(END, '\n\nCost Decent\n\n','HEADER')
    log_ScrolledText.insert(END, "%20s %20s" % ('Step','Cost')+'\n\n')
    for step in range(t_t):
        if step%100 == 0: # 100번마다 찍을꺼야!
            cost_val = history.history['loss'][step]
            g_xdata.append(step)
            g_ydata.append(cost_val)
            log_ScrolledText.insert(END, '%20i %20.5f'%(step,cost_val)+'\n')
    #Drawing Graph
    grad_ax.plot(g_xdata,g_ydata,'ro')
    grad_ax.set_title("The minimum cost is %10.3f at %5i times"%(cost_val,step))
    grad_fig.canvas.draw()

    #Hypothesis
    W_val = model.layers[0].get_weights()[0][0]
    b_val = model.layers[0].get_weights()[1]
    log_ScrolledText.insert(END,"%20s"%('\n\nHypothesis = X * W + b'),'HEADER')
    draw_hypothesis(W_val,b_val)


    log_ScrolledText.insert(END,'%20s'%("\n\nRecords Prediction\n\n"),'HEADER')
    log_ScrolledText.insert(END,'%20s %20s %20s %20s'% ("Distnace(km)","Real Record","ML Prediction","Variation(Second)")+'\n\n')
    for index in range(7,10):
        x_value = xData[index]/10
        p_xdata.append(xData[index])
        time= model.predict(np.array([x_value]))
        p_ydata.append(time[0][0])
        log_ScrolledText.insert(END,"%20.3f %20s %20s %20i"%(xData[index],
                                                             seconds_to_hhmmss(t_ydata[index]),
                                                             seconds_to_hhmmss(time[0][0]),
                                                            (t_ydata[index]-time[0][0]))+'\n')
    #Get history --> Machine Training 을 해야 t_ydata에 데이터가 들어간다

    dn.set_data(t_xdata,t_ydata)
    pn.set_data(p_xdata,p_ydata)
    fig.canvas.draw()

#main 함수
main = Tk()
main.title("Marathon Records")
main.geometry() #창 생성
#Main Title
label = Label(main,text="Marathon Records Prediction by Machine Learning") #title글
label.config(font=("Courier",18))
label.grid(row=0,column=0,columnspan=6)
#grid 설정 - grid 설정한 순서로 우선배치 , 셀 단위 배치, 여러셀 건너뛰어 배치 X

#Rank_of_runner spinbox 설정
t_aVal = IntVar(value=1) #intVal은 spinbox에서 받는 값 (1은 초기값)
t_aSpbox = Spinbox(main,textvariable=t_aVal,from_=0,to=len(record_list),increment=1,justify = RIGHT)
#spinbox는 숫자돌림판? 느낌 from (default) / to (max) / increment(증가수치)
t_aSpbox.grid(row=1,column=1)
t_aLabel = Label(main,text='Rank of Runner : ')
t_aLabel.grid(row=1,column=0)

#Number of Train
t_tVal = IntVar(value = 5000)
t_tSpbox = Spinbox(main, textvariable=t_tVal, from_=0, to = 100000, increment=1000,justify= RIGHT)
t_tSpbox.grid(row=1,column=3)
t_tLabel = Label(main,text='Number of train: ')
t_tLabel.grid(row=1,column=2)

#Learning Rate
t_rVal = DoubleVar(value = 0.010)
t_rSpbox = Spinbox(main,textvariable=t_rVal,from_=0,to = 1, increment = 0.001,justify = RIGHT)
t_rSpbox.grid(row=1,column=5)
t_rLabel = Label(main,text='Learning Rate:')
t_rLabel.grid(row=1,column=4)

#Button
Button(main,text='Get History',height=2,command=lambda : update()).grid(row=2,column=0,columnspan=3,sticky=(W,E))
Button(main,text='Machine Learning',height=2,command=lambda : learning()).grid(row=2,column=3,columnspan=3,sticky=(W,E))

#record of Runner Canvas
canvas = FigureCanvasTkAgg(fig,main) #MatplotLib + TKinter 그래프 그리는 도구
canvas.get_tk_widget().grid(row=3,column=0,columnspan=3)

grad_canvas = FigureCanvasTkAgg(grad_fig,main) #
grad_canvas.get_tk_widget().grid(row=3,column=3,columnspan=3)

log_ScrolledText = tkst.ScrolledText(main,height=15)
log_ScrolledText.grid(row=4,column=0,columnspan=6,sticky=(N,S,W,E))
log_ScrolledText.configure(font='TkFixedFont')
log_ScrolledText.tag_config("RESULT", foreground='blue', font=('Helvetica',12))
log_ScrolledText.tag_config("HEADER", foreground='gray', font=('Helvetica', 14),underline=1)
log_ScrolledText.tag_config("TITLE", foreground='orange', font=('Helvetica', 18),underline=1,justify='center')

main.mainloop()
