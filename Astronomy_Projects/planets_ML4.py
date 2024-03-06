#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 12:31:48 2023

@author: wln
"""

import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers



planets = pd.read_csv('Astronomy_Datasets/planets.csv')


pfloat = planets.select_dtypes(include='float64')

pfloat =  pfloat.fillna(0)

pfloat_features = pfloat.copy()
pfloat_labels = pfloat_features.pop('pl_orbeccen')

pfloat_features = np.array(pfloat_features)

normalize = layers.Normalization()
normalize.adapt(pfloat_features)

pfloat_model = tf.keras.Sequential([
    normalize,
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(64, activation='relu'),
    
    layers.Dense(1)
    ])

pfloat_model.compile(loss = 'mean_absolute_error', optimizer = tf.keras.optimizers.Adam(0.001))

pfloat_model.fit(pfloat_features, pfloat_labels, epochs=1000)

planets['predicted_eccen'] = pfloat_model.predict(pfloat_features)

error = planets['pl_orbeccen'] - planets['predicted_eccen']

plt.hist(error, bins=25)

