import pandas as pd
import matplotlib.pyplot as plt

freq = [4.70, 10, 22, 47, 100, 220, 470, 1000, 2200, 4700, 10000, 22000, 47000]
dol_R2 = [14, 14, 14, 14, 14, 13.92, 13.36, 11.44, 7.92, 4.4, 2.16, 1.12, 0.640]
hor_R2 = [0.200, 0.240, 0.400, 0.560, 1.04, 2.16, 4.2, 7.6, 11, 12.72, 12.64, 13.36, 13.52]
dol_R1 = [13.84, 13.12, 10.96, 7.28, 4.08, 2, 1.04, 0.240, 0.240, 0.240, 0.240, 0.240, 0.240]
hor_R1 = [2.48, 4.8, 8.64, 11.92, 13.36, 13.84, 14, 14, 14, 14, 14, 14, 14]


figure, axis = plt.subplots(2, 2)
  
# For Sine Function
axis[0, 0].plot(freq, dol_R1)
axis[0, 0].set_title("dolní propust R = 5k ")
#axis[0, 0].set_ylable('U[V]')
#axis[0, 0].set_xlable('f[Hz]')
  
# For Cosine Function
axis[0, 1].plot(freq, hor_R1)
axis[0, 1].set_title("horní propust R = 5k")
#axis[0, 0].set_ylable('U[V]')
#axis[0, 0].set_xlable('f[Hz]')
  
# For Tangent Function
axis[1, 0].plot(freq, dol_R2)
axis[1, 0].set_title("dolní propust R = 1k")
#axis[0, 0].set_ylable('U[V]')
#axis[0, 0].set_xlable('f[Hz]')
  
# For Tanh Function
axis[1, 1].plot(freq, hor_R2)
axis[1, 1].set_title("horní porpust R = 1k")
#axis[0, 0].set_ylable('U[V]')
#axis[0, 0].set_xlable('f[Hz]')
figure.add_subplot(1, 1, 1, frame_on=False)

plt.xlabel('f[Hz]')
plt.ylabel('U[V]')
plt.show()