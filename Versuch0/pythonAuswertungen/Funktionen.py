from math import *
from sympy import *
import sympy as sp
import numpy as np
import csv

def extrahieren(Y):
    return Y[0][0][0],Y[0][1][0],Y[1][0][0],Y[1][1][0]

def crop(x, indices):
    i0 = [y-1 for y in indices]
    y = []
    for i in i0:
        y = y + [x[i]]
    return y

def signifikanteStelle(a):
    if a==0:
        return 1
    s = -int(floor(log10(abs(a))))
    if a*(10**s) < 3:
        s+=1
        
    return s

def prod(z1,z2):
    #print("A",z1,"B",z2)
    temp=[]
    for i in range(len(z1)):
        temp.append(z1[i] * z2[i])
    #print("C",z1)
    return temp

#runden rundet so wie gefordert.
def runden(Y):
    #Y = [Array von Messwerten, Array von Messungenauigkeiten]
    y = Y[0]
    dy = Y[1]
    x = []
    dx = []
    for i in range(len(dy)):
        a=dy[i]
       # print(a,np.isnan(1.1))
        #if np.isnan(a):
        if 1 == 0:
            dx.append(np.nan)
            x.append(np.nan)
        else:
            s=signifikanteStelle(a)
            dx.append(round(10**(-s)*ceil(a*10**s),s))
            x.append(round(y[i],s))
            if s == 0:
                dx[i] = int(dx[i])
                x[i] = int(x[i])
    return [x,dx]

#Varianzgewichteter Mittelwert
def varMW(z,dz2):
    p = 0
    q = 0
    for i in range(len(z)):
        p += z[i]/(dz2[i])
        q += 1/(dz2[i])
    #print(p,q,z,dz2)
    return p/q


#Varianzgewichtete lineare Regression -> liefert Ausgleichsgrade der Form y=mx+b
def varLinReg(x,y,dy):
    dy2 = [asdf**2 for asdf in dy]
    m=(varMW(prod(x,y),dy2)-varMW(x,dy2)*varMW(y,dy2))/(varMW(prod(x,x),dy2)-varMW(x,dy2)**2)
    n=varMW(y,dy2)-varMW(x,dy2)*m
    dm2=abs(varMW(dy2,dy2)/(len(x)*(varMW(prod(x,x),dy2)-varMW(x,dy2)**2)))
    dn2=abs(varMW(prod(x,x),dy2)*dm2)
    print(m,n)
    return [runden([[m],[sqrt(dm2)]]),runden([[n],[sqrt(dn2)]])]
    #return [[[m],[sqrt(dm2)]],[[n],[sqrt(dn2)]]]

#setze xi in f ein:
def plug(f,X,x):
    temp = f
    for i in range(len(X)):
        #print(temp)
        temp = temp.subs(X[i],x[i])
    return temp

#Fehlerfortpflanzung, xi fehlerbehaftete Werte, f Formel in den Xi 
def mistake(x,dx,f,X):
    val = 0
    for i in range(len(X)):
        #print(val, f,X[i],X,x,dx[i])
        val += (plug(diff(f,X[i]),X,x)*dx[i])**2
    return sqrt(val)

#Transponiere Matrix
def transpose(M):
    N=[[] for i in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[i])):
            N[j].append(M[i][j])
    return N

#Lineare Regression für x1n = [x,x2,...,xn], wobei y gegen x geplottet ist
def linReg(x1n,dx1n,y,dy):        
    return varLinReg(x1n[0],y,dy)

def scmult(array,value):
    return [x*value for x in array]

def csv_to_named_arrays(file_name):
    # Dictionary für die benannten Arrays
    named_arrays = {}

    # Öffnen der CSV-Datei
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter =';')
        
        # Erste Zeile als Header (Spaltennamen) einlesen
        header = next(reader)
        header = [column.strip() for column in header]  # Entferne Leerzeichen in den Header-Werten

        # Sicherstellen, dass für jede Spalte im Header ein leeres Array existiert
        for column_name in header:
            named_arrays[column_name] = []
        
        # Die Daten in den jeweiligen Arrays speichern
        for row in reader:
            # Wenn eine Zeile weniger Spalten hat als der Header, fülle mit leeren Werten auf
            if len(row) < len(header):
                row.extend([''] * (len(header) - len(row)))  # Leere Werte für fehlende Spalten
            
            # Daten in die benannten Arrays speichern
            for i, value in enumerate(row):
                column_name = header[i]
                
                # Wenn der Wert eine Zahl ist, konvertiere sie von Komma zu Punkt und dann in float
                try:
                    # Ersetze ',' durch '.' und konvertiere in float
                    value = value.replace(',', '.') if value else value
                    if value:  # Nur konvertieren, wenn der Wert nicht leer ist
                        value = float(value)
                except ValueError:
                    # Falls der Wert keine Zahl ist, lasse ihn als String
                    pass

                # Speichern des Wertes in das passende Array
                named_arrays[column_name].append(value)

    return named_arrays

