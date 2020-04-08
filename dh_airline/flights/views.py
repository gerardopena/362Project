from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, CreateView, DeleteView
from . import Flight
# Create your views here.

class FlightList(ListView):
    template_name = 'flights/flight_list.html'
    context_object_name = 'flights'
    model = Flight

