from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, CreateView, DeleteView, DetailView
from .models import Flight
from . import models
# Create your views here.

def search(request):
    try:
        orig = request.GET.get('origin')
        dest = request.GET.get('destination')
    except:
        orig = None
        dest = None
    if orig and dest:
        flights = Flight.objects.filter(origin=orig, destination=dest)
        context = {'dest' : dest, 'orig' : orig, 'flights': flights}
        template = 'flights/flight_list.html'
        if not flights:
            context = {'DNE' : 'Invalid Search'}
            template = 'bookpage.html/'
    elif orig:
        flights = Flight.objects.filter(origin=orig)
        context = {'orig' : orig, 'flights': flights}
        template = 'flights/flight_list.html'
        if not flights:
            context = {'DNE' : 'Invalid Search'}
            template = 'bookpage.html/'
    elif dest:
        flights = Flight.objects.filter(destination=dest)
        context = {'dest' : dest, 'flights': flights}
        template = 'flights/flight_list.html'
        if not flights:
            context = {'DNE' : 'Invalid Search'}
            template = 'bookpage.html/'
    else:
        template = 'bookpage.html/'
        context = {}
    return render(request, template, context)



class FlightDetailView(DetailView):
    context_object_name = 'flight_details'
    model = models.Flight
    template_name = 'flights/flight_detail.html'


class FlightListView(ListView):
    template_name = 'flights/flight_list.html'
    context_object_name = 'flights'
    model = models.Flight


class BookPage(TemplateView):
    template_name = 'bookpage.html'