#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:38:25 2023

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

planets = pd.read_csv('Astronomy_Datasets/planets.csv')

pfloat = planets.select_dtypes('float64')

pfloat = pfloat.fillna(0)

pfloat_labels = pfloat['pl_orbsmax']
pfloat_features = pfloat.drop('pl_orbsmax', axis=1)

X_train, X_test, y_train, y_test = train_test_split(pfloat_features, pfloat_labels, test_size=0.2)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

normal = layers.Normalization()

normal.adapt(X_train)

model_orbsmax = keras.Sequential([
    normal,
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)    
])

model_orbsmax.compile(optimizer=keras.optimizers.Adam(),loss=keras.losses.MeanSquaredError())

model_orbsmax.fit(X_train, y_train,epochs=10)

planets['orbspred'] = model_orbsmax.predict(pfloat_features)

y_pred = model_orbsmax.predict(X_test)

diff = y_pred - y_test

plt.hist(diff)





