# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 00:01:34 2018

@author: lzt68
"""
import pandas as pd
import numpy as np
import datetime
from my_app.models import Classroom

dayofweek=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
for i in range(1,14):
    today=datetime.datetime.now()
    targetday=today+datetime.timedelta(days=i)
    dayofw=targetday.weekday()
    data=pd.read_csv(dayofweek[dayofw]+'.csv',engine='python',encoding='utf-8')
    for j in range(len(data)):
        datapiece=list(data.loc[j])
        for k in range(3,len(datapiece)):
            if pd.isnull(datapiece[k]):
                datapiece[k]=1
            else:
                datapiece[k]=0        
        cla=Classroom(building=datapiece[0],dayofweek=dayofw+1,\
                      date=datetime.datetime.strftime(targetday,"%Y-%m-%d"),\
                      room=datapiece[1],maxnum=int(datapiece[2]),\
                      status=str(datapiece[3:]))
        cla.save()

