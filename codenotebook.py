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
