# -*- coding: utf-8 -*-
from django.conf.urls import url
from issuetracker import views

urlpatterns = [
    url(r'^$', views.BugListView.as_view(), name='home' ),
    url(r'^(?P<pk>[0-9]+)/$', views.BugDetailView.as_view(), name='detail' ),
]