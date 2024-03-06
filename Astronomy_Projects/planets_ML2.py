

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:54:58 2022

@author: wn
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


import os

#os.chdir('Documents')

planets = pd.read_csv('Astronomy_Datasets/planets.csv').head()

x = np.array(planets['st_mass'].fillna(0))
y = np.array(planets['st_optmag'].fillna(0))

from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept = True)
X = x[:, np.newaxis]
model.fit(X,y)
xfit = np.linspace(-1,11)
Xfit = xfit[:,np.newaxis]
yfit = model.predict(Xfit)
plt.xlim(0,4)
plt.ylim(0,20)
plt = sns.scatterplot(x='st_mass',y='st_optmag',hue = 'pl_letter', data=planets)
plt.plot(xfit,yfit)