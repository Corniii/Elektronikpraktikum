from math import *
import numpy as np
import matplotlib.pyplot as plt
from Funktionen import *
import Funktionen as func
 
import numpy as np
import matplotlib.pyplot as plt

def plot_line_with_error(m, b, dm, db, x_min, x_max, xsymbol = "x", ysymbol = "y", xEinheit = "", yEinheit = "", a = 1, color = "red", label = ""):
    """
    Plottet eine Gerade der Form y = mx + b und zeigt den Fehlerbereich
    durch die Parameter dm (Fehler der Steigung) und db (Fehler des y-Achsenabschnitts) an.
    
    :param m: Steigung der Geraden
    :param b: y-Achsenabschnitt der Geraden
    :param dm: Fehler der Steigung
    :param db: Fehler des y-Achsenabschnitts
    :param x_min: Minimaler x-Wert für den Plot
    :param x_max: Maximaler x-Wert für den Plot
    :param num_points: Anzahl der Punkte zur Darstellung der Geraden
    """
    # Generiere x-Werte
    x = np.linspace(x_min, x_max)
    # Berechne die y-Werte der Geraden und den Fehlerbereich
    y = m * x + b
    y_error_upper = (m + dm) * x + (b + db)  # obere Grenze des Fehlerbereichs
    y_error_lower = (m - dm) * x + (b - db)  # untere Grenze des Fehlerbereichs
    
    # Plot der Gerade
    plus = "+"
    if (b < 0):
        plus = "-"
    astr = str(a)
    if a == 1:
        astr = ""
    Y = runden([[m/a],[dm/a]])
    plt.plot(x, y, label=f'Fehlergerade ' +label + f': {ysymbol} = {astr}({Y[0][0]} ± {Y[1][0]}){xsymbol}{yEinheit}/{xEinheit} + ({b}±{db}){yEinheit}', color=color)
    
    # Fehlerbereich als gefüllte Fläche anzeigen
    #plt.fill_between(x, y_error_lower, y_error_upper, color='lightblue', alpha=0.5, label='Fehlerbereich')
def zeichneAG(datenx, dateny, fehlerx, fehlery,m,dm,b,db, titel, xName, yName, xEinheit, yEinheit, safe= False, log = False, xBeginn = 0, yBeginn = 0, a = 1):
#Ausgleichsgerade
    plot_line_with_error(m,b,dm,db,xBeginn,max(datenx), xsymbol = xName, ysymbol = yName,xEinheit = xEinheit, yEinheit = yEinheit, a = a)
    zeichne(datenx, dateny, fehlerx, fehlery, titel, xName, yName, xEinheit, yEinheit, log = False, xBeginn = 0, yBeginn = 0, safe = safe)
    plt.show()

def zeichne(datenx, dateny, fehlerx, fehlery, titel, xName, yName, xEinheit, yEinheit, log = False, xBeginn = 0, yBeginn = 0, safe = False, tabelle = True, style = 'bx'):
    plt.grid()
#Graph
    plt.plot(datenx,dateny,style)
    plt.errorbar(datenx,dateny, fehlery, xerr = fehlerx, fmt=style,capsize=6)

# Diagramm beschriften und anzeigen
    plt.xlabel(xName + " in " + xEinheit)
    plt.ylabel(yName + " in " + yEinheit)
    plt.title(titel)
    plt.axhline(xBeginn, color='black', linewidth=0.5)  # x-Achse
    plt.axvline(yBeginn, color='black', linewidth=0.5)  # y-Achse
    plt.legend()
    plt.grid(True)
    if safe:
        plt.savefig(titel + "_plot.jpg", format="jpeg", dpi=300)
    
#Tabelle
    if tabelle:
        Y = runden([dateny,fehlery])
        if fehlerx[0] == 0:
            X = [round(k,func.signifikanteStelle(k)+2)for k in datenx]
            data = [X,Y[0], Y[1]]
            columns = [xName + " in " + xEinheit, yName + " in " + yEinheit, '$\Delta$'+yName]
        else:
            X = runden([datenx,fehlerx])
            data = [X[0],Y[0], X[1], Y[1]]
            columns = [xName + " in " + xEinheit, yName + " in " + yEinheit, '$\Delta$' + xName, '$\Delta$'+yName]
        rows = [f'Reihe {i+1}' for i in range(len(datenx))]

        # Abbildung und Tabelle erstellen
        fig, ax = plt.subplots()
        ax.axis('off')  # Verhindert das Anzeigen von Achsen
        table = ax.table(cellText=list(zip(*data)), colLabels=columns, loc='center')
        if safe: 
            plt.savefig(titel + "_tabelle.jpg", format="jpeg", dpi=300)
        # Anpassung des Tabellenstils
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1.2, 1.2)
    
