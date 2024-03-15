#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:04:20 2022

@author: wn
"""
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
import numpy as np


planets = pd.read_csv('Astronomy_Datasets/planets.csv')

x = planets['pl_orbeccen'].fillna(0)
y = planets['pl_orbeccenerr1'].fillna(0)

from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept = True)

X = x[:,np.newaxis]

model.fit(X,y)

xfit = np.linspace(0,1,100)

Xfit = xfit[:,np.newaxis]


yfit = model.predict(Xfit)



model.fit(Xfit,yfit)




f = plt.figure()
a = plt.axes()
a.set_xlim([0,1])
a.set_ylim([0,0.4])

p = sns.scatterplot(x='pl_orbeccen',y='pl_orbeccenerr1',data=planets)

#a.plot(p)
a.plot(Xfit,yfit)




