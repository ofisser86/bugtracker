# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

def bugList(request):
    """Views for get"""
    return render(request, 'issuetracker/list.html', {})