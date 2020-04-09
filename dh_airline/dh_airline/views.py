from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, CreateView, DeleteView
from flights.models import Flight
# Create your views here.

class HomePage(TemplateView):
    template_name='homepage.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[''] = 'text'
        return context


class MyTripsPage(TemplateView):
    template_name = 'mytrips.html'

class LogIn(TemplateView):
    template_name = 'login.html'

class LogOut(TemplateView):
    template_name = 'logout.html'