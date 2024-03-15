#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:53:30 2023

@author: wn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import GradientBoostingClassifier

from sklearn.model_selection import train_test_split

s = pd.read_csv('Astronomy_Datasets/stars.csv')

sub = s[['Spectral Class', 'Temperature (K)']]

sub.columns = ['Spectral Class', 'Temperature']

y = np.array(sub['Spectral Class'].fillna(0))

X = np.array(sub['Temperature'].fillna(0))

X = X[:,np.newaxis]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

g = GradientBoostingClassifier()

g.fit(X_train,y_train)

y_pred = g.predict(X_test)

g.train_score_

c = sub.corr()

sns.heatmap(c, cmap='viridis', annot=True)


