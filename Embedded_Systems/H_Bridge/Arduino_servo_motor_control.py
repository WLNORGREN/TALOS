#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:59:58 2023

@author: wln
"""

import pyfirmata
from pyfirmata import SERVO
import tkinter as tk
import time

port = '/dev/ttyACM1'
board = pyfirmata.Arduino(port)

servo_pin = 9
servo_pin2 = 8

board.digital[servo_pin].mode = SERVO
board.digital[servo_pin2].mode = SERVO
for i in range(10):
    board.digital[servo_pin].write(0)
    board.digital[servo_pin2].write(90)
    time.sleep(1)
    board.digital[servo_pin].write(90)
    board.digital[servo_pin2].write(0)
    time.sleep(1)
board.digital[servo_pin].write(0)
time.sleep(1)


