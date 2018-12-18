# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 16:20:37 2018

@author: lzt68
"""

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