import sys
from matplotlib.pyplot import text
from setuptools import Command
import csv_generator as cs
from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("300x200")

def get_data():
   #labelsource.config(text= entry_starting.get(), font= ('Helvetica 13'))
   #labelendpoint.config(text = entry_end.get(), font= ('Helvetica 13'))

   cs.csv_generator(entry_starting.get(), entry_end.get())

start = Frame(win)
csv_generatorF = Frame(win)

def Change_to_start():
   start.pack(fill='both', expand=1)
   csv_generatorF.pack_forget()
def change_to_csv_generetorF():
   csv_generatorF.pack(fill='both', expand=1)
   start.pack_forget()

entry_starting = Entry(csv_generatorF, width= 42)
entry_starting.place(relx= .5, rely= .4, anchor= CENTER)
entry_end = Entry(csv_generatorF, width = 42)
entry_end.place(relx= .5, rely= .6, anchor= CENTER)
entry_starting.insert(0, 'path to file whict you want to convert')
entry_end.insert(0, 'path to where do you want to store it')


ttk.Button(win, text='switch to start', command=Change_to_start).place(relx=.25, rely=.1, anchor=CENTER)
ttk.Button(win, text='switch to csv_generator', command=change_to_csv_generetorF).place(relx=.25,rely=.2,anchor=CENTER)
ttk.Button(csv_generatorF, text= "Click to Generate", command= get_data).place(relx= .75, rely= .5, anchor= CENTER)

win.mainloop()
important_info = cs.csv_generator('starting_files','csv_files')