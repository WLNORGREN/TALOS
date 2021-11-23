# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 17:19:33 2021

@author: WN
"""

from bioinfokit import analys, visuz
df = analys.get_data('volcano').data
df.head(2)
visuz.gene_exp.volcano(df=df, lfc='log2FC', pv='p-value',show=True)


# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 02:32:08 2021

@author: WN
"""

import matplotlib
from bioinfokit import analys, visuz
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


matplotlib.use('TkAgg')

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
    
#Updating functions
    
    
a = visuz.gene_exp.volcano(df=df, lfc='log2FC', pv='p-value')
print(type(a))
    

#This function displays the x-y graph to a matplotlib canvas    
def plot(event=None):
    
    
    df = analys.get_data('volcano').data
    
    df.head(2)
    bx.clear()
    bx.plot(vplot())
    canvas2.draw()
    print("Hello World")
    
def vplot(event=None):    
    return visuz.gene_exp.volcano(df=df, lfc='log2FC', pv='p-value')
    

#Tkinter setup
root = tk.Tk()
mainframe = tk.Frame(root)
mainframe.pack()

#Formula entry
entry = tk.Entry(mainframe, width=70)
entry.pack()
entry.insert(0, "2")

#Label entry
label = tk.Label(mainframe)
label.pack()
#Quit button

quitButton = tk.Button(root, text = "Quit", command = root.destroy)
quitButton.pack()
#Formula canvas
fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)


canvas = FigureCanvasTkAgg(fig, master=label)
canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
canvas._tkcanvas.pack(side="top", fill="both", expand=True)




#Graph display
fig2 = Figure(figsize=(5, 4), dpi=100)
x= np.arange(0, 3, .01)
bx = fig2.add_subplot(111)
bx.plot(x, x**(int(entry.get())))

canvas2 = FigureCanvasTkAgg(fig2, master=root)  # A tk.DrawingArea.
canvas2.draw()
canvas2.get_tk_widget().pack(side="top", fill="both", expand=True)


ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)




#plot()


root.mainloop()