from cProfile import label
from math import trunc
from time import sleep
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
            #print(ik)
            time.append(ik[0])
            Cha.append(float(ik[1]))
            Chb.append(float(ik[2])/100)
            

        x = time[:trunc(len(time)/4)]
        y = Cha[:trunc(len(Cha)/4)]
        y2 = Chb[:trunc(len(Chb)/4)]
        
        print (len(x), len(y2), len(y))



        y2_avarage = []
        y2aproximater = 2
        for y2aproximater in range(len(y2)-2):
            av = 0
            av = y2[y2aproximater] +y2[y2aproximater+2]+ y2[y2aproximater+1] + y2[y2aproximater-1]+y2[y2aproximater-2]
            av = av/5
            y2_avarage.append(av)

        y_avarage = []
        yaproximater = 2
        for yaproximater in range(len(y2)-2):
            av = 0
            av = y[yaproximater] + y[yaproximater-2]+y[yaproximater+1]+y[yaproximater+2] + y[yaproximater-1]
            av = av/5
            y_avarage.append(av)

        #print(y2_avarage)
        #print(y_avarage)
        #sleep(5)
      
      
        del x[len(x)-2:len(x)]
        del x[0:3]
        del y_avarage[0:3]
        del y2_avarage[0:3]
        #print (len(time), len(y2_moving_avarage), len(y_moving_avarage))
        fig,ax=plt.subplots()
        ax.plot(x, y_avarage, color='C1')
        ax.set_xlabel('čas')
        ax.set_ylabel('napětí [V]', color='C1')
        ax.xaxis.set_major_locator(plt.MaxNLocator(15))
        ax2 = ax.twinx()
        ax2.plot(x, y2_avarage, color='C0')
        ax2.set_ylabel('proud [A]', color='C0')
        plt.title('Průběh napětí proudu')
        #plt.show() 
        i = i.split('.')
        i = i[0]
        plt.savefig('last3/' + i +'.png',bbox_inches='tight')
        plt.close()

