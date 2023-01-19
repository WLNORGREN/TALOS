#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 12:46:57 2023

@author: wn
"""



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import KernelPCA



p = pd.read_csv('Astronomy_Datasets/planets.csv')




p_subset = p[['st_rad','st_raderr1','st_raderr2']].fillna(0)



print(p_subset.info())

pca = KernelPCA(n_components=1)

pca.fit_transform(p_subset)

print(pca.alphas_)
print(pca.lambdas_)