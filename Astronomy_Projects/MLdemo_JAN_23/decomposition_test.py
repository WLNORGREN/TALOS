#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 18:57:33 2023

@author: wn
"""

from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


s = pd.read_csv('Astronomy_Datasets/stars.csv')


sub = s[['Luminosity(L/Lo)', 'Radius(R/Ro)','Absolute magnitude(Mv)']]

sub.columns = ['Luminosity', 'Radius', 'Magnitude']

sub = np.array(sub)


p = PCA(n_components=1)

reduced = p.fit_transform(sub)
