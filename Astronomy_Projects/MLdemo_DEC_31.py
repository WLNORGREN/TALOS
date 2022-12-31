#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 15:14:45 2022

@author: wn
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns


s = pd.read_csv('Astronomy_Datasets/stars.csv')

print(s.columns)

subset = s[['Luminosity(L/Lo)', 'Radius(R/Ro)']]

subset.columns = ['Luminosity','Radius']




k = KMeans(n_clusters=4)

k.fit_predict(np.array(subset))

print(k.labels_)

subset['cluster'] = k.labels_

p1 = plt.figure()
g = sns.scatterplot(x='Luminosity',y='Radius',data=subset,hue='cluster',palette='viridis')
p1.add_subplot(g)

p2 = plt.figure()
c = s[['Luminosity(L/Lo)', 'Radius(R/Ro)']].corr()
h = sns.heatmap(c,annot=True)
p2.add_subplot(h)