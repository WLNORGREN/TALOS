#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 14:54:37 2023

@author: wln
"""

import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

planets = pd.read_csv('Astronomy_Datasets/planets.csv')


stdata = planets.loc[:,planets.columns.str.startswith('st_rad')]

stdata = stdata.fillna(0)

stdata['st_radlim'] = pd.get_dummies(stdata['st_radlim'])
stdata['st_radblend'] = pd.get_dummies(stdata['st_radblend'])

labels = stdata['st_rad'].astype('float')

features = stdata.drop('st_rad',axis=1)
features = features.astype('float')

X_train, X_test, y_train, y_test = train_test_split(features,labels,test_size=0.2)

X_train = np.array(X_train)
y_train = np.array(y_train)
X_test = np.array(X_test)
y_test = np.array(y_test)


normal = layers.Normalization()

normal.adapt(X_train)

model = keras.Sequential([
    normal,
    normal,
    layers.Dense(100,activation='relu'),
    layers.Dense(100,activation='relu'),

    layers.Dense(100,activation='relu'),
    layers.Dense(100,activation='relu'),
    layers.Dense(100,activation='relu'),
    layers.Dense(1)
    ])

model.compile(optimizer = keras.optimizers.Adam(learning_rate=0.1),loss=keras.losses.MeanAbsolutePercentageError())

model.fit(X_train,y_train,epochs=10)

planets['stmasspredict'] = model.predict(features)

model.evaluate(X_test,y_test)

y_pred = model.predict(X_test)

diff = y_pred - y_test

plt.hist(diff)



