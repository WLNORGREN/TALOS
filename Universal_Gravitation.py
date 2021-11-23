# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 21:07:44 2021

@author: WN
"""



# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 02:32:08 2021

@author: WN
"""

import matplotlib 
import sympy as sp
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import scipy as scp


matplotlib.use('TkAgg')

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
    
#Updating functions

    
#This function displays the function to be graphed in a Latex format to a matplotlib canvas
def graph(value=None):
  
    r = sp.symbols('r')
    ax.clear()
    
    ax.text(0.2, 0.4, "Gravitational Acceleration = $" + sp.latex(function(r)) + "$", fontsize=10) 
    
    ax.text(0.2, 0.6, "Field Strength = " + str(scp.constants.G*int(s1.get())/(s2.get()**2)) + " $N/{kg}$", fontsize=10) 
 
    canvas.draw()
    print("Test Phrase")
    
#This function displays the x-y graph to a matplotlib canvas    
def plot(value=None):
    
    bx.clear()
    x_vals = np.linspace(0.1, 10,100)
    
    t = sp.symbols('t')
    
    
    markers_on = [int(s2.get())]
    lam_x = sp.lambdify(t, function(t), modules=['numpy'])
    vfunc = np.vectorize(lam_x)
    bx.plot(x_vals,vfunc(x_vals),'-gD',markevery=markers_on)
    

   
    canvas2.draw()
    print(scp.constants.G)
    print(s1.get())
    
def function(a):
    a = sp.symbols(str(a))
    return scp.constants.G*int(s1.get())/(a**2)
    
def vel(a):
    return sp.diff(function(a),a)
    
def acc(a):
    return sp.diff(vel(a),a)
def lam(a,b):
    lam_x = sp.lambdify(a, b,'numpy')
    return lam_x
    
    
    

#Tkinter setup
root = tk.Tk()


#Coefficient entry

s1 = tk.Scale( root, 
           from_ = 1, to = 100,orient=tk.HORIZONTAL,command= lambda x:(plot(),graph())) 
s1.grid(column=0,row=1)



s2 = tk.Scale( root, 
           from_ = 1, to = 100,orient =tk.HORIZONTAL,command=lambda x:(plot(),graph())) 
s2.grid(column=0,row=2)


quitButton = tk.Button(root, text = "Quit", command = root.destroy)
quitButton.grid(column=3,row=1)
#Formula canvas
fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
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