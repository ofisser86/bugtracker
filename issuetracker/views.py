# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Ticket

# Create your views here.

class BugListView(ListView):
    model = Ticket
    template_name = 'issuetracker/list.html'


class BugDetailView(DetailView):
    model = Ticket
    template_name = 'issuetracker/detail.html'
