# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Ticket

# Create your views here.

class BugListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'issuetracker/list.html'



class BugDetailView(DetailView):
    model = Ticket
    template_name = 'issuetracker/detail.html'

class RegisterView(CreateView):
    class Meta:
        form_class = UserCreationForm
        template_name = 'issuetracker/register.html'
        fields = '__all__'
        success_url = reverse_lazy('home')