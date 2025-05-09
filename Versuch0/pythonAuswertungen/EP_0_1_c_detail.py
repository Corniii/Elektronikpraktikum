from Funktionen import *
from Plotten import *
import Funktionen as func
import Plotten as pt
from math import *
from sympy import *
import sympy as sp
import numpy as np
import random as rd
import scipy as sc


    

#Versuch 0 Aufgabe 1c) Messdaten:
titel = "Versuch 0 Aufgabe 1 (c) detailliert"
yName = "$U_{pp}/U_{0pp}$"
xName = "$\log(\omega / kHz)$"
yEinheit = "$dB$"
xEinheit = "$1$"
#pt.beschriften(titel = titel, xName = xName, yName = yName, xEinheit = xEinheit, yEinheit = yEinheit)
omega = [6.5,6.7,7.0,7.05,7.1,7.15,7.2,7.22,7.24,7.26,7.31,7.61,8,10]
Upp = [2.85,2.81,2.75,2.75,2.74,2.74,2.73,2.72,2.71,2.70,2.70,2.65,2.6,2.25]
U0pp = 4
y = [20*np.log10(element/U0pp) for element in Upp]
x = [np.log10(k) for k in omega]
dy = [0.2 for r in x]
dx = [0.03 for r in x]
plt.xlim(0.5,1.25)
plt.ylim = (-5.1,0)
pt.zeichne(x,y,dx,dy,titel,xName,yName,xEinheit,yEinheit,xBeginn = min(x), yBeginn = min(y), safe = True, tabelle=False)

plt.axhline(-3,color="red")
plt.show()


#m, dm, b, db = extrahieren(linReg([x], [dx], y,dy))


#m, dm, b, db = extrahieren(linReg([datenx], [fehlerx], dateny,fehlery))


#pt.plot_line_with_error(mz,bz,dmz,dbz,min(datenxz),max(datenxz),xName,yName,xEinheit,yEinheit,col='green')
#print(m,dm,b,db)



#xBeginn = min(datenx)
#yBeginn = min(dateny)



