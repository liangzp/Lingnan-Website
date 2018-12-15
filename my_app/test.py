# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 00:01:34 2018

@author: lzt68
"""
import pandas as pd
import numpy as np
import datetime

dayofweek=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
i=1
today=datetime.datetime.now()
targetday=today+datetime.timedelta(days=i)
dayofw=targetday.weekday()
data=pd.read_csv(dayofweek[dayofw]+'.csv',engine='python',encoding='utf-8')
'''
for i in range(1,14):
    today=datetime.datetime.now()
    targetday=today+datetime.timedelta(days=i)
    dayofw=targetday.weekday()
    data=pd.read_csv(dayofweek[dayofw])
'''