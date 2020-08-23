# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('echo', views.echo, name='echo'),
    path('echo_once', views.echo_once, name='echo_once'),
]
