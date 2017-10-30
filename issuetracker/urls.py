# -*- coding: utf-8 -*-
from django.conf.urls import url
from issuetracker import views

urlpatterns = [
    url(r'^$', views.bugList, name='home' ),
]