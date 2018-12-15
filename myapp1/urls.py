# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 21:23:46 2018

@author: lzt68
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]