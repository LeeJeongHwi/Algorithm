import tensorflow as tf
import numpy as np
from tkinter import *
import tkinter.scrolledtext as tkst
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import pandas as pd

#pandas 가 컬럼타입을 동적으로 추론하는데에는 많은 메모리가 소요 된다.
marathon_2015_2017 = pd.read_csv("../../data/marathon_2015_2017.csv",low_memory=False)

record = pd.DataFrame(marathon_2015_2017,
                      columns=['5K', '10K', '15K', '20K', 'Half', '30K', '35K', '40K', 'Official Time']).sort_values(by=['Official Time'])

record_list = record.values.tolist()

print(record.info())