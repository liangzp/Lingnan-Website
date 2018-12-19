# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 20:34:10 2018

@author: lzt68
"""
#%%用于shell中快速引入库的代码
from my_app.models import User
from reward.models import Task,Material,Opinion
user=User.objects.filter(uname="16332092")[0]
task=Task.objects.filter(user=user).filter(description="奖学金")[0]
material=Material.objects.filter(task=task)[0]

#%%
from my_app.models import User
from reward.models import Task,Material
import os
tasklist=Task.objects.filter(description="奖学金")
rootpath="E:/工作事务/小组工作/大三上/管理信息系统/期末作业/project/Lingnan-Website/reward/pic/"
for task in tasklist:
    if os.path.exists(rootpath+task.user.uname):
        task.total_material=len(os.listdir(rootpath+task.user.uname))
    else:
        task.total_material=0
    task.save()
#%%录入课室信息
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
#%%给所有人初始化奖学金流程
from my_app.models import User
from reward.models import Task,Material

userlist=User.objects.all()
for user in userlist:
    if user.role=="student":
        checkorder=str(['self','16332124','16332144'])
        checkorder_char=str(['提交材料','学委审核','学工办第一次审核'])
        task=Task(user=user,description="奖学金",checkorder=checkorder,\
                  checkorder_char=checkorder_char,status=1,now_checker='self')
        #李子天学委，16332092
        #吕笳赈学工办大佬16332124
        task.save()
#%%清空所有申请
from my_app.models import Application
applist=Application.objects.all()
for i in range(len(applist)):
     app=applist[i]
     app.delete()
#%%清空所有课室
from my_app.models import Classroom
clalist=Classroom.objects.all()
for i in range(len(clalist)):
     cla=clalist[i]
     cla.delete()
#%%清空已有的材料和反馈
from my_app.models import User
from reward.models import Task,Material,Opinion
materiallist=Material.objects.all()
for i in range(len(materiallist)):
    material=materiallist[i]
    material.delete()
opinionlist=Opinion.objects.all()
for i in range(len(opinionlist)):
    opinion=opinionlist[i]
    opinion.delete()
