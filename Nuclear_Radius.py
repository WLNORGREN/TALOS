# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 00:29:31 2021

@author: WN
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 03:34:23 2021

@author: WN
"""


import matplotlib
import sympy as sp
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


matplotlib.use('TkAgg')

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
    
#Updating functions

    
#This function displays the function to be graphed in a Latex format to a matplotlib canvas
def graph(value=None):
    tmptext = "R = {r_0}A^{1/3}"
    tmptext = "$"+tmptext+"$"
    
    tmptext2 = "R= " + str(s1.get())+"(1.2)^{1/3} = " + str(float(s1.get()**(1/3)*1.2)) 
    tmptext2 = "$"+tmptext2+"$" + " femtometers."

    ax.clear()
    ax.text(0.2, 0.6, tmptext, fontsize=25)  
    ax.text(0.2, 0.2, tmptext2, fontsize=10)
    canvas.draw()
    print("Test Phrase")
    
#This function displays the x-y graph to a matplotlib canvas    
def plot(value=None):
    
    bx.clear()
    x_vals = np.linspace(0, 100,100)
    
    t = sp.symbols('t')
    markers_on = [int(s1.get())]
    
    lam_x = sp.lambdify(t, function(t), modules=['numpy'])
    vfunc = np.vectorize(lam_x)
    bx.plot(x_vals,vfunc(x_vals),'-gD',markevery=markers_on)
    
    
   
    canvas2.draw()
    print("Hello World")
    print(s1.get())
    
def function(a):
    a = sp.symbols(str(a))
    return 1.2*a**(1/3)
    

def lam(a,b):
    lam_x = sp.lambdify(a, b,'numpy')
    return lam_x
    
    
    

#Tkinter setup
root = tk.Tk()


#Coefficient entry

s1 = tk.Scale( root, 
           from_ = 1, to = 100,orient=tk.HORIZONTAL,command= lambda x:(plot(),graph())) 
s1.grid(column=0,row=1)

quitButton = tk.Button(root, text = "Quit", command = root.destroy)
quitButton.grid(column=3,row=1)
#Formula canvas
fig = matplotlib.figure.Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)


canvas = FigureCanvasTkAgg(fig, master=root)


canvas.get_tk_widget().grid(column=2,row=1)
   



#Graph display
fig2 = Figure(figsize=(5, 4), dpi=100)
bx = fig2.add_subplot(111)


canvas2 = FigureCanvasTkAgg(fig2, master=root)  # A tk.DrawingArea.
canvas2.draw()
canvas2.get_tk_widget().grid(column=2,row=2)


ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)



graph()
plot()


root.mainloop()
