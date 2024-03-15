#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 11:27:55 2023

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



pfloat_labels = pfloat['st_mass']
pfloat_features = pfloat.drop('st_mass', axis=1)

X_train, X_test, y_train, y_test = train_test_split(pfloat_features,pfloat_labels, test_size=0.2)

X_train = np.array(X_train)
y_train = np.array(y_train)
X_test = np.array(X_test)
y_test = np.array(y_test)


normal = layers.Normalization()
normal.adapt(X_train)

stmass_model = keras.Sequential([
    normal,
    layers.Dense(64,activation='relu'),
    layers.Dense(64,activation='relu'),
    layers.Dense(64,activation='relu'),
    layers.Dense(64,activation='relu'),
    
    layers.Dense(1)    
])

stmass_model.compile(loss="mean_absolute_error",optimizer=keras.optimizers.Adam(learning_rate=0.001))
stmass_model.fit(X_train,y_train,epochs=10)

newmass = stmass_model.predict(pfloat_features)

planets['newmass'] = newmass

error = planets['st_mass'] - planets['newmass']

plt.hist(error, bins=25)

print(newmass)

y_pred = stmass_model.predict(X_test)

test_error = y_pred - y_test


