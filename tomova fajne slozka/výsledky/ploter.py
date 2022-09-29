from cProfile import label
from math import trunc
from tokenize import Double
from matplotlib.axis import YAxis
import pandas as pd
import matplotlib.pyplot as plt
import os 
from scipy.interpolate import make_interp_spline
import numpy as np
#print('what do you want to do? 1=file plot; 2=interest rate calculator')
#picker = input()

#if picker == '1':
dir_list = os.listdir()
for i in dir_list:
    if i.endswith('.txt'):
        lines = [[]]
        results=[[]]
        with open(i,'r') as f:
            print(i)
            for line in f:
                separ = line.strip().split('\t')
                lines.append(separ)
        time = []
        Cha = []
        Chb = []
        
        del lines[0:2]
        for k in range(len(lines)):
            for j in range(len(lines[k])):
                lines[k][j] = lines[k][j].replace(',', '.')
        #print(lines)
        for ik in lines:
           # print(ik)
            time.append(ik[0])
            Cha.append(float(ik[1]))
            Chb.append(float(ik[2])/100)
            

        x = time[:trunc(len(time)/4)]
        y = Cha[:trunc(len(Cha)/4)]
        y2 = Chb[:trunc(len(Chb)/4)]
        
        print (len(x), len(y2), len(y))
        '''
        y2_moving_avarage = []
        y_moving_avarage = []
        window_size = 3
        e=0
        for y2_iter in range(len(y2)-window_size):
            sumarum = 0
            for y2_iter in range(window_size+y2_iter):
              sumarum = sumarum + y2[y2_iter]
            sumarum = sumarum/window_size
            y2_moving_avarage.append(sumarum)
            if y2_iter == len(y2)-window_size:
                for kret in range(window_size):
                    y2_moving_avarage.append(sumarum)

        for y_iter in range(len(y)-window_size):
            sumarum = 0
            for y_iter in range(window_size+y_iter):
                sumarum = sumarum + y[y_iter]
            sumarum = sumarum/window_size
            y_moving_avarage.append(sumarum)
            if y_iter == len(y)-window_size:
                for kret in range(window_size):
                    y_moving_avarage.append(sumarum)

        print (len(x), len(y2_moving_avarage), len(y_moving_avarage))
        
        del y_moving_avarage[len(y_moving_avarage)-window_size-2:len(y_moving_avarage)]
        del y2_moving_avarage[len(y2_moving_avarage)-window_size-2:len(y2_moving_avarage)]
        del x[len(x)-window_size-2:len(x)]
        '''
        #print (len(time), len(y2_moving_avarage), len(y_moving_avarage))
        fig,ax=plt.subplots()
        ax.plot(x, y, color='C1')
        ax.set_xlabel('čas')
        ax.set_ylabel('napětí na 1. cívce [A]', color='C1')
        ax.xaxis.set_major_locator(plt.MaxNLocator(15))
        ax2 = ax.twinx()
        ax2.plot(x, y2, color='C0')
        ax2.set_ylabel('napětí na 2. cívce [A]', color='C0')
        plt.title('Průběh napětí')
        #plt.show() 
        i = i.split('.')
        i = i[0]
        plt.savefig('last3/' + i +'.png',bbox_inches='tight')
        plt.close()

