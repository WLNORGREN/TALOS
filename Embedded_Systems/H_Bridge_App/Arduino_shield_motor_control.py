#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 13:10:42 2023

@author: wln
"""

import pyfirmata
from pyfirmata import util
import tkinter as tk


directionA = 12
brakeA = 9
#speedA = 3

directionB = 13
brakeB = 8
#speedB = 11



port = '/dev/ttyACM3'
board = pyfirmata.Arduino(port)

speedA = board.get_pin('d:3:p')
speedB = board.get_pin('d:11:p')


def a_f():
    board.digital[directionA].write(1);
def a_b():
    board.digital[directionA].write(0);
def b_f():
    board.digital[directionB].write(1);
def b_b():    
    board.digital[directionB].write(0);
    
def a():
    board.digital[directionA].write(1);
    board.digital[brakeA].write(0);
    speedA.write(1.0);

def b():
    board.digital[directionB].write(1);
    board.digital[brakeB].write(0);
    speedB.write(1.0);
    

def off():
    board.digital[directionA].write(0);
    board.digital[brakeA].write(0);
    speedA.write(0);
    
    board.digital[directionB].write(0);
    board.digital[brakeB].write(0);
    speedB.write(0);

def msa(value):
    speedA.write(float(value))
    
def msb(value):
    speedB.write(float(value))
    
root = tk.Tk()
root.title("Arduino Motor Shield GUI")



scaleA = tk.Scale(root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, command=msa)


scaleB = tk.Scale(root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, command=msb)



selected_button_a = tk.StringVar()
selected_button_b = tk.StringVar()



button1 = tk.Radiobutton(root, text="Motor A Forward", value="Motor A Forward", variable=selected_button_a, command=a_f)
button2 = tk.Radiobutton(root, text="Motor A Backward", value="Motor A Backward", variable=selected_button_a, command=a_b)
button3 = tk.Radiobutton(root, text="Motor B Forward", value="Motor B Forward", variable=selected_button_b, command=b_f)
button4 = tk.Radiobutton(root, text="Motor B Backward", value="Motor B Backward", variable=selected_button_b, command=b_b)

a_button = tk.Button(root, text="Motor A", command=a)


b_button = tk.Button(root, text="Motor B", command=b)


no_button = tk.Button(root, text="Off", command=off)


scaleA.grid(row=1,column=0)
button1.grid(row=0,column=1)
button2.grid(row=1,column=1)
a_button.grid(row=2,column=1)

button3.grid(row=0,column=2)
button4.grid(row=1,column=2)
b_button.grid(row=2,column=2)
scaleB.grid(row=1,column=3)

no_button.grid(row=1,column=4)

    
    
    
root.mainloop()