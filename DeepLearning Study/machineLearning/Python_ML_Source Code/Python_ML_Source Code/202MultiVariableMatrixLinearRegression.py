import numpy as np
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as tkst
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import math
# Import pandas as a alias 'pd'
import pandas as pd

# Load the CSV files "marathon_results_2015 ~ 2017.csv" under "data" folder
marathon_2015_2017 = pd._______("./data/marathon_2015_2017.csv")

# Merge 2015, 2016 and 2017 files into marathon_2015_2017 file index by Official Time
record = pd.DataFrame(marathon_2015_2017,columns=['M/F',  'Age',  'Pace',  '10K', '20K',  '30K',  'Official Time']).sort_values(by=['Official Time'])

record['M/F'] = record[____].map({'M': 1, ___: _})
# Dataframe to List
record_list = record.values.tolist()

gender_list = ['Female', 'Male']
grad_fig = Figure(figsize=(10, 6), dpi=100)
grad_ax = grad_fig.add_subplot(111)
grad_ax.set_xlim(15, 88)
grad_ax.set_ylim(0, 1300)
grad_ax.set_ylabel("Pace : Runner's overall minute per mile pace")
grad_ax.set_xlabel("Age : Age on race day")
g_xdata, g_ydata = [], []
gn, = grad_ax.plot([], [], 'ro')

def seconds_to_hhmmss(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)

def histogram():
    gender = t_gCbbox.get()
    t_g = int(gender_list.index(gender)) 
    t_a = int(t_aSpbox.get())
    t_p = int(t_pSpbox.get())
    if(t_g):
        gender_color = 'b'
    else:
        gender_color = 'r'  
    gender_record = record[record['M/F'] == t_g]
    gender_age_record = gender_record[gender_record.Age == t_a-1] 
    gender_age_record_list = gender_age_record.values.tolist() 
    
    grad_ax.plot(gender_record.Age, gender_record.Pace, '.', color=gender_color, alpha=0.5)
    grad_ax.plot(t_a, t_p, 'yd')
    stat = gender_age_record['Pace'].describe()
    print(stat)
    title = 'Gender : '+gender_list[t_g]+', Age : '+str(t_a)
    grad_ax.set_title(title)
    grad_ax.annotate("%10s %7i" % ('Count : ', stat[0]), (75, 1200), fontsize=10)
    grad_ax.annotate("%10s %7.3f" % ('Mean :  ', stat[1]), (75, 1150), fontsize=10)
    grad_ax.annotate("%10s %7.3f" % ('25% :   ', stat[3]), (75, 1100), fontsize=10)
    grad_ax.annotate("%10s %7.3f" % ('75% :   ', stat[5]), (75, 1050), fontsize=10)
        
    grad_fig.canvas.draw()     

def learing(): 
    """
    MAchine Learning, Tensorflow 
    """
    # Tensorflow Linear Regression
    import _________ as tf
    tf.set_random_seed(777)  # for reproducibility

    gender = t_gCbbox.get()
    t_g = int(gender_list.index(gender))    
    t_a = int(t_aSpbox.get()) 
    t_p = int(t_pSpbox.get())

    t_t = int(t_tSpbox.get()) + 1
    t_r = float(t_rSpbox.get())
        
        
    # X and Y data from 0km to 30km 
    x_train = [ r[___] for r in record_list ]
    y_train = [ [r[__]] for r in record_list ]

    # Try to find values 
    W = tf.Variable(tf.random_normal([_, _]), name='weight')
    b = tf.Variable(tf.random_normal([_]), name="bias")
    
    # placeholders for a tensor 
    X = tf.placeholder(tf.float32, shape=[None, _])
    Y = tf.placeholder(tf.float32, shape=[None, _])
    
    # Our hypothesis 
    # hypothesis = X1 * W1 + X2 * W2 + X3 * W3 + b
    hypothesis = tf.______(_, _) + b

    # cost/loss function
    cost = tf.reduce_mean(tf.square(________ - Y))
    
    # optimizer
    train = tf.train.GradientDescentOptimizer(___________=t_r).minimize(____)
    
    # Launch a session.
    with tf._______() as sess:
        # Initializes global variables 
        sess.___(tf._____________________())

        # Fit the line
        #log_ScrolledText.insert(END, "%10s %6s %10s %3s %10s %5s" % ('\nGender :', gender_list[t_g], ', Age :', t_a, ', Pace :'+ t_p)+'\n', 'TITLE')
        log_ScrolledText.insert(END, '\nGender :'+gender_list[t_g]+', Age :'+str(t_a)+', Pace :'+str(t_p)+'\n', 'TITLE')
        log_ScrolledText.insert(END, '\n\nCost Decent\n\n','HEADER')
        log_ScrolledText.insert(END, "%20s %20s" % ('Step', 'Cost')+'\n\n')
        for step in range(t_t):
            _, cost_val, h_val = sess.run([train, cost,  __________], feed_dict={X: ________, Y: y_train})
    
            if step % 100 == 0:
                print(step, cost_val, h_val[0]) 
                log_ScrolledText.insert(END, "%20i %20.5f" % (step, cost_val)+'\n')

        # Testing our model
        winner = [ t_g, t_a, t_p ]
        time = sess.___(___________, feed_dict={X: [________]})
        ml_time = seconds_to_hhmmss(time[0][0]) + '(' + str(time[0][0]) + ')'
        # time = sess.run(hypothesis, feed_dict={X1: [1], X2: [25], X3: [296]})
        log_ScrolledText.insert(END, "%20s" % ('\n\nThe Prediction Records\n\n'), 'HEADER')
        log_ScrolledText.insert(END, "%10s %10s %10s %50s" % ('Gender', 'Age', 'Pace','Record Prediction(Second) at 42.195km')+'\n\n')
        log_ScrolledText.insert(END, "%10s %10s %10s %50s" % (gender_list[t_g], str(t_a), str(t_p), ml_time)+'\n') 
            
#main
main = Tk()
main.title("Multi Variable Matrix Linear Regression")
main.geometry()

label=Label(main, text='Multi Variable Matrix Linear Regression')
label.config(font=("Courier", 18))
label.grid(row=0,column=0,columnspan=6)

t_gVal  = StringVar(value=gender_list[0])
t_gCbbox = ttk.Combobox(main, textvariable=t_gVal)
t_gCbbox['values'] = gender_list
t_gCbbox.config(state='readonly')
t_gCbbox.grid(row=1,column=1)

t_gLabel=Label(main, text='Gender : ')                
t_gLabel.grid(row=1,column=0)

t_aVal  = IntVar(value=45)
t_aSpbox = Spinbox(main, textvariable=t_aVal ,from_=18, to=84, increment=1, justify=RIGHT)
#t_tSpbox.config(state='readonly')
t_aSpbox.grid(row=1,column=3)
t_aLabel=Label(main, text='Age : ')                
t_aLabel.grid(row=1,column=2)

t_pVal  = IntVar(value=500)
t_pSpbox = Spinbox(main, textvariable=t_pVal ,from_=0, to=1500, increment=1, justify=RIGHT)
#t_rSpbox.config(state='readonly')
t_pSpbox.grid(row=1,column=5)
t_pLabel=Label(main, text='Pace : ')                
t_pLabel.grid(row=1,column=4)


t_tVal  = IntVar(value=2000)
t_tSpbox = Spinbox(main, textvariable=t_tVal ,from_=0, to=100000, increment=1000, justify=RIGHT)
#t_tSpbox.config(state='readonly')
t_tSpbox.grid(row=2,column=1)
t_tLabel=Label(main, text='Number of train : ')                
t_tLabel.grid(row=2,column=0)

t_rVal  = DoubleVar(value=1e-6)
t_rSpbox = Spinbox(main, textvariable=t_rVal ,from_=0, to=1, increment=1e-6, justify=RIGHT)
#t_rSpbox.config(state='readonly')
t_rSpbox.grid(row=2,column=3)
t_rLabel=Label(main, text='Learning rate : ')                
t_rLabel.grid(row=2,column=2)

Button(main,text="Histogram", height=2,command=lambda:histogram()).grid(row=2, column=4, columnspan=1, sticky=(W, E))
Button(main,text="Prediction", height=2,command=lambda:learing()).grid(row=2, column=5, columnspan=1, sticky=(W, E))

grad_canvas = FigureCanvasTkAgg(grad_fig, main)
grad_canvas.get_tk_widget().grid(row=3,column=0,columnspan=6)

log_ScrolledText = tkst.ScrolledText(main, height=15)
log_ScrolledText.grid(row=4,column=0,columnspan=6, sticky=(N, S, W, E))
log_ScrolledText.configure(font='TkFixedFont')
log_ScrolledText.tag_config('RESULT', foreground='blue', font=("Helvetica", 12))
log_ScrolledText.tag_config('HEADER', foreground='gray', font=("Helvetica", 14), underline=1)
log_ScrolledText.tag_config('TITLE', foreground='orange', font=("Helvetica", 18), underline=1, justify='center')

main.mainloop()