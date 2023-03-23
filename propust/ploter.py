import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('freq.csv')
from scipy.optimize import curve_fit

freq = [4.70, 10, 22, 47, 100, 220, 470, 1000, 2200, 4700, 10000, 22000, 47000]
dol_R2 = [14, 14, 14, 14, 14, 13.92, 13.36, 11.44, 7.92, 4.4, 2.16, 1.12, 0.640]
hor_R2 = [0.200, 0.240, 0.400, 0.560, 1.04, 2.16, 4.2, 7.6, 11, 12.72, 12.64, 13.36, 13.52]
dol_R1 = [13.84, 13.12, 10.96, 7.28, 4.08, 2, 1.04, 0.240, 0.240, 0.240, 0.240, 0.240, 0.240]
hor_R1 = [2.48, 4.8, 8.64, 11.92, 13.36, 13.84, 14, 14, 14, 14, 14, 14, 14]
dol_faz_1 = []
print (df)
dol_faz_1 = df[' faz_posun Dolní propust']
hor_faz_1 = []
hor_faz_1 = df[' Faz_posun Horní propust']
dol_faz_2 = []
dol_faz_2 = df[' faz_posun Dolní propust 2']
hor_faz_2 = []
hor_faz_2 = df[' Faz_posun Horní propust 2']


'''figure2, axis2 = plt.subplots(2,2, layout='constrained', subplot_kw={'projection': 'polar'})
#figure2, axis2 = plt.subplots(2, 2, layout="constrained")
#axis2[0,0].set_rmax(47000)
axis2[0, 0].set_rticks(freq)
axis2[0, 0].scatter(dol_faz_1, freq)
axis2[0, 0].set_rscale('symlog')

axis2[0, 1].set_rticks(freq)
axis2[0, 1].set_rscale('symlog')
axis2[0, 1].scatter(hor_faz_1, freq)
#axis2[0, 1].set_xscale('log')
axis2[1, 0].set_rticks(freq)
axis2[1, 0].set_rscale('symlog')
axis2[1, 0].scatter(dol_faz_2, freq)
#axis2[1, 0].set_xscale('log')
axis2[1, 1].set_rticks(freq)
axis2[1, 1].set_rscale('symlog')
axis2[1, 1].scatter(hor_faz_2, freq)
#axis2[1, 1].set_xscale('log')
plt.show()'''
figure2, axis2 = plt.subplots(2, 2, layout="constrained")
figure2.supylabel('rad')
figure2.supxlabel('f [Hz]')
axis2[0, 0].scatter(freq, dol_faz_1, marker = "+")
axis2[0, 0].set_title('dolní propust R = 5 k$\Omega$')
#axis2[0, 0].set_ylabel('rad')
#axis2[0, 0].set_xlabel('f [Hz]')
axis2[0, 0].set_xscale('log')
axis2[0, 1].scatter(freq, hor_faz_1, marker = "+")
axis2[0, 1].set_title('horní propust R = 5 k$\Omega$')
#axis2[0, 1].set_ylabel('rad')
#axis2[0, 1].set_xlabel('f [Hz]')
axis2[0, 1].set_xscale('log')
axis2[1, 0].scatter(freq, dol_faz_2, marker = "+")
axis2[1, 0].set_title('dolní propust R = 1 k$\Omega$')
#axis2[1, 0].set_ylabel('rad')
#axis2[1, 0].set_xlabel('f [Hz]')
axis2[1, 0].set_xscale('log')
axis2[1, 1].scatter(freq, hor_faz_2, marker = "+")
axis2[1, 1].set_title('horní porpust R = 1 k$\Omega$')
#axis2[1, 1].set_ylabel('rad')
#axis2[1, 1].set_xlabel('f [Hz]')
axis2[1, 1].set_xscale('log')
plt.savefig('lol1.png')
#plt.show()

max_voltage = 14
voltage_err =0.04
for i in range(len(dol_R2)):
    dol_R2[i] = 10*np.log10(dol_R2[i]/max_voltage)
    hor_R2[i] = 10*np.log10(hor_R2[i]/max_voltage)
    dol_R1[i] = 10*np.log10(dol_R1[i]/max_voltage)
    hor_R1[i] = 10*np.log10(hor_R1[i]/max_voltage)


figure, axis = plt.subplots(2, 2, layout="constrained")
figure.supylabel('H [dB]')
figure.supxlabel('f [Hz]')

def func(x, k, a, L):
    return (L/(1+np.exp(-k*(x-a))))



p = np.linspace(min(freq)-3, max(freq)+5, 100000)
parsDR2, covDR2 = curve_fit(f=func, xdata=np.log(freq), ydata=dol_R2, bounds=([0., 0., -20.], [3., 10., -15.]))#, sigma=1./(np.log((yerr*eff))**2)
parsHR2, covHR2 = curve_fit(f=func, xdata=np.log(freq), ydata=hor_R2, bounds=([-3., 0., -20.], [0., 10., -15.]))
parsDR1, covDR1 = curve_fit(f=func, xdata=np.log(freq), ydata=dol_R1, bounds=([0., 0., -20.], [3., 10., -15.]))
parsHR1, covHR1 = curve_fit(f=func, xdata=np.log(freq), ydata=hor_R1, bounds=([-3., 0., -20.], [0., 10., -15.]))


axis[0, 0].scatter(freq, dol_R1, marker = "+")
axis[0, 0].set_title("dolní propust R = 5 k$\Omega$ ")
axis[0, 0].set_xscale('log')
axis[0, 0].axvline(x = 35.36, ymin = 0.1, ymax = 0.9, color = 'r', label = 'mezní frekvence')
axis[0, 0].plot(p, func(np.log(p), *parsDR1), c="m")


axis[0, 1].scatter(freq, hor_R1, marker = "+")
axis[0, 1].set_title("horní propust R = 5 k$\Omega$")
axis[0, 1].set_xscale('log')
axis[0, 1].axvline(x = 35.36, ymin = 0.1, ymax = 0.9, color = 'r', label = 'mezní frekvence')
axis[0, 1].plot(p, func(np.log(p), *parsHR1), c="m")


axis[1, 0].scatter(freq, dol_R2, marker = "+")
axis[1, 0].set_title("dolní propust R = 1 k$\Omega$")
axis[1, 0].set_xscale('log')
axis[1, 0].axvline(x = 159.15, ymin = 0.1, ymax = 0.9, color = 'r', label = 'mezní frekvence')
axis[1, 0].plot(p, func(np.log(p), *parsDR2), c="m")


axis[1, 1].scatter(freq, hor_R2, marker = "+")
axis[1, 1].set_title("horní porpust R = 1 k$\Omega$")
axis[1, 1].set_xscale('log')
axis[1, 1].axvline(x = 159.15, ymin = 0.1, ymax = 0.9, color = 'r', label = 'mezní frekvence')
axis[1, 1].plot(p, func(np.log(p), *parsHR2), c="m")

#figure.add_subplot(1, 1, 1, frame_on=False)
#plt.legend(bbox_to_anchor = (1.0, 1), loc = 'best')

plt.savefig("lul.png")
#plt.show()