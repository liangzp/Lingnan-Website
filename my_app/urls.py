# -*- coding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('testtemplate/',views.testtemplate, name='testtemplate'),
    path('login/',views.login, name='login'),
    path('login/loginsuccess.html',views.loginsuccess, name='loginsuccess'),
    url(r'^manage/$',views.manage, name='manage'),
    path(r'managestu/', views.managestu),
    path(r'managetea/', views.managetea),
    path(r'testurl/<int:year>/test/', views.testurl),
    path(r'applypage/', views.applypage),
    path(r'applysuccess/', views.applysuccess),
    path(r'checkapplication/', views.checkapplication),
    path(r'checkallapplication/', views.checkallapplication),
    path(r'permitapplication/', views.permitapplication),
    path(r'logout/', views.logout),
    path(r'updatestatus/', views.updatestatus),
    path(r'applyselclassroom/', views.applyselclassroom),
]


