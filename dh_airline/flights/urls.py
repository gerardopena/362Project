from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('', views.BookPage.as_view(), name='bookpage'),
    path('s/', views.search, name='search'),
    path('flight/<pk>/', views.FlightDetailView.as_view(), name='detailpage'),

]