# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 17:44:20 2018

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
    path('materialpage/submitnewmaterial/',views.submitnewmaterial),
    path('materialpage/savematerial/',views.savematerial),
    path('materialpage/editmaterial/',views.editmaterial),
    path('materialpage/deletematerial/',views.deletematerial),
    path('materialpage/editspecificmaterial/',views.editspecificmaterial),
    path('materialpage/saveedition/',views.saveedition),
    path('materialpage/submitdeletematerial/',views.submitdeletematerial),
    path('materialpage/viewmaterial/',views.viewmaterial),
    path('materialpage/viewspecificmaterial/',views.viewspecificmaterial),
    path('materialpage/checktask/',views.checktask),
    path('materialpage/checkspecifictask/',views.checkspecifictask),
    path('materialpage/checkspecificmaterial/',views.checkspecificmaterial),
    path('materialpage/savecheck/',views.savecheck),
    path('result/',views.reuslt),
    path('', views.rewardmain),
]
urlpatterns +=static("pic/", document_root="reward/pic/")