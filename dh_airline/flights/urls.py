from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('', views.BookPage.as_view(), name='bookpage')
]