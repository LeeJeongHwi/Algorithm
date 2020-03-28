import numpy as np
from tkinter import *
import tkinter.scrolledtext as tkst
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import math
# Import pandas as a alias 'pd'
import pandas as pd

# Load the CSV files "marathon_results_2015 ~ 2017.csv" under "data" folder
marathon_2015_2017_qualifying = pd.read_csv("./data/marathon_2015_2017_qualifying.csv")
marathon_2015_2017_qualifying["Grade"] = 1
statistics_2015_2017 = marathon_2015_2017_qualifying["Official Time"]._________

marathon_2015_2017_qualifying.loc[marathon_2015_2017_qualifying["Official Time"] < statistics_2015_2017["25%"], "Grade"] = 0
marathon_2015_2017_qualifying.loc[marathon_2015_2017_qualifying["Official Time"] > statistics_2015_2017["75%"], "Grade"] = 2
'''
count    79638.000000
mean     13989.929167
std       2492.272069
min       7757.000000
25%      12258.000000
50%      13592.000000
75%      15325.000000
max      37823.000000
Name: Official Time, dtype: float64
'''
marathon_2015_2016 = marathon_2015_2017_qualifying[marathon_2015_2017_qualifying['Year'] __ 2017]
marathon_2017 = marathon_2015_2017_qualifying[marathon_2015_2017_qualifying['Year'] __ 2017]

df_2015_2016 = pd.DataFrame(marathon_2015_2016,columns=['M/F',  'Age',  'Pace',  'Grade'])
df_2017 = pd.DataFrame(marathon_2017,columns=['M/F',  'Age',  'Pace',  'Grade'])

# Dataframe to List
record_2015_2016 = df_2015_2016.values.tolist()
record_2017 = df_2017.values.tolist()

nb_classes = 3  # 0 ~ 2
gender_list = ['Female', 'Male']
grade_list = ['Outstanding(>25%)', 'Average(25~75%)', 'Below(<75%)']

grad_fig = Figure(figsize=(10, 6), dpi=100)
grad_ax = grad_fig.add_subplot(111)
grad_ax.set_xlim(15, 88)
grad_ax.set_ylim(0, 1300)
grad_ax.set_ylabel("Pace : Runner's overall minute per mile pace")
grad_ax.set_xlabel("Age : Age on race day")

def seconds_to_hhmmss(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)

def normalization(record):
    r0 = record[0]
    r1 = record[1] / 10
    r2 = record[2] / 100
    return [r0, r1, r2]

# X and Y data 
x_train = [ normalization(r[___]) for r in record_2015_2016]
y_train = [ [r[__]] for r in record_2015_2016]
# x_test = [ r[0:3] for r in record_2017]
x_test = [ r[___] for r in record_2017]
y_test = [ [r[__]] for r in record_2017]

def histogram():
    t_a = int(t_aSpbox.get()) - 1
    runner = x_test[t_a]
    print(runner)
    t_g = int(runner[0])
    t_y = int(runner[1])
    t_p = int(runner[2])
    if(t_g):
        gender_color = 'b'
    else:
        gender_color = 'r'  
    gender_record = df_2017[df_2017['M/F'] == t_g]
    gender_age_record = gender_record[gender_record.Age == t_y] 
    gender_age_record_list = gender_age_record.values.tolist() 
    
    grad_ax.plot(gender_record.Age, gender_record.Pace, '.', color=gender_color, alpha=0.5)
    grad_ax.plot(t_y, t_p, 'yd')
    stat = gender_age_record['Pace'].describe()
    print(stat)
    title = 'Gender : '+gender_list[t_g]+', Age : '+str(t_y)+', Pace : '+str(t_p)
    grad_ax.set_title(title)
    grad_ax.annotate('['+gender_list[t_g]+', '+str(t_y)+']', (75, 1200), fontsize=10)
    grad_ax.annotate("%10s %7i" % ('Count : ', stat[0]), (75, 1150), fontsize=10)
    grad_ax.annotate("%10s %7.3f" % ('Mean :  ', stat[1]), (75, 1100), fontsize=10)
    grad_ax.annotate("%10s %7.3f" % ('25% :   ', stat[3]), (75, 1050), fontsize=10)
    grad_ax.annotate("%10s %7.3f" % ('75% :   ', stat[5]), (75, 1000), fontsize=10)
        
    grad_fig.canvas.draw()    
    
def learing(): 
    """
    MAchine Learning, Tensorflow 
    """
    # Tensorflow 
    import tensorflow as tf
    tf.set_random_seed(777)  # for reproducibility
    
    t_a = int(t_aSpbox.get()) - 1
    runner = x_test[t_a]
    t_g = int(runner[0])
    t_y = int(runner[1])
    t_p = int(runner[2])

    t_t = int(t_tSpbox.get()) + 1
    t_r = float(t_rSpbox.get())

    # placeholders for a tensor 
    W = tf.Variable(tf.random_normal([__________]), name='weight')
    b = tf.Variable(tf.random_normal([__________]), name='bias')
    
    X = tf.placeholder(tf.float32, shape=[None, _])
    Y = tf.placeholder(tf.int32, shape=[None, _])

    Y_one_hot = tf.one_hot(__________)  # one hot
    print("one_hot:", Y_one_hot)
    Y_one_hot = tf.________(Y_one_hot, [-1, nb_classes])
    print("reshape one_hot:", Y_one_hot)

    '''
    one_hot: Tensor("one_hot:0", shape=(?, 1, 7), dtype=float32)
    reshape one_hot: Tensor("Reshape:0", shape=(?, 7), dtype=float32)
    '''
    # tf.nn.softmax computes softmax activations
    # softmax = exp(logits) / reduce_sum(exp(logits), dim)
    logits = tf.matmul(X, W) + b
    hypothesis = tf.nn.______(logits)

    # Cross entropy cost/loss
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=_____,
                                                                     labels=tf.stop_gradient([________])))
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

    prediction = tf.______(hypothesis, 1)
    correct_prediction = tf.equal(_________, tf.argmax(Y_one_hot, 1))
    accuracy = tf.reduce_mean(tf.cast(________________, tf.float32))

    # Launch a session.
    with tf.Session() as sess:
        # Initializes global variables
        sess.run(tf.global_variables_initializer())
    
        # Fit the line
        log_ScrolledText.insert(END, '\nGender :'+gender_list[t_g]+', Age :'+str(t_y)+', Pace :'+str(t_p)+'\n', 'TITLE')
        log_ScrolledText.insert(END, '\n\nCost Decent & Accuracy\n\n','HEADER')
        log_ScrolledText.insert(END, "%10s %20s %20s" % ('Step', 'Cost', 'Accuracy(%)')+'\n\n')
        for step in range(t_t):
            _, cost_val, a_val = sess.run([optimizer, cost, accuracy], feed_dict={X: x_train, Y: y_train})
            
            if step % 100 == 0:
                print("Step: {:5}\tCost: {:.3f}\tAccuracy: {:.2%}".format(step, cost_val, a_val))
                log_ScrolledText.insert(END, "%10i %20.5f %20.7f" % (step, cost_val, a_val*100)+'\n')
        
        winner = [ t_g, t_y, t_p ]
        result = sess.run(hypothesis, feed_dict={X: [normalization(winner)]})
        grade_index = sess.run(tf.argmax(result, axis=1))
        grade = grade_list[grade_index[0]]
        log_ScrolledText.insert(END, '\n\n')
        log_ScrolledText.insert(END, "%30s" % ('One Hot & Grade Prediction  \n\n'), 'HEADER')
        log_ScrolledText.insert(END, "%30s" % (result))             
        log_ScrolledText.insert(END, '\n\n')
        if(grade_index[0]):
            log_ScrolledText.insert(END, "%30s" % (grade+'\n\n'), 'DisQualifier')
        else:
            log_ScrolledText.insert(END, "%30s" % (grade+'\n\n'), 'Qualifier') 
            
#main
main = Tk()
main.title("Logistic Regression Multinominal Classification")
main.geometry()

label=Label(main, text='Logistic Regression Multinominal Classification')
label.config(font=("Courier", 18))
label.grid(row=0,column=0,columnspan=6)

t_aVal  = IntVar(value=1)
t_aSpbox = Spinbox(main, textvariable=t_aVal ,from_=0, to=len(x_test), increment=1, justify=RIGHT)
#t_aSpbox.config(state='readonly')
t_aSpbox.grid(row=1,column=1)
t_aLabel=Label(main, text='Rank of runner : ')                
t_aLabel.grid(row=1,column=0)

t_tVal  = IntVar(value=10000)
t_tSpbox = Spinbox(main, textvariable=t_tVal ,from_=0, to=100000, increment=1000, justify=RIGHT)
#t_tSpbox.config(state='readonly')
t_tSpbox.grid(row=1,column=3)
t_tLabel=Label(main, text='Number of train : ')                
t_tLabel.grid(row=1,column=2)

t_rVal  = DoubleVar(value=1e-2)
t_rSpbox = Spinbox(main, textvariable=t_rVal ,from_=0, to=1, increment=1e-2, justify=RIGHT)
#t_rSpbox.config(state='readonly')
t_rSpbox.grid(row=1,column=5)
t_rLabel=Label(main, text='Learning rate : ')                
t_rLabel.grid(row=1,column=4)

Button(main,text="Histogram", height=2,command=lambda:histogram()).grid(row=2, column=0, columnspan=3, sticky=(W, E))
Button(main,text="Prediction", height=2,command=lambda:learing()).grid(row=2, column=3, columnspan=3, sticky=(W, E))

grad_canvas = FigureCanvasTkAgg(grad_fig, main)
grad_canvas.get_tk_widget().grid(row=3,column=0,columnspan=6)

log_ScrolledText = tkst.ScrolledText(main, height=15)
log_ScrolledText.grid(row=4,column=0,columnspan=6, sticky=(N, S, W, E))
log_ScrolledText.configure(font='TkFixedFont')
log_ScrolledText.tag_config('Qualifier', foreground='blue', font=("Helvetica", 16))
log_ScrolledText.tag_config('DisQualifier', foreground='red', font=("Helvetica", 16))
log_ScrolledText.tag_config('HEADER', foreground='gray', font=("Helvetica", 14), underline=1)
log_ScrolledText.tag_config('TITLE', foreground='orange', font=("Helvetica", 18), underline=1, justify='center')

main.mainloop()