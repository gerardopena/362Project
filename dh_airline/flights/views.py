from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, CreateView, DeleteView
from . import models
# Create your views here.

class FlightListView(ListView):
    template_name = 'flights/flight_list.html'
    context_object_name = 'flight'
    model = models.Flight
    
class BookPage(TemplateView):
    template_name = 'bookpage.html'