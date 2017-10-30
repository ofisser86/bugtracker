
# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import viewlist

urlpatterns = [
    url('/', viewlist, name='home' ),
]