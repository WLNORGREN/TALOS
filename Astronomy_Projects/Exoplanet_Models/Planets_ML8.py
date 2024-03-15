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



features = planets.select_dtypes('float64')

labels = planets['pl_letter']

labels = LabelEncoder().fit_transform(labels)

labels = tf.keras.utils.to_categorical(labels, num_classes=7)

X_train, X_test, y_train, y_test = train_test_split(features,labels,test_size=0.01)

X_train = np.array(X_train)
y_train = np.array(y_train)
X_test = np.array(X_test)
y_test = np.array(y_test)


normal = layers.Normalization()

normal.adapt(X_train)

model = keras.Sequential([
    normal,
    layers.Dense(100,activation='relu',),
    layers.Dense(100,activation='relu'),

    layers.Dense(100,activation='relu'),
    layers.Dense(100,activation='relu'),
    #layers.Dense(100,activation='softmax'),
    layers.Dense(7,activation='softmax')
    ])

model.compile(optimizer = keras.optimizers.Adam(learning_rate=0.0001),loss='mean_absolute_error',metrics=['accuracy'])

model.fit(X_train,y_train,epochs=10)

model.predict(features)

model.evaluate(X_test,y_test)

y_pred = model.predict(X_test)


