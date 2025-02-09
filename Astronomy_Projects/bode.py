#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:11:20 2022

@author: wn
"""

import pandas as pd
import numpy as np
import os

os.chdir('Astronomy_Datasets')

p = pd.read_csv('planets.csv')

#p['count'] = p.groupby('pl_hostname')['pl_hostname'].transform(count)



