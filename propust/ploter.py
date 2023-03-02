import pandas as pd
import matplotlib.pyplot as plt

freq = [4.70, 10, 22, 47, 100, 220, 470, 1000, 2200, 4700, 10000, 22000, 47000]
dol_R2 = [14, 14, 14, 14, 14, 13.92, 13.36, 11.44, 7.92, 4.4, 2.16, 1.12, 0.640]
hor_R2 = [0.200, 0.240, 0.400, 0.560, 1.04, 2.16, 4.2, 7.6, 11, 12.72, 12.64, 13.36, 13.52]
dol_R1 = [13.84, 13.12, 10.96, 7.28, 4.08, 2, 1.04, 0.240, 0.240, 0.240, 0.240, 0.240, 0.240]
hor_R1 = [2.48, 4.8, 8.64, 11.92, 13.36, 13.84, 14, 14, 14, 14, 14, 14, 14]

figure, axis = plt.subplots(2, 2, layout="constrained", sharex=True, sharey=True)
figure.supylabel('U[V]')
figure.supxlabel('f [Hz]')

 
# place legend outside
#axis[0, 0].legend(bbox_to_anchor = (1.0, 1), loc = 'upper left')


axis[0, 0].scatter(freq, dol_R1, marker = "+")
axis[0, 0].set_title(r"dolní propust R = 5 k$\Omega$ ")
axis[0, 0].set_xscale('log')
axis[0, 0].axvline(x = 35.36, ymin = 0.1, ymax = 0.9, color = 'r',
            label = 'mezní frekvence')

  
# For Cosine Function
axis[0, 1].scatter(freq, hor_R1, marker = "+")
axis[0, 1].set_title("horní propust R = 5 k$\Omega$")
axis[0, 1].set_xscale('log')
axis[0, 1].axvline(x = 35.36, ymin = 0.1, ymax = 0.90, color = 'r',
            label = 'mezní frekvence')

  
# For Tangent Function
axis[1, 0].scatter(freq, dol_R2, marker = "+")
axis[1, 0].set_title("dolní propust R = 1 k$\Omega$")
axis[1, 0].set_xscale('log')
axis[1, 0].axvline(x = 159.15, ymin = 0.1, ymax = 0.90, color = 'r',
            label = 'mezní frekvence')

  
# For Tanh Function
axis[1, 1].scatter(freq, hor_R2, marker = "+")
axis[1, 1].set_title("horní porpust R = 1 k$\Omega$")
axis[1, 1].set_xscale('log')
axis[1, 1].axvline(x = 159.15, ymin = 0.1, ymax = 0.90, color = 'r',
            label = 'mezní frekvence')
#figure.add_subplot(1, 1, 1, frame_on=False)
#plt.legend(bbox_to_anchor = (1.0, 1), loc = 'best')

plt.savefig(r"C:\Users\david\Desktop\david\programing\Elektrofokus\propust\lul.png")
plt.show()