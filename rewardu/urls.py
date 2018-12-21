# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 10:42:10 2018

@author: lzt68
"""

from django.contrib import admin
from django.urls import include,path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('materialpage/', views.materialpage),
    path('materialpage/submitnewmaterialscore/',views.submitnewmaterialscore),
    path('materialpage/submitnewmaterialpublic/',views.submitnewmaterialpublic),
    path('materialpage/savematerialscore/',views.savematerialscore),
    path('materialpage/savematerialpublic/',views.savematerialpublic),
    path('materialpage/editmaterialscore/',views.editmaterialscore),
    path('materialpage/editmaterialpublic/',views.editmaterialpublic),
    path('materialpage/deletematerial/',views.deletematerial),
    path('materialpage/editspecificmaterialscore/',views.editspecificmaterialscore),
    path('materialpage/editspecificmaterialpublic/',views.editspecificmaterialpublic),
    path('materialpage/saveedition/',views.saveedition),
    path('materialpage/submitdeletematerial/',views.submitdeletematerial),
    path('materialpage/viewmaterial/',views.viewmaterial),
    path('materialpage/viewspecificmaterial/',views.viewspecificmaterial),
    path('materialpage/checktask/',views.checktask),
    path('materialpage/checkspecifictask/',views.checkspecifictask),
    path('materialpage/checkspecificmaterial/',views.checkspecificmaterial),
    path('materialpage/savecheck/',views.savecheck),
    path('', views.rewardmain),
]
urlpatterns +=static("pic/", document_root="rewardu/pic/")