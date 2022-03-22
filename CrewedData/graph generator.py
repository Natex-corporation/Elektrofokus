from turtle import pos
from matplotlib.axis import XAxis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('tranzistory1data.csv')

ax = df.plot(y="M1 - U [V]", x="M1 - I [mA]", kind="line", label = '0mV')
df.plot(y="M2 - U [V]", x="M2 - I [mA]", kind="line", ax=ax, color="C2", label = '20mV')
df.plot(y="M3 - U [V]", x="M3 - I [mA]", kind="line", ax=ax, color="C3", label = '50mV')
df.plot(y="M4 - U [V]", x="M4 - I [mA]", kind="line", ax=ax, color="C4", label = '100mV')

plt.ylabel(r'$\ U_{BE} (V)$')
plt.xlabel(r'$\ I_B (mA)$')
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.text(5,0.5,'vstupní charakteristiky')
plt.show()


df = pd.read_csv('tranzistory2data.csv')

ax = df.plot(x="M1 - U [V]", y="M1 - I [mA]", kind="line", label = '100mV')
df.plot(x="M2 - U [V]", y="M2 - I [mA]", kind="line", ax=ax, color="C2", label = '500mV')
df.plot(x="M3 - U [V]", y="M3 - I [mA]", kind="line", ax=ax, color="C3", label = '1000mV')
df.plot(x="M4 - U [V]", y="M4 - I [mA]", kind="line", ax=ax, color="C4", label = '2000mV')
plt.legend(loc='upper left')
plt.ylabel(r'$\ U_{CE} (V)$')
plt.xlabel(r'$\ I_B (mA)$',)
#plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.text(1,6.5,'převodní charakteristiky')
ax.xaxis.set_ticks_position("top")
plt.show()


df = pd.read_csv('tranzistory3data.csv')

ax = df.plot(x="M1 - U [V]", y="M1 - I [mA]", kind="line", label = '2000mV')
df.plot(x="M2 - U [V]", y="M2 - I [mA]", kind="line", ax=ax, color="C2", label = '4000mV')
df.plot(x="M3 - U [V]", y="M3 - I [mA]", kind="line", ax=ax, color="C3", label = '6000mV')
df.plot(x="M4 - U [V]", y="M4 - I [mA]", kind="line", ax=ax, color="C4", label = '8000mV')
plt.legend(loc='lower right')
plt.ylabel(r'$\ I_C (mA)$')
plt.xlabel(r'$\ U_{CE} (V)$')
ax.xaxis.set_ticks_position("top")
ax.yaxis.set_ticks_position("right")
plt.text(0.5,6.5,'výstupní charakteristiky')
#plt.gca().invert_yaxis()
#plt.gca().invert_xaxis()

plt.show()