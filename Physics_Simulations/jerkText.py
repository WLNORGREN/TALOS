# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 23:05:26 2021

@author: WN
"""

"""
Created on Thu Oct 28 02:32:08 2021

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
    tmptext = "x(t) = " + str(s2.get()) + "cos{" + str(s1.get()) + "t}"
    tmptext = "Position: $"+tmptext+"$ ${m}$"
    t = sp.symbols('t')
    ax.clear()
    ax.text(0.2, 0.8, tmptext, fontsize=10) 
    
    ax.text(0.2, 0.6, "Velocity: v(t) = $" + sp.latex(vel(t)) + "$ $\\frac{m}{s}$", fontsize=10) 
    ax.text(0.2, 0.4,"Acceleration: a(t) = $" + sp.latex(acc(t))+ "$ $\\frac{m}{s^2}$", fontsize=10) 
    
    ax.text(0.2, 0.2,"Jerk: j(t) = $" + sp.latex(jerk(t))+ "$ $\\frac{m}{s^3}$", fontsize=10) 
    canvas.draw()
    print("Test Phrase")
    
#This function displays the x-y graph to a matplotlib canvas    
def plot(value=None):
    
    bx.clear()
    x_vals = np.linspace(0, 10,10000)
    
    t = sp.symbols('t')
    
    lam_x = sp.lambdify(t, function(t), modules=['numpy'])
    vfunc = np.vectorize(lam_x)
    bx.plot(x_vals,vfunc(x_vals))
    
    lam_x = sp.lambdify(t, vel(t), modules=['numpy'])
    vfunc = np.vectorize(lam_x)
    bx.plot(x_vals,vfunc(x_vals),color='red')
    
    lam_x = sp.lambdify(t, acc(t), modules=['numpy'])
    vfunc = np.vectorize(lam_x)
    bx.plot(x_vals,vfunc(x_vals),color='green')
    
    lam_x = sp.lambdify(t, jerk(t), modules=['numpy'])
    vfunc = np.vectorize(lam_x)
    bx.plot(x_vals,vfunc(x_vals),color='purple')
   
    canvas2.draw()
    print("Hello World")
    print(s1.get())
    
def function(a):
    a = sp.symbols(str(a))
    return float(s2.get())*sp.cos(float(s1.get())*a)
    
def vel(a):
    return sp.diff(function(a),a)
    
def acc(a):
    return sp.diff(vel(a),a)

def jerk(a):
    return sp.diff(acc(a),a)
def lam(a,b):
    lam_x = sp.lambdify(a, b,'numpy')
    return lam_x
    
    
    

#Tkinter setup
root = tk.Tk()


#Coefficient entry

s1 = tk.Scale( root, 
           from_ = 0.1, to = 10,digits = 3, resolution = 0.1, orient=tk.HORIZONTAL,command= lambda x:(plot(),graph())) 
s1.grid(column=0,row=1)



s2 = tk.Scale( root, 
           from_ = 0.1, to = 10,digits = 3, resolution = 0.1,orient =tk.HORIZONTAL,command=lambda x:(plot(),graph())) 
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