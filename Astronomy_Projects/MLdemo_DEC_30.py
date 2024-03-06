#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 14:58:55 2022

@author: wn
"""
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('Astronomy_Datasets/sloan_survey.csv')



l = LinearRegression(fit_intercept=True)

y = np.array(data['ra'])

x = np.array(data['dec'])
X = x[:,np.newaxis]

l.fit(X,y)

X_test = np.linspace(-5,70,76)
X_test = X_test[:,np.newaxis]

y_test = l.predict(X_test)


def plot(X_test,y_test,x,y,data):
    f = plt.figure()
    plt.plot(X_test,y_test)
    s = sns.scatterplot(x=x,y=y,data=data)
    plt.xlabel('Right Ascension')
    plt.ylabel('Declination')
    plt.title('Right Ascension vs. Declination of SDSS objects')
    f.add_subplot(s)

def corr(data):
    f = plt.figure()
    c = data.corr()
    s = sns.heatmap(c,annot=True)
    plt.title('Correlation Matrix of Right Ascension and Declination')
    f.add_subplot(s)

    
plot(X_test,y_test,x,y,data)

corr(data[['ra','dec']])
