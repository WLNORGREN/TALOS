#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:57:48 2023

@author: wln
"""

import matplotlib.pyplot as plt
import numpy as np

scale = 7.5
w = 1000
A = lambda r: 2000 / r ** 2
m1x = -20
m1y = 0
m2x = 20
m2y = 0.001
m3x = 0
m3y = 20 * np.tan(np.radians(60))
m1vx = [-0.5 * scale]
m1vy = [np.sqrt(3) / 2 * scale]
m2vx = [-0.5 * scale]
m2vy = [-np.sqrt(3) / 2 * scale]
m3vx = [1 * scale]
m3vy = [0]
t = 1
i = 0

while abs(m2x) < w and abs(m2y) < w:
    r12 = np.sqrt((m2x - m1x) ** 2 + (m2y - m1y) ** 2)
    r13 = np.sqrt((m3x - m1x) ** 2 + (m3y - m1y) ** 2)
    m12a = A(r12)
    m13a = A(r13)
    m1ax = m12a * (m2x - m1x) / r12 + m13a * (m3x - m1x) / r13
    m1ay = m12a * (m2y - m1y) / r12 + m13a * (m3y - m1y) / r13

    m1vx.append(m1vx[i] + m1ax * t)
    m1dx = m1vx[i] * t + 0.5 * m1ax * t ** 2

    m1vy.append(m1vy[i] + m1ay * t)
    m1dy = m1vy[i] * t + 0.5 * m1ay * t ** 2

    r21 = np.sqrt((m1x - m2x) ** 2 + (m1y - m2y) ** 2)
    r23 = np.sqrt((m3x - m2x) ** 2 + (m3y - m2y) ** 2)
    m21a = A(r21)
    m23a = A(r23)
    m2ax = m21a * (m1x - m2x) / r21 + m23a * (m3x - m2x) / r23
    m2ay = m21a * (m1y - m2y) / r21 + m23a * (m3y - m2y) / r23

    m2vx.append(m2vx[i] + m2ax * t)
    m2dx = m2vx[i] * t + 0.5 * m2ax * t ** 2

    m2vy.append(m2vy[i] + m2ay * t)
    m2dy = m2vy[i] * t + 0.5 * m2ay * t ** 2

    r31 = np.sqrt((m1x - m3x) ** 2 + (m1y - m3y) ** 2)
    r32 = np.sqrt((m2x - m3x) ** 2 + (m2y - m3y) ** 2)
    m31a = A(r31)
    m32a = A(r32)
    m3ax = m31a * (m1x - m3x) / r31 + m32a * (m2x - m3x) / r32
    m3ay = m31a * (m1y - m3y) / r31 + m32a * (m2y - m3y) / r32

    m3vx.append(m3vx[i] + m3ax * t)
    m3dx = m3vx[i] * t + 0.5 * m3ax * t ** 2

    m3vy.append(m3vy[i] + m3ay * t)
    m3dy = m3vy[i] * t + 0.5 * m3ay * t ** 2

    m1x += m1dx
    m1y += m1dy
    m2x += m2dx
    m2y += m2dy
    m3x += m3dx
    m3y += m3dy

    plt.plot(m1x, m1y, 'b.', markersize=10)
    plt.plot(m2x, m2y, 'r.', markersize=10)
    plt.plot(m3x, m3y, 'g.', markersize=10)

    plt.axis('square')
    plt.xlim(-w, w)
    plt.ylim(-w, w)
    plt.pause(0.0001)

    i += 1

plt.show()
