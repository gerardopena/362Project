from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, CreateView, DeleteView
from flights.models import Flight
# Create your views here.

class IndexView(TemplateView):
    template_name='homepage.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[''] = 'text'
        return context


class WebsiteReserveView(ListView):
    template_name = 'website/reservepage.html'
    context_object_name = 'flights'
    model = Flight

